import hashlib
import requests
from format import format_response
from config_mailchimp import *


def hash_email(email: str):
    md5str = hashlib.md5(email.encode('utf-8')).hexdigest()
    return md5str


def lookup_email(email: str):
    email_hash = hash_email(email)

    url = "{}/members/{}".format(get_list_url(), email_hash)
    response = requests.get(url, auth=get_credentials())

    return format_response(response)

