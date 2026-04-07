students = [("Ali", ["Fizika", "Matematika"]), ("Laylo", ["Ingliz tili"]), ("Jasur", ["Matematika", "Informatika"])]

choosen = ()

count = 0
for name, subject in students:
    if "Matematika" in subject:
        count += 1

print(f"{count} talaba matematikani tanlagan")
