import argparse
import os

import sys

from scanner import scanner


parser = argparse.ArgumentParser(description='Scan bookscan images')
parser.add_argument('--src', help='source directory', default='./')
args = parser.parse_args()

src_dir = os.path.abspath(os.path.expanduser(args.src))

# check source directory exists
if not os.path.exists(src_dir):
    print("source directory not found %s" % src_dir)
    sys.exit(1)

# scan
scanner = scanner.Scanner()
scanner.scan(src_dir)
