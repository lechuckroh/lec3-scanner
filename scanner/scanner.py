import os
import zipfile

from scanner.file import get_extension
from scanner.info import *


class Scanner:
    def scan(self, dirpath):
        """
        Scan sub-directories recursively
        :param dirpath: directory to scan
        """
        Scanner.process_dir(dirpath)

        subdirs = []
        for f in os.listdir(dirpath):
            filepath = os.path.join(dirpath, f)
            if os.path.isdir(filepath):
                subdirs.append(filepath)

        for subdir in subdirs:
            self.scan(subdir)

    @staticmethod
    def process_dir(dirpath):
        """
        process directory
        :param dirpath: directory to process
        :return bookinfo, zipfile list
        """
        txtfiles = []
        zipfiles = []
        print('processing : ', dirpath)
        for f in os.listdir(dirpath):
            filepath = os.path.join(dirpath, f)
            if os.path.isfile(filepath):
                ext = get_extension(f)
                if ext == '.txt':
                    txtfiles.append(filepath)
                elif ext == '.zip':
                    zipfiles.append(filepath)

        # no bookinfo in this directory
        if len(txtfiles) == 0 and len(zipfiles) == 0:
            return

        # Get bookInfo
        bookinfo = Scanner.get_bookinfo(txtfiles)

        # Validate and extract cover image
        for f in zipfiles:
            with zipfile.ZipFile(f) as zf:
                filenames = zf.namelist()
                count = len(filenames)
                if bookinfo and bookinfo.scan_pages != count:
                    print('scan pages mismatch. %d != %d' %
                          (bookinfo.scan_pages, count))

                # extract cover image file
                cover_filename = filenames[0]
                try:
                    ext = get_extension(cover_filename)
                    raw_bytes = zf.read(cover_filename)
                    dest = os.path.join(dirpath, 'cover' + ext)
                    Scanner.write_cover(raw_bytes, dest)
                except ValueError:
                    print('Failed to extract %s from %s' % (cover_filename, f))

        return bookinfo, zipfiles

    @staticmethod
    def get_bookinfo(txtfiles):
        bookinfo = None
        for f in txtfiles:
            info = read_info_file(f)
            if not bookinfo:
                bookinfo = info
            else:
                bookinfo = merge_info(bookinfo, info)
        return bookinfo

    @staticmethod
    def write_cover(raw_bytes, filepath):
        with open(filepath, 'wb') as f:
            f.write(raw_bytes)
