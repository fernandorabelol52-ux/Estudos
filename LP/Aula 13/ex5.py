string1 = input("Insira a primeira string: ")
string2 = input("Insira a segunda string: ")
string3 = ""

for letra in string1: 
    if letra not in string2:
        string3 += letra

print(f"A terceira string ficará: {string3}")