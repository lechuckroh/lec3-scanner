import io


class BookInfo:
    """
    Book information class
    """
    dir = None
    isbn = None
    owner = None
    title = None
    author = None
    orig_pub_date = None
    orig_title = None
    pub_date = None
    bought_date = None
    bought_price = None
    scan_date = None
    scan_pages = 0
    price = None


def merge_info(info1, info2):
    """
    Merge two BookInfos into one.
    info1 has priority on conflict
    :param info1: BookInfo 1
    :param info2: BookInfo 2
    :return: New merged BookInfo
    """
    info = BookInfo()
    info.isbn = _merge_value(info1.isbn, info2.isbn)
    info.owner = _merge_value(info1.owner, info2.owner)
    info.title = _merge_value(info1.title, info2.title)
    info.author = _merge_value(info1.author, info2.author)
    info.orig_pub_date = _merge_value(info1.orig_pub_date, info2.orig_pub_date)
    info.orig_title = _merge_value(info1.orig_title, info2.orig_title)
    info.pub_date = _merge_value(info1.pub_date, info2.pub_date)
    info.bought_date = _merge_value(info1.bought_date, info2.bought_date)
    info.bought_price = _merge_value(info1.bought_price, info2.bought_price)
    info.scan_date = _merge_value(info1.scan_date, info2.scan_date)
    info.scan_pages = _merge_value(info1.scan_pages, info2.scan_pages)
    info.price = _merge_value(info1.price, info2.price)
    return info


def _merge_value(value1, value2):
    if value1:
        return value1
    else:
        return value2


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
    info = BookInfo()
    for line in lines:
        key, value = _parse_line(line)
        if not key:
            continue
        if key == 'isbn':
            info.isbn = value
        elif key == 'owner':
            info.owner = value
        elif key == 'origPubDate':
            info.orig_pub_date = value
        elif key == 'origTitle':
            info.orig_title = value
        elif key == 'pubDate':
            info.pub_date = value
        elif key == 'boughtDate':
            info.bought_date = value
        elif key == 'boughtPrice':
            info.bought_price = value
        elif key == 'scanDate':
            info.scan_date = value
        elif key == 'scanPages':
            info.scan_pages = int(value)
        elif key == 'price':
            info.price = value
    return info


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
