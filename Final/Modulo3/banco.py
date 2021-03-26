#Ejercicio 01
mastercard= [51, 52, 53, 54 , 55]
american_expres = [34,37]
visa = [4]
def luhn(ccn):
    c = [int(x) for x in ccn[::-2]]
    u2 = [(2*int(y))//10+(2*int(y))%10 for y in ccn[-2::-2]]
    print(f"numero = {ccn}")
    return sum(c+u2)%10 == 0
    
prueba = 49927398716  #con este numero funciona
prueba2=549273989816  #no valida la funcion por eso arroja not found apesar de que inicia con 54
numero = input("Ingrese numero: ")
#Test
if luhn(numero) == True : 
    dig = numero[0] + numero[1]
    dig = int(dig)

    if (dig == 34 or dig == 37):
        print("American express")
    elif (dig == 51 or dig== 52 or dig == 53 or dig==54 or dig == 55):
        print("Mastercard")
    elif int(numero[0]) == 4 :
        print("Visa")
else:
    print("Not found")
