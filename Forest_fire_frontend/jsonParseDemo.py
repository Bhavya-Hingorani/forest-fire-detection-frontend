import json

callMeBack = '{\n  "Temperature": "38.671875",  "flameDetected": "1"\n}'
json_object = json.loads(callMeBack)

print(json_object["Temperature"])
