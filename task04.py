orders = [(102, "Ali"), (99, "Vali"), (150, "Sami")]

juft_sonlari = ()

for num, name in orders:
    if num % 2 == 0:
        juft_sonlari += ((num, name),)

print(juft_sonlari)