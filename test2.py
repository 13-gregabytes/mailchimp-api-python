import json
import base64

print(json.loads('{}"responseBody":"{}"{}'.format("{", base64.b64encode("ABCxyz".encode('utf-8')).decode('utf-8'), "}")))
