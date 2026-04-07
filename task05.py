numbers = (3, 6, 7, 8, 10, 11)

juft_sonlar = ()

for num in numbers: 
    if num % 2 == 0:
        juft_sonlar = juft_sonlar + (num,)

print(juft_sonlar)