#Ejercicio 1
n = int(input("Ingrese un numero: "))
for i in range(1, n+1):
    print("  "*(n-i) + "# "*(i))

#Ejercicio 2
mover = int(input("Ingrese cuantas posiciones se debe mover: "))
text = input("ingrese texto: ")
text = text.upper()
encryption = ""

for c in text:

    if c.isupper():

        c_unicode = ord(c)

        c_index = ord(c) - ord("A")
        new_index = (c_index + mover) % 26
        new_unicode = new_index + ord("A")

        new_character = chr(new_unicode)
        encryption = encryption + new_character

    else:
        encryption += c
        
print("texto:",text)

print("Texto encriptado:",encryption)