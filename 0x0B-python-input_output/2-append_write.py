#!/usr/bin/python3
"""Function that append"""


def append_write(filename="", text=""):
    """ function append_write """
    with open(filename, "a", encoding="utf-8") as z:
        return z.write(text)
