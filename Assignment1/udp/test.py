#dictionary
'''
Dict = { } 
print("Initial nested dictionary:-") 
print(Dict) 
  
Dict['Dict1'] = {}
Dict['Dict2'] = {}
print(Dict)
  
# Adding elements one at a time  
Dict['Dict1']['name'] = 'Bob'
Dict['Dict1']['age'] = 21
print("\nAfter adding dictionary Dict1") 
print(Dict) 
'''

#split
'''
message = "Rain"
seq = 11
delimiters = "|:|"
data = (str(seq) + delimiters + message)
print(data)
split_test = data.split(delimiters)
print(split_test)
seq2 = data.split(delimiters)[0]
print(seq2)
'''


#read text file line by line
'''
file_1 = open("upload.txt","r")
while True:
    data = file_1.readline()
    print(data)
    if not data:
        break
file_1.close()
'''
lst_dict = [{"name": "Rain", "sid": 1}, {"name": "Wind", "sid": 2}]
#print(lst_dict[1])
data = next(item["name"] for item in lst_dict if item["sid"] == 1)
print(data)


print("Data: ", data)

