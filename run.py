import argparse

import sys
import zipfile

from scanner.file import *
from scanner.info import *


def process_dir(dirpath):
    txtfiles = []
    zipfiles = []
    subdirs = []
    print("processing : ", dirpath)
    for f in os.listdir(dirpath):
        filepath = os.path.join(dirpath, f)
        if os.path.isdir(filepath):
            subdirs.append(filepath)
        else:
            ext = get_extension(f)
            if ext == '.txt':
                txtfiles.append(filepath)
            elif ext == '.zip':
                zipfiles.append(filepath)

    for subdir in subdirs:
        process_dir(subdir)

    bookinfo = None
    for f in txtfiles:
        info = read_info_file(f)
        if not bookinfo:
            bookinfo = info
        else:
            bookinfo = merge_info(bookinfo, info)

    if bookinfo:
        print("%s : %s" % (dirpath, bookinfo.isbn))

    for f in zipfiles:
        with zipfile.ZipFile(f) as zf:
            filenames = zf.namelist()
            count = len(filenames)
            if bookinfo:
                if bookinfo.scan_pages != count:
                    print("scan pages mismatch. %d <> %d" %
                          (bookinfo.scan_pages, count))


parser = argparse.ArgumentParser(description='Scan bookscan images')
parser.add_argument('--src', help='source directory', default='./')
args = parser.parse_args()

src_dir = os.path.abspath(os.path.expanduser(args.src))

# check source directory exists
if not os.path.exists(src_dir):
    print("source directory not found %s" % src_dir)
    sys.exit(1)

process_dir(src_dir)
