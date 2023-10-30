import json
from googletrans import Translator

translator = Translator()

# add this to the LANGUAGES dictionary in site-packages/googletrans/constants.py 
#  'dv': 'dhivehi',

def translate(text, src, dest):
  return translator.translate(text, src=src, dest=dest)

# Read data from json file
with open('Promise.json', encoding="utf-8") as json_file:
    data = json.load(json_file)

for chapter in data:
    # print(chapter["Title_Dhiv"])
    chapter["Title_Eng"] = translate(chapter["Title_Dhiv"], "dv", "en").text
    for promise in chapter["Promise"]:
        if promise["Dhiv"] != "":
          promise["Eng"] = translate(promise["Dhiv"], "dv", "en").text

# Write data to json file
with open('Promise-translated.json', 'w', encoding="utf-8") as outfile:
    json.dump(data, outfile, indent=2, ensure_ascii=False)