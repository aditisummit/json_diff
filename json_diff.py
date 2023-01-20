
import json
import jsondiff as jd
from jsondiff import diff
# Opening JSON file
with open(r'spread_template_business(1).json') as f1:
  data1 = json.load(f1)

with open(r'spread_template_business(2).json') as f2:
  data2 = json.load(f2)
 
    # Print the type of data variable
print("Type1:", type(data1), "Type2:",type(data2))
print("-------------------------------------------------------------------------------------")



#obtain diff
jdiff= diff(data1,data2)
print (jdiff)


print("-------------------------------------------------------------------------------------")

print("Type:", type(jdiff))
print("#####################################################################")
with open(r'data.json') as data:
  data = json.load(data)
#obtain diff
jdiff2= diff(data2,data)
print (jdiff2)
