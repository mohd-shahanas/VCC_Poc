import time
import os

from dynaconf import settings as conf


def vcc_click(element, text):
    element.click()
    print(text + " Clicked")
    time.sleep(5)


def get_table_contents(table_element):
    table_rows = table_element.find_elements_by_tag_name("tr")
    data = {}

    for row in table_rows:
        key = row.find_element_by_tag_name("th").text.strip()
        value = row.find_element_by_tag_name("td").text.strip()
        data[key] = value

    return data


def validate_file_exists(filename, folder=conf.DOWNLOAD_FOLDER):
    assert os.path.exists(os.path.join(folder,filename)) == True


def add_info_message(actual, expected, keyword=''):
    """Add more information to the assertion message in case of a failure."""
    return '(Actual) Response is {}, (Expected) Should {} be {}'.format(actual, keyword, expected)


def verify_object_equal(actual, expected):
    assert actual == expected, add_info_message(actual, expected)


def verify_object_not_equal(actual, expected):
    assert actual != expected, add_info_message(actual, expected, keyword="not")