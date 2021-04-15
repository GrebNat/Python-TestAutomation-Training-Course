# Using functional approach, generators, currying,
# implement functions that writes IP list of redirected requests (code 304) into another file
# separate pure_func from functions that change state (io_func)
# write negative test "test_myfunc_negative"
# Set pytest as default runner https://stackoverflow.com/questions/6397063/how-do-i-configure-pycharm-to-run-py-test-tests
# hit Ctrl+Shift+F10 or RMB on the file to run tests

import re


def io_func(logfile_path, result_file_path):
    with open(logfile_path, 'r') as file_r:
        data = file_r.readlines()
        with open(result_file_path, 'a') as file_w:
            for line in data:
                pf = pure_func(line)
                if pf is not None:
                    file_w.write(pf+"\n")
    pass


def test_write_file():
    io_func("apache_log", "result")


def pure_func(file_line):
    p = re.compile(
        '(([0-9]{1,3}\.){3}[0-9]{1,3})(.-.-.)(\[[0-9\/A-Za-z:]* \+0000\]) ("[A-Z]{3,5} .*[ ]*HTTP\/1\.[0-1]") ([0-9]{3}) (.*)')
    m = p.match(file_line)
    if m is None:
        return None
    if m.group(6) == '304':
        return m.group(1)
    return None


def test_myfunc_positive():
    line = '218.30.103.62 - - [17/May/2015:11:05:17 +0000] "GET /projects/xdotool/xdotool.xhtml \
    HTTP/1.1" 304 - "-" "Sogou web spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)"'
    assert pure_func(line) == "218.30.103.62"


def test_myfunc_negative():
    line = '218.30.103.62 - - [17/May/2015:11:05:17 +0000] "GET /projects/xdotool/xdotool.xhtml \
       HTTP/1.1" 200 - "-" "Sogou web spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)"'
    assert pure_func(line) is None
