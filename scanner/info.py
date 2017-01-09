import io


class BookInfo:
    """
    Book information class
    """
    dir = None
    isbn = None
    owner = None
    title = None
    origin_title = None
    author = None
    orig_pub_date = None
    orig_title = None
    pub_date = None
    bought_date = None
    bought_price = None
    scan_date = None
    scan_pages = 0
    price = None


def read_info_file(filename, encoding="utf-8"):
    """
    Reads info from text file and returns BookInfo instance
    :param filename: text filename
    :param encoding: text file encoding
    :return: BookInfo instance
    """
    with open(filename, "r", encoding=encoding) as f:
        return read_info_lines(f.readlines())


def read_info_str(s):
    """
    Reads info from string and returns BookInfo instance
    :param s: multi-line string
    :return: BookInfo instance
    """
    with io.StringIO(s) as f:
        return read_info_lines(f.readlines())


def read_info_lines(lines):
    """
    Reads info from list of lines and returns BookInfo instance
    :param lines: list of lines
    :return: BookInfo instance
    """
    book = BookInfo()
    for line in lines:
        key, value = _parse_line(line)
        if not key:
            continue
        if key == 'isbn':
            book.isbn = value
        elif key == 'owner':
            book.owner = value
        elif key == 'origPubDate':
            book.orig_pub_date = value
        elif key == 'origTitle':
            book.orig_title = value
        elif key == 'pubDate':
            book.pub_date = value
        elif key == 'boughtDate':
            book.bought_date = value
        elif key == 'boughtPrice':
            book.bought_price = value
        elif key == 'scanDate':
            book.scan_date = value
        elif key == 'scanPages':
            book.scan_pages = int(value)
        elif key == 'price':
            book.price = value
    return book


def _parse_line(line):
    """
    Parses a line into key, value tuple
    :return key, value tuple
    """
    if line:
        tokens = line.split('=', 2)
        if len(tokens) == 2:
            return tokens[0].strip(), tokens[1].strip()
    return None, None
