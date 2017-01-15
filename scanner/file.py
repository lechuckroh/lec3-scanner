import glob
import os

import errno


def mkdirs(path):
    """
    Make sure path exists
    :param path:
    :return:
    """
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise


def get_filenames(path, pattern):
    """
    Get filenames with matching pattern in given path
    :param path:
    :param pattern:
    :return:
    """
    cwd = os.getcwd()
    os.chdir(path)
    filenames = glob.glob(pattern)
    os.chdir(cwd)
    return filenames


def get_extension(path):
    """
    Get filename extension
    :param path:
    :return:
    """
    return os.path.splitext(path)[1]
