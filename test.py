from segment import *
import json

json_response = create_segment()
# json_response = delete_segment(3682186)
print(json.dumps(json_response, indent=2))
