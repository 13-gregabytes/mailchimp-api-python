import requests
from format import format_response
from config_mailchimp import *


def get_folder():
    url = get_folder_url()
    response = requests.get(url, auth=get_credentials())

    return format_response(response)

