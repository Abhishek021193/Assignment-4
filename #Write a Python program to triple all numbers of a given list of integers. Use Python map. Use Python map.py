#Write a Python program to triple all numbers of a given list of integers. Use Python map.

given_list = [1, 2, 3, 4, 5, 6, 7]
print ("our list is : ",given_list)
result = map (lambda x : x + x + x , given_list)
print ("Triple of list numbers are :")
print (list(result))