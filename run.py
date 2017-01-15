import argparse

import sys

from scanner.file import *


def process_dir(path):
    txtfiles = []
    zipfiles = []
    subdirs = []
    print("processing : ", path)
    for f in os.listdir(path):
        if os.path.isdir(f):
            subdirs.append(f)
        else:
            ext = get_extension(f)
            if ext == '.txt':
                txtfiles.append(f)
            elif ext == '.zip':
                zipfiles.append(f)

    for subdir in subdirs:
        process_dir(subdir)
    for f in txtfiles:
        print("text file : ", f)
    for f in zipfiles:
        print("zip file : ", f)


parser = argparse.ArgumentParser(description='Scan bookscan images')
parser.add_argument('--src', help='source directory', default='./')
args = parser.parse_args()

src_dir = os.path.abspath(args.src)

# check source directory exists
if not os.path.exists(src_dir):
    print("source directory not found %s" % src_dir)
    sys.exit(1)

process_dir(src_dir)
