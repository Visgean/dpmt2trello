import os
import requests


LIST_URL = 'https://dpmt.inf.ed.ac.uk/api/v1/tenant/ug4/projects'
DETAIL_URL = "https://dpmt.inf.ed.ac.uk/api/v1/tenant/ug4/projects/{pid}"


# parse cookie file:
if not os.path.exists('./cookie.txt'):
    raise FileNotFoundError('Please create a cookie file in the current directory as per instructions')


cookies = {}
with open('cookie.txt') as f:
    for l in f.read().splitlines():
        for cookie in l.split(';'):
            name, val = cookie.split('=')
            cookies[name.strip()] = val



def get_project_list():
    api_response = requests.get(LIST_URL, cookies=cookies)
    api_response.raise_for_status()
    return api_response.json()


def get_project_detail(pid):
    url = DETAIL_URL.format(pid=pid)
    api_response = requests.get(url, cookies=cookies)
    api_response.raise_for_status()
    return api_response.json(), url
