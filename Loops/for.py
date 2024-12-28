'''
for loop 3 fundamentals

1- start
2- stop
3- step/operation

for i in range(start,stop,step):
    statement
'''

# for i in range(1,10,2):
#     print(i)

m=int(input("Enter a number to start: "))
n=int(input("Enter a number to end: "))
z=n-1
for i in range(m,z,-1):
    print(i)