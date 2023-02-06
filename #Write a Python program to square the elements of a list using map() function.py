#Write a Python program to square the elements of a list using map() function.

given_list=[4, 5, 2, 9]
print ("given list is :",given_list)
result = map (lambda x : x*x , given_list)
print ("Square the elements of the list are : ",list (result))