import requests
from format import format_response
from config_mailchimp import *


def create_campaign(segment_id):
    data = {
        "type": "regular",
        "recipients": {
            "list_id": get_list_id(),
            "segment_opts": {
                "saved_segment_id": segment_id
            }
        },
        "settings": {
            "subject_line": "Subject",
            "preview_text": "Small amount of text",
            "from_name": "The sender",
            "reply_to": "sender@donotreply.com",
            "to_name": "Recipient",
            "template_id": get_custom_email_template()
        }
    }

    url = get_campaign_url()
    response = requests.post(url, auth=get_credentials(), json=data)

    return format_response(response)


def set_email_content(campaign_id):
    text = """*|FNAME|*,<br>
This should replace *|FNAME|* with the member's first name"""

    data = {
        "template": {
            "id": get_custom_email_template(),
            "sections": {
                "body": text
            }
        }
    }

    url = "{}/{}/content".format(get_campaign_url(), campaign_id);
    response = requests.put(url, auth=get_credentials(), json=data)

    return format_response(response)


def send_email(campaign_id):
    url = "{}/{}/actions/send".format(get_campaign_url(), campaign_id)
    response = requests.post(url, auth=get_credentials())

    return format_response(response)
