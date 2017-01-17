from unittest import TestCase, main
from scanner.info import *


class InfoTestCase(TestCase):
    def test_read_info_lines(self):
        isbn = '123456'
        owner = 'Lechuck Roh'
        orig_pub_date = '2014'
        orig_title = 'Original Book Title'
        pub_date = '2016-12-31'
        bought_date = '2017-01-01'
        bought_price = '35000'
        scan_date = '2017-01-03'
        scan_pages = 456
        price = '36000'

        bookinfo = read_info_str('''
            isbn=%s
            owner=%s
            origPubDate=%s
            origTitle=%s
            pubDate=%s
            boughtDate=%s
            boughtPrice=%s
            scanDate=%s
            scanPages=%s
            price=%s
        ''' % (isbn,
               owner,
               orig_pub_date,
               orig_title,
               pub_date,
               bought_date,
               bought_price,
               scan_date,
               scan_pages,
               price))

        self.assertEqual(isbn, bookinfo.isbn)
        self.assertEqual(owner, bookinfo.owner)
        self.assertEqual(orig_pub_date, bookinfo.orig_pub_date)
        self.assertEqual(orig_title, bookinfo.orig_title)
        self.assertEqual(pub_date, bookinfo.pub_date)
        self.assertEqual(bought_date, bookinfo.bought_date)
        self.assertEqual(bought_price, bookinfo.bought_price)
        self.assertEqual(scan_date, bookinfo.scan_date)
        self.assertEqual(scan_pages, bookinfo.scan_pages)
        self.assertEqual(price, bookinfo.price)

    def test_merge_info(self):
        info1 = BookInfo()
        info1.isbn = '123456789'
        info1.title = 'title1'
        info1.author = ''

        info2 = BookInfo()
        info2.isbn = '123456789'
        info2.title = 'title2'
        info2.author = 'author2'
        info2.scan_pages = 150
        info2.price = '25000'

        merged = merge_info(info1, info2)
        self.assertEqual(info1.isbn, merged.isbn)
        self.assertEqual(info1.title, merged.title)
        self.assertEqual(info2.author, merged.author)
        self.assertEqual(info2.scan_pages, merged.scan_pages)
        self.assertEqual(info2.price, merged.price)
        pass


if __name__ == '__main__':
    main()
