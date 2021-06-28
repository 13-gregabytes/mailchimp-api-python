import json
import requests
from format import format_response
from config_mailchimp import *


def lookup_segments():
    url = "{}/segments/?offset=0&count=100".format(get_list_url())
    response = requests.get(url, auth=get_credentials())

    return format_response(response)


def create_segment():
    url = "{}/segments".format(get_list_url())
    data = json.loads('{"name":"random_name","static_segment":["email@addr.ess"]}')
    response = requests.post(url, auth=get_credentials(), json=data)

    return format_response(response)


def delete_segment(segment_id):
    url = "{}/segments/{}".format(get_list_url(), segment_id)
    response = requests.delete(url, auth=get_credentials())

    return format_response(response)

