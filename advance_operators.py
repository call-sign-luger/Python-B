'''
IDENTITY OPERATOR:

-> Used to compare the memory locations of two objects
- 'is'
- 'is not'


* is will return true when two variables are pointing to the same object 
* is not will return true when the two variables are pointing to different objects

'''

l1=[1,2,3]
l2=[1,2,3]
l3=l1
print(l1 is l3)