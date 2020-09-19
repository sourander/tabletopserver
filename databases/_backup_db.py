import argparse
import os
import gzip
import shutil
from datetime import datetime

# Parse the arguments
parser = argparse.ArgumentParser()
parser.add_argument('--infile', '-i', type=str, required=True,
                    help='Path to corpus.db')
parser.add_argument('--outpath', '-o', type=str, required=True,
                    help='Path to output directory')
args = parser.parse_args()

# Input file and output directory
inputpath = args.infile
outpath = args.outpath

# Generate the output filename
# e.g. /absolute/to/dir/2020-12-31_corpus.db.gz
f_out_filename = datetime.today().strftime('%Y-%m-%d') + '_corpus.db.gz'
f_out_absolute = os.path.join(outpath, f_out_filename)

# Write the file as compressed
with open(inputpath, 'rb') as f_in:
    with gzip.open(f_out_absolute, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
