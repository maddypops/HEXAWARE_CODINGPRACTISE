
import json

try:
    with open(r"C:\HEXAWARE\HEXAWARE-CODINGPRACTISE\ex.json",'r') as file:
        data = json.load(file)
except FileNotFoundError:
    print("The file was not found.")
except json.JSONDecodeError:
    print("Invalid JSON format.")

