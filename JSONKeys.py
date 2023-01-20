import json
from collections import Counter

filename = "output/fhir/Jody426_Haley279_f09a432b-ccb3-0771-23a4-715390c10e53.json"
with open(filename, 'r') as f:
    str1=f.read()

data=json.loads(str1)

c = Counter(k[:] for d in data for k, v in d.items() if k.startswith('resourceType'))
#c now has the count. Below it will check if count is 0 or not and print.
if c['resourceType']>0:
    print("There are",c['resourceType'],"failed cases")
else:
    print("test case passed sucessfully")