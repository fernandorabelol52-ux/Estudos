string1 = input("Insira a primeira string: ")
string2 = input("Insira a segunda string: ")
comuns = ""

for letra in string1:
    if letra in string2 and letra not in comuns:
        comuns += letra
print(f"Caracteres em comum: {comuns}")

