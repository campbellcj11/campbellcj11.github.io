import csv
import json

data = {}
# json_data = json.dumps(data)

with open('../USNALinkedInDataScott.csv') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         if row["SimpleLocation"] not in data:
             data.update({row["SimpleLocation"] : {row["Industry"] : 1}})
         else:
             stateData = data[row["SimpleLocation"]]
             if row["Industry"] in data[row["SimpleLocation"]]:
                 data[row["SimpleLocation"]][row["Industry"]] += 1
             else:
                # if the industry is not in state - add industry and set to one
                data[row["SimpleLocation"]][row["Industry"]] = 1

json_data = json.dumps(data)
print(json_data)
