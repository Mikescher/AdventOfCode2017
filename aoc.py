#!/usr/bin/env python3

from os import path


def read_input(day):
    with open(path.join(path.dirname(__file__), "{:02d}_input.txt".format(day))) as f:
        return f.read()
