import json
from collections import Counter

filename = "output/fhir/Jody426_Haley279_f09a432b-ccb3-0771-23a4-715390c10e53.json"
with open(filename, 'r') as f:
    str1=f.read()

data=json.loads(str1)

vals = {}                       # A dictonary to store how often each value occurs.
for i in data.values():
  for j in set(i):              # Convert to a set to remove duplicates
    vals[j] = 1 + vals.get(j,0) # If we've seen this value iterate the count
                                # Otherwise we get the default of 0 and iterate it
print(vals)