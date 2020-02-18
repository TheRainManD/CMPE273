'''
from collections import defaultdict

classes = {"class_id": {"class_name": {"student_id": "student_name"}}}
c_id = 22
c_name = "CMPE"
classes.update({c_id: c_name})  
# Adding elements one at a time  
#classes[c_id][c_name].update({'Bob': '22'})
classes[c_id][c_name] = {'Bob': '22'}
#Dict['Dict1'].update({'Aob': '55'})

print("\nAfter adding dictionary Dict1") 
print(classes)
'''


Dict = { } 
print("Initial nested dictionary:-") 
print(Dict) 
  
Dict['dict1'] = {}
Dict['dict1']['name'] = {}
print(Dict) 
dict1 = 'dict1'
name = 'name'
# Adding elements one at a time  
Dict[dict1][name].update({'Bob': '22'})
Dict[dict1][name].update({'Aob': '22'})
print("\nAfter adding dictionary Dict1") 
print(Dict)
  
