#wap to enter marks of 3 subjects and store them in dict.
#start with empty dictionary and add one by one.Use subject
#name as key and marks as value
dict={}
m1=input("marks for chem ")
m2=input("marks for phy ")
m3=input("marks for maths ")
dict.update({"chem: ":m1})
dict.update({"phy: ":m2})
dict.update({"maths: ":m3})
print(dict)

