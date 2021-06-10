"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.
For dir with two files from hw1.py:
 universal_file_counter(test_dir, "txt")
6
universal_file_counter(test_dir, "txt", str.split)
6
"""
import logging
import os
from functools import reduce
from pathlib import Path
import numpy as np
from typing import Callable, Optional


def universal_file_counter(dir_path: str, file_extension: str, tokenizer: Optional[Callable] = None) -> int:
    return sum(list(CountFilesIterator(dir_path, file_extension, tokenizer)))


def test_count_lines():
    assert universal_file_counter("files/", "txt") == 10


def test_count_lines_tokenizer():
    assert universal_file_counter("files/", "txt", lambda x: x.split()) == 12


class CountFilesIterator(object):
    def __init__(self, dir_path: str, file_extension: str, tokenizer: Optional[Callable] = None):
        self.dir_path = dir_path
        self.files = list(filter(lambda x: x.endswith(file_extension), os.listdir(dir_path)))
        self.iterator = 0
        self.tokenizer = tokenizer

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if self.iterator == len(self.files):
            raise StopIteration()
        with open(self.dir_path + self.files[self.iterator]) as f:
            self.iterator += 1
            if self.tokenizer is not None:
                return len(np.array(list(map(self.tokenizer,f.readlines()))).flatten())
            else:
                return len(f.readlines())
