# print("hola mundo")

# input() entreda de datos 
# int() para convertir cadena en entero

# x = float(input("ingrese dato Uno: ")) # convierte los numeros en string 
# #print(x)
# y = float(input("ingrese dato Dos: ")) # convierte los numeros en string

# print(x+y)

# a = int(input("ingrese dato Uno: ")) # convierte los numeros en entero 
#print(x)
# b = int(input("ingrese dato Dos: ")) # convierte los numeros en entero
# sacar la potencia es con doble **
# suma +
# resta -
# multi *
# divi /
# potencia **
# modulo %

# boleanos
# a = True
# b = False
# print(a)
# print(b)

# # potencia 
# print(10**2)

# # modulo
# print(10%2)

# if elif else

# a = 5

# if a < 4:
#     print("hola")
#     print("mundo")
# elif a<5:
#     print("es menor que 5")
# else:
#     print("No es menor")

# # print("curso")

# condicionales 
# a = 3
# b = 4

# if a == 3 or b == 4:
#     print("es correcto")


# //// while
# a = 7
# while a == 7:
#     print("estoy en el while")
#     a = int(input("ingrese el nuevo valor de a:  "))
#     if a != 7:
#         break


# metodo for

# for i in range(0,5):
#     print(i)
    
num1 = int(input("ingrese numero Uno"))
num2 = int(input("ingrese numero Dos"))

while True:
    option = input(" escoja la opreación S = suma / R = resta / M = multiplicar / D = division")
    if option == 'S':
        print(num1+num2)
    elif option == 'R':
        print(num1-num2)
    elif option == 'M':
        print(num1*num2)
    elif option == 'D':
        print(num1/num2)
    else:
        print("ingrese un dato correcto")