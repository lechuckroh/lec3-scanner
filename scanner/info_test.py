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


if __name__ == '__main__':
    main()
