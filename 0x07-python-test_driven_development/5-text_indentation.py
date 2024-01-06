#!/usr/bin/python3
"""text_indentation function"""


def text_indentation(text):
    """adding 2 new lines after '.?:'

    Args:
        text: string text

    Raises:
        TypeError: if text is not string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for delim in ".?:":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])
    print(text, end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
