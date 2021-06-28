import json
import requests
from format import format_response
from config_mailchimp import *


def lookup_interest_categories():
    url = "{}/interest-categories/?offset=0&count=100".format(get_list_url())
    response = requests.get(url, auth=get_credentials())
    return format_response(response)

def lookup_interests():
    url = "{}/interest-categories/62e9b40054/interests/?offset=0&count=100".format(get_list_url())
    response = requests.get(url, auth=get_credentials())
    json = format_response(response)
    return json

