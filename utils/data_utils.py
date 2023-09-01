import calendar
import random
import string
import time
import yaml


def generate_timestamp():
    return str(calendar.timegm(time.gmtime()))


def generate_string_data(length):
    return str(''.join(random.choices(string.ascii_lowercase + string.digits, k=length)))


def fetch_endpoints():
    with open(f'./yaml/endpoints.yaml') as file_read:
        file = yaml.load(file_read, Loader=yaml.FullLoader)
    return file['endpoints']
