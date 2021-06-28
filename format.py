import json
import requests
import base64


def format_response(response):
    return_json = json.loads("{}")

    if response is not None:
        if response.text:
            try:
                return_json = response.json()
            except ValueError:
                try:
                    return_json = json.loads('{}"responseBody":"{}"{}'.format("{", response.text, "}"))
                except ValueError:
                    return_json = json.loads('{}"Base64":"{}"{}'.format("{", base64.b64encode(response.text.encode('utf-8')).decode('utf-8'), "}"))
        else:
            return_json = json.loads('{}"statusCode":"{}"{}'.format("{", str(response.status_code), "}"))

    return return_json
