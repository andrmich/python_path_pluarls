"""
Retrive and print words from a URL.
"""

from urllib.request import urlopen
import sys


def fetch_words(url):
    """Fetch a list of words from a URL.

    Args:
        url: The URL of a UTF-8 text document.

    Returns:
        A list of strings containing the words from
        the document.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


# 'http://sixty-north.com/c/t.txt'

def print_items(items):
    """
    Print items one per line.
    :param items: An iterable series of printable items.
    :return:
    """
    for item in items:
        print(item)


def main(url):
    """
    Print each word from a text document from a URL.
    :param url: The URL of a UTF-8 text document.
    :return:
    """
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1])
