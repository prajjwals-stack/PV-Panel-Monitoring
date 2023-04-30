import json
import random
import datetime

def generate():
    date=datetime.date(2023, 4, 1)
    for i in range(0,30):
        current=random.uniform(0.05,0.2)
        voltage=random.uniform(4.08,4.80)
        energy=current*voltage
        new_data={
            "date":str(date),
            "current":current,
            "voltage":voltage,
            "power":energy,
        }
        with open("daily.json",'r+') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            # Join new_data with file_data inside emp_details
            file_data["details"].append(new_data)
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent = 4)
        date+=datetime.timedelta(days=1)