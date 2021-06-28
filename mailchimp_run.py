import json
from member import *
from segment import *
from template import *
from campaign import *

email = 'some@email.ooo'

json_response = lookup_email(email)
print('------------------------------------------')
print('Lookup Email')
print(json.dumps(json_response, indent=2))
print('------------------------------------------')

if "id" not in json_response:
    print("{} not found in mailchimp".format(email))
    print(json.dumps(json_response, indent=2))
else:
    json_response = create_segment()
    print('------------------------------------------')
    print('Create Segment')
    print(json.dumps(json_response, indent=2))
    print('------------------------------------------')

    if "id" not in json_response:
        print("Error creating segment for {}".format(email))
        print(json.dumps(json_response, indent=2))
    else:
        segment_id = json_response['id']

        # json_response = lookup_templates()
        # print(json.dumps(json_response, indent=2))

        json_response = create_campaign(segment_id)
        print('------------------------------------------')
        print('Create Campaign')
        print(json.dumps(json_response, indent=2))
        print('------------------------------------------')

        if "id" not in json_response:
            print("Error creating campaign for {}".format(email))
            print(json.dumps(json_response, indent=2))
        else:
            campaign_id = json_response['id']

            json_response = set_email_content(campaign_id)
            print('------------------------------------------')
            print('Update Campaing')
            print(json.dumps(json_response, indent=2))
            print('------------------------------------------')

            json_response = send_email(campaign_id)
            print('------------------------------------------')
            print('Send Campaign')
            print(json.dumps(json_response, indent=2))
            print('------------------------------------------')

            # json_response = delete_segment(segment_id)
            # print(json.dumps(json_response, indent=2))
