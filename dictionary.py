# Dictionary is a data-type which is a collection of key:value pairs

'''
Syntax:
    var_name={key1:value1, key2:value2}
'''

### STEP 1: Initialize a dictionary
menu={} #empty

### STEP 2: Add elements in the dictionary
menu["Coffee"] = 40
menu["Tea"] = 55

### STEP 3: Remove an element from dictionary
# del menu["Coffee"]
# print(menu)

### STEP 4: How to access key
menu["Espresso"] = 120
# price=menu["Espresso"]
# print(price)

### STEP 5: How to update
menu["Espresso"]=200
price=menu["Espresso"]
print(price)

### STEP 6: HOW TO CLEAR A DICTIONARY
menu.clear()
print(menu)
