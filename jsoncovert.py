import pandas as pd
import json
import openpyxl
import os

if __name__ == '__main__':
    jstojson =open(r"/Users/administrator/PycharmProjects/pythonProject1/follower.js")
    print(jstojson)
    jsonfile = json.load(jstojson)
    jsonfile = pd.read_json(r"/Users/administrator/PycharmProjects/pythonProject1/follower.js")
    jsonfile.to_csv(r"/Users/administrator/PycharmProjects/pythonProject1/follower.csv")
