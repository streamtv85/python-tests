import json

salaries = '{"Alfred" : 300, "Jane" : 400 }'

decoded_salaries = json.loads(salaries)
print decoded_salaries["Alfred"]
print decoded_salaries["Jane"]
# print decoded_salaries["Me"]
print "hello world!"


