string1 = input("Insira a primeira string: ")
string2 = input("Insira a segunda string: ")
string3 = ""

for letra in string1:
    if letra not in string2 and letra not in string3:
        string3 += letra
for letra in string2:
    if letra not in string1 and letra not in string3:
        string3 += letra

print(f"As terceira string será: {string3}")

    
