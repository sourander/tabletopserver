# Table Top Server in AWS

This is my documentation or memo of deploying the app in AWS EC2.

# Deployment

### Prequisites
The demo deployment was done on t3.micro reserved instance. Elastic IP 13.49.168.238 had been reserved. An A record (Route 53) had also been created.

### Once logged in Ubuntu 18.04
First, install all packages:
```shell script
sudo apt update && sudo apt upgrade
sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools
sudo apt install python3-venv
sudo apt install nginx
```

Set up the Python project
```shell script
# Clone the repo
git clone https://github.com/sourander/tabletopserver
cd tabletopserver

# Create virtual environment
python3 -m venv venv

# Activate
source venv/bin/activate

# Get Python modules
pip install --upgrade pip
pip install -r requirements.txt
pip install gunicorn

# Optional: Test the server
# gunicorn --bind 13.49.168.238:80 wsgi:app

deactivate
```

Next, it is time to set up the systemd daemons for running the server.

**Contents: /etc/systemd/system/tabletop.service**
```shell script
[Unit]
Description=Gunicorn instance to serve tabletop
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/tabletopserver
Environment="PATH=/home/ubuntu/tabletopserver/venv/bin"
Environment="SECRET_KEY=generate_me_and_keep_hidden_from_github"
ExecStart=/home/ubuntu/tabletopserver/venv/bin/gunicorn \
           --workers 2 --bind unix:/tmp/tabletop.sock -m 007 wsgi:app

[Install]
WantedBy=multi-user.target
```

Create a backup of the original conf
```shell script
cd /etc/nginx
sudo copy nginx.conf back.nginx.conf
```

And configure the nginx with:

```shell script
user ubuntu;
worker_processes auto;
pid /run/nginx.pid;
include /etc/nginx/modules-enabled/*.conf;

events {
        worker_connections 768;
        # multi_accept on;
}

http {
        # Include MIME types
        include /etc/nginx/mime.types;
        
        # Fallback
        default_type application/octet-stream;

        # Basic Settings from NGINX.conf
        sendfile on;
        tcp_nopush on;
        tcp_nodelay on;
        keepalive_timeout 65;
        types_hash_max_size 2048;

        # Logging Settings
        access_log /var/log/nginx/access.log;
        error_log /var/log/nginx/error.log;

        # Virtual Host Configs
        include /etc/nginx/conf.d/*.conf;
        include /etc/nginx/sites-enabled/*;
        
        # SSL Settings
        ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
        ssl_prefer_server_ciphers on;

}
```

Create the site config to:

```shell script
cd /etc/nginx/sites-available/
touch tabletop
```

As:

```
server {
        listen 80;
        client_max_body_size 4G;

        # Set the domain
        server_name tabletop.wtf www.tabletop.wtf;

        # Set TTL
        keepalive_timeout 10;

        # Path for static files
        root /home/ubuntu/tabletopserver/static/;

        location / {
                include proxy_params;
                proxy_pass http://unix:/tmp/tabletop.sock;
        }
}
```

Test the script syntax and create a symbolic link to sites-enabled:

```shell script
# Check the config syntax
sudo nginx -t

# Create the symlink to included directory
sudo ln -s /etc/nginx/sites-available/tabletop /etc/nginx/sites-enabled

# Run the systemds
sudo systemctl start tabletop
sudo systemctl enable tabletop
sudo systemctl restart nginx
```



# Certification

```shell script
# Add certbot repo
sudo add-apt-repository ppa:certbot/certbot

# Install the tool
sudo apt install python-certbot-nginx

# This will add required lines to .../sites-enabled/tabletop
sudo certbot --nginx -d tabletop.wtf -d www.tabletop.wtf
```



# Continuous Deployment

Currently, the deployment is done manually. Log in to ssh and run:

```shell script
# Stop the service.
sudo systemctl stop tabletop.service

# Make sure not to touch the database. Git stash would be another way.
cd ~/tabletopserver
cp databases/corpus.db databases/corpus.db.backup 
git pull
cp databases/corpus.db.backup databases/corpus.db

# If new modules have been added or existing updated, run:
source venv/bin/activate
pip install -r requirements.txt
deactivate

sudo systemctl restart tabletop.service
```

# Creating a scheduled copy of database

Since all users of the website are allowed to vote words as too difficult to kids or adults, there is a danger that someone would change them all to 'extreme'.

As a precaution, the system currently creates a copy of `corpus.db` every Monday at 7.00 UTC. This was achieved by adding a line to crontab using `crontab -e`. The line is:

```shell script
0 7 * * 1 /usr/bin/python3 /home/ubuntu/backup_db.py -i /home/ubuntu/tabletopserver/databases/corpus.db -o /home/ubuntu/dbbackups > /home/ubuntu/dbbackups/log.txt
```

The 'backup_db.py' is a symbolic link to `tabletopserver/databases/_backup_db.py`