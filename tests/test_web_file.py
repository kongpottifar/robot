from robot import web_file
from pytest import raises
from os import path, remove
from requests.exceptions import HTTPError


def test_web_file():
    test_url = "https://gist.githubusercontent.com/kongpottifar/4145ce86303d82916997b2ad3ea54320/raw/499df95ca8515780dfbc1f609e9d8b7edb97c73e/B.txt" 
    test_file= "test_file.txt"

    if path.isfile(test_file):
        remove(test_file)
    wf = web_file(test_file, test_url, [])
    try:
        assert wf.needs_build()
        wf.run()
        assert path.isfile(test_file)
    finally:
        if path.isfile(test_file):
            remove(test_file)


def test_web_file_error():
    test_url = "https://kongpottifar.github.io/404"
    test_file= "test_file.txt"
    wf = web_file(test_file, test_url, [])
    try:
        with raises(HTTPError):
            wf.run()
    finally:
        if path.isfile(test_file):
            remove(test_file)
    
