people = [("Ali", 24), ("Laylo", 30), ("Jasur", 19)]

max_age = 0
max_person = ("")

for name, age in people:
    if age > max_age:
        max_age = age
        max_person = name

print(f"{max_person} -  {max_age}")