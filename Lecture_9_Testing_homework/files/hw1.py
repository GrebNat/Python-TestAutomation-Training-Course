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
from typing import Iterator, List, Union


def merge_sorted_files(file_list: List[str]) -> Iterator:
    files_text = []
    for i in range(len(file_list)):
        with open(file_list[i]) as file:
            files_text.append(file.readlines())

    for i in range(len(files_text[0])):
        for j in range(len(file_list)):
            yield int(files_text[j][i])


def test_two_files_positive():
    assert list(merge_sorted_files(["file1.txt", "file2.txt"])) == [1, 2, 3, 4, 5, 6]
