import json
import random

def generate():
    current=random.uniform(0.05,0.2)
    voltage=random.uniform(4.08,4.80)
    energy=current*voltage
    new_data={
        "current":current,
        "voltage":voltage,
        "power":energy,
    }
    with open("weekly.json",'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["details"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)