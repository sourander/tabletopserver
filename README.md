# tabletopserver
A flask based web server running various table top helpers. Currently included:

* Raiders of the North Sea setup shuffler. Allows the user to select which expansions are in play. The code shuffles the tokens and displays the setup as a grid.
* Just One word generator. Randomizes a Finnish noun. The Sqlite database (corpus.db) has been formed using wiktionary database dump.

More will be added when/if I find some table top game challenging. Potential helpers might be e.g. scoring calculators. Feel free to suggest a tool that you would find helpful.

## How to run?
As of now, the project is not online. During study time, it was temporarily deployed to AWS. For deployment guidance, check the MEMO.md

If you want to simply run this locally, do the following steps. This should work on Linux, Unix and MacOS. For details, check the links below.
* Install Python
  * For Windows: [Download from Python.org](https://www.python.org/downloads/)
  * For MacOS: [Use HomeBrew](https://brew.sh/index_fi)
  * For Linux: [Depends on your distro etc](https://realpython.com/installing-python/#how-to-install-python-on-linux)
* Install [pip](https://pip.pypa.io/en/stable/installation/)
* Install [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* Clone this repo
  * Run `git clone https://github.com/sourander/tabletopserver` in a directory where you want to place this
* *(Optional)* create [a virtual environment](https://realpython.com/python-virtual-environments-a-primer/)
* Run `pip install -r requirements.txt` inside the project folder
* Run `flask run` to start local Flask development server
* Navigate to the URL printed by Flask (default `localhost:5000`)
  * Close the server in Command Prompt/Terminal by pressing CTRL+C.