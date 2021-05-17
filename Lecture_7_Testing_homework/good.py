"""
NHTSA has a public api; the url we will be working with is
https://vpic.nhtsa.dot.gov/api/vehicles/getallmanufacturers?format=json&page=1
This api endpoint returns JSON; it has the field 'Results' - a list of car manufacturers with details.
We want to create a dictionary with country as a key, and list of manufacturer names as a value, e.g:
{
    'USA': ['Tesla', 'Ford', ...],
    'Japan': ['Honda', 'Subaru', ...]
}
Use 'Mfr_Name' as a manufacturer name.
If 'Country' is empty - skip it. We should traverse through all pages of this api endpoint
bad.py has a finished implementation of this task. Your goal is to make this code better, in any
way you can think of. Put your solution in good.py
Some examples of what can be done:
- you can create your own iterator/generator to go through pages for you
- insertion of items into dictionary can be improved
Also, add more tests to the test_dict.py to check response content.
"""
from typing import Dict, List
from collections import defaultdict

import requests
import logging

logging.basicConfig(level=logging.INFO)


class create_one_page_dict_iter(object):
    def __init__(self, url):
        self.url = url
        self.page = 1
        self.country_manufacturers = defaultdict(set)

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        make_dict = requests.get(f"{self.url}&page={self.page}").json()

        if not make_dict["Count"] or make_dict["Count"] == 0 or self.page > 3:
            raise StopIteration()

        for manufacturer in make_dict["Results"]:
            self.country_manufacturers[manufacturer["Country"]].add(manufacturer["Mfr_Name"])

        logging.info(f"Done with page {self.page}")
        self.page += 1
        return self.country_manufacturers


def create_country_make_dict(url: str) -> Dict[str, set]:
    country_manufacturers = defaultdict(set)

    for item in create_one_page_dict_iter(url):
        merge_dicts(country_manufacturers, item)

    return country_manufacturers


def merge_dicts(dict1, dict2):
    for a, b in dict2.items():
        for b_item in b:
            dict1[a].add(b_item)
