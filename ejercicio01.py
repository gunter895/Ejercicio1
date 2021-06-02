def primo():
    print("Serán primos??")
    numero = int(input("Introduzca un número: "))
    if numero <=1:
        print("Introduzca un número que sea mayor que 1 ")
    else:
        contador = 0
        for i in range(1, numero + 1):
            if numero % i == 0:
                contador = contador + 1
                if contador == 2:
                    print("{numero} es primo ")
                else:
                    print("{numero} no es primo ")   
    primos = open('primos.txt', 'w')
    primos.write(str(numero))
print(primo())


