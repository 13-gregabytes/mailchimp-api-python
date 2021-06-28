import requests
from format import format_response
from config_mailchimp import *


def lookup_templates():
    url = get_template_url()
    response = requests.get(url, auth=get_credentials(), params={'count':100})

    return format_response(response)
