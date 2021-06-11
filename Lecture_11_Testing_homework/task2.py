import re
import requests

url = "http://stackoverflow.com/"
pattern = '<a href="[^ ]*"'
session = requests.Session()
response_html = session.get(url).text
found_links = re.findall(pattern, response_html)


def map1(opt):
    return None if opt is None else opt.group(0)


after_search = map(lambda x: map1(re.search('(https|http):\/\/[a-zA-Z\.0-9]*', x)), found_links)
after_filter = filter(lambda x: x is not None, after_search)
after_replace = set(map(lambda x: str(x).replace("https://", ""), after_filter))
after_sorted = sorted(after_replace)

print(*after_sorted, sep="\n")
