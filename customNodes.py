import openpyxl
from collections import OrderedDict
import json
import random
wb = openpyxl.load_workbook('../Dataset#4-HumanResources/USNA LinkedIn Data Scott.xlsx')
wsData = wb['LinkedIn USNA']
wsLocation = wb['Location']

# Dictionary to hold lists
nodesAndLinks = {}
nodesAndLinks['nodes'] = []
nodesAndLinks['links'] = []

# Add some titles
nodesAndLinks['type'] = "NetworkGraph"
nodesAndLinks['label'] = "Beyond The Uniform Visualization"

# Get Simple Location into Dictionary
locations = {}
counter = 0
for row in wsLocation.rows:
    if (counter >= 2):
        locations[row[0].value] = row[1].value
    counter += 1

# 0 - empty, 1 - empty, 2- warefare_spec, 3-Year service, 4- Name, 5- headline, 6- position, 7- industry, 8- location
#     9- current Companies, 10 -current company links, 11- previous companies, 12- previous companies links, 13- education
#     14 - connection Degree, 15- connections, 16 - Email, 17-Email (researched), 18 - twitter handles, 19 - websites,
#     20 - Last company website, 21 - Profile link, 22- Profile image link, 23 - Simple Location
counter = 0
numberOfElements = 0
for row in wsData.rows:
    if (counter == 100): #temporary
        break
    if (counter == 0 or counter == 1 or counter == 2):
        pass
    else:
        data = {
            #'Warefare Specialty' : row[2].value,
            'id' : numberOfElements,
            'properties' : {
              'Name' : row[4].value,
              'Years Service' : row[3].value,
              'Industry' : row[7].value,
              'Location' : locations[row[8].value]
            },
            'Years Service' : row[3].value,
            'Name' : row[4].value,
            'Industry' : row[7].value,
            'Location' : locations[row[8].value],
        }
        nodesAndLinks['nodes'].append(data)
        numberOfElements += 1
    counter +=1

print("Number of elements: " + str(numberOfElements))

# Location -
counter = 0
count = 0
for firstIndex, node in enumerate(nodesAndLinks['nodes']):
    for otherNode in nodesAndLinks['nodes'][firstIndex + 1:]:
        value = 0
        # if (node['Location'] == otherNode['Location']):
        #     value += 1
        # if (node['Industry'] == otherNode['Industry']):
        #     value += 1
        if (abs(int(node['Years Service']) - int(otherNode['Years Service'])) <= 0):
            value += 1
        if (value is not 0):
            count += 1
            linkData = {
                'source' : node['id'],
                'target' : otherNode['id'],
                'cost' : value
            }
            nodesAndLinks['links'].append(linkData)

print(count)

#Write to file
json_data = json.dumps(nodesAndLinks, indent=2)
with open('yearsOfService.json', 'w') as f:
    f.write(json_data)
