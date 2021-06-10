"""
Write a function that merges integer from sorted files and returns an iterator
file1.txt:
1
3
5
file2.txt:
2
4
6
# list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
Add tests for this function.
"""
import logging
from typing import Iterator, List, Union


def merge_sorted_files(file_list: List[str]) -> Iterator:
    files_text = []
    for i in range(len(file_list)):
        with open(file_list[i]) as file:
            files_text.append(file.readlines())

    for i in range(get_longest_list_size(files_text)):
        for j in range(len(file_list)):
            if len(files_text[j]) > i:
                yield int(files_text[j][i])


def get_longest_list_size(lists: list) -> int:
    return max(map(lambda x: len(x), lists))


def test_two_files_positive():
    assert list(merge_sorted_files(["files/file1.txt", "files/file2.txt"])) == [1, 2, 3, 4, 5, 6]


def test_two_files_different_size():
    assert list(merge_sorted_files(["files/file1.txt", "files/file4.txt"])) == [1, 2, 3, 3, 5]


def test_two_files_different_size_revert_order():
    assert list(merge_sorted_files(["files/file4.txt", "files/file1.txt"])) == [2, 1, 3, 3, 5]
