# import json

# employee = '{"id":"09", "name":"Nitin", "department":"finance"}'

# employee_dict = json.loads(employee)
# # print(employee_dict)
# # print(type(employee_dict))
# # print("\n")


# json_object = json.dumps(employee_dict, indent=4)
# print(json_object)
# print(type(json_object))

import time;  # This is required to include time module.

ticks = time.time()
print ("Number of ticks since 12:00am, January 1, 1970:", ticks)


localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)