import json
import csv
from csv import DictWriter
import datetime

field_names = ['Time', 'Temperature', 'Flame', 'Fire']

def fireHere(temp, flame):
    if float(temp) >= 40 and int(flame) == 1:
        return True
    return False

callMeBack = '{"Temperature": "38.671875",  "flameDetected": "1"}'

json_object = json.loads(callMeBack)
fire = fireHere(json_object["Temperature"], json_object["flameDetected"])
now = str(datetime.datetime.now())

List = [now, json_object["Temperature"], json_object["flameDetected"], fire]
Dict = {'Time': now, 'Temperature':json_object["Temperature"], 'Flame':json_object["flameDetected"], 'Fire':fire}

with open('data.csv', 'a+') as f_object:    
    dictwriter_object = DictWriter(f_object, fieldnames=field_names, lineterminator='\n')
    dictwriter_object.writerow(Dict)
    f_object.close()

print("Done :)")
