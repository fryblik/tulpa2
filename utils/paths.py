import os

from functools import wraps


def memoize(func):
    """
    Memoization decorator.
    """
    cache = {}

    @wraps(func)
    def wrapped(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapped


@memoize
def get_root_dir_path():
    """
    Get the path to the project's root directory.

    :return: Absolute path to the project's root.
    """
    return os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


@memoize
def get_subdirectory_path(name: str):
    """
    Get the path to a subdirectory of the project's root directory.

    :param name: Name of the subdirectory.
    :return: Absolute path to the subdirectory.
    """
    root_dir = get_root_dir_path()
    subdirectory_path = os.path.join(root_dir, name)
    if not os.path.isdir(subdirectory_path):
        raise ValueError(f"Invalid subdirectory name: {name}")
    return subdirectory_path
