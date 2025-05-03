import time
import winsound as sound

# Generar un bucle for dentro del while
# a=int(input("Ingrese un numero: "))
# while a<10:
#     for i in range(1,11,2):
#         a=a+i #a la variable a se le suma i. También se puede poner como a+=i
#         print(a)
# print("Fin del bucle")

""""""""
a=int(input("Ingrese un numero: "))
while a<10:
    a=a+1
    time.sleep(0.5)
    sound.Beep(frequency=800, duration=100) 
    print(a)
    # print (a, end=(" ")) #si uno pone un espacio entre comillas, se imprime un espacio entre cada número
    # print (a, end=("\t")) #si uno pone un tabulador entre comillas, se imprime un tabulador entre cada número
while a>0:
    a=a-1
    time.sleep(0.5)
    sound.Beep(frequency=800, duration=100) 
    print(a)
    # print(a, end=(" "))
print("\nFinalizo el ciclo while")


        
        
        

