# Array 
users = ["AJI","REZA","AJAT","IMAM","MAYA"]
# add users items

# users.append("New Users")
users.insert(0,"first user")

# remove array 
users.pop()
print(users)


# otomatic generate array
alot_zero = [0] * 20
print(alot_zero)

# Unpacking array 
items = ['laptops' , 'phone' , 'joystick']
laptop = items[0]
print(laptop)

# distratring variabel array 
laptops , *other = items
print(laptops)
print(other)