### 1\.E/S de datos:

## a) 
#print("Esto funciona de maravilla")

## b)  
#dato = input("Ingrese un dato: ")
#print(f"El dato ingresado es: {dato}")

## c) 
#nombre = input("Ingrese su nombre: ")
#edad = input("Ingrese su edad: ")
#print(f"Usted se llama {nombre} y tiene {edad} años.")

## d) Suma de dos números enteros 
#numero_uno = int(input("Ingrese el primer número: "))
#numero_dos = int(input("Ingrese el segundo número: "))
#suma = numero_uno + numero_dos
#print(f"La suma es {suma}")

## e) Resto u operador módulo entre dividendo y divisor 
#numero_uno = int(input("Ingrese el dividendo: "))
#numero_dos = int(input("Ingrese el divisor: "))
#resto = numero_uno % numero_dos
#print(f"El resto es {resto}")

## f) Importe con incremento del 10% 
#importe = float(input("Ingrese el importe: "))
#diez_porciento = importe * 0.10
#importe_con_incremento = importe + diez_porciento
#print(f"Importe ingresado: {importe}")
#print(f"10% del importe: {diez_porciento}")
#print(f"Importe final con incremento: {importe_con_incremento}")

## g) Importe con descuento del 25% 
#importe = float(input("Ingrese el importe: "))
#veinticinco_porciento = importe * 0.25
#importe_con_descuento = importe - veinticinco_porciento
#print(f"Importe ingresado: {importe}")
#print(f"25% del importe: {veinticinco_porciento}")
#print(f"Importe final con descuento: {importe_con_descuento}")

#### 2\. Estructuras de Control Condicionales (if / elif/ else)

## a) Verificación de año particular (Pac-Man) 
#anio = int(input("Ingrese un año: "))
#if anio == 1980:
#    print("Este año se creó el videojuego Pac-Man")

## b)  
#edad = int(input("Ingrese su edad: "))
#if edad >= 18:
#    print("Es mayor de edad")

## c) 
#edad = int(input("Ingrese su edad: "))
#if edad >= 18:
#    print("Es mayor de edad")
#else:
#    print("Es menor de edad")

## d)  
#edad = int(input("Ingrese su edad: "))
#if edad > 13 and edad <=17:
#    print("Es adolescente")

## e)
#edad = int(input("Ingrese su edad: "))
#if edad < 13 and edad >18:
#    print("No es adolescente")

## f)
#edad = int(input("Ingrese su edad: "))
#if edad < 13 and edad >0 :
#    print("Es menor")
#elif edad > 13 and edad <=17:
#    print("Es adolescente")
#else: 
#    print("Es mayor de")

### 2\. Estructuras de Control Condicionales (Match)
#a)
#mes = input("Ingrese un mes: ").strip().capitalize()
#match mes:
#    case "Enero":
#        print("Que comiences bien el año!")
#    case "Marzo":
#        print("A clases!")
#    case "Julio":
#        print("Se vienen las vacaciones!")
#    case "Diciembre":
#        print("Felices fiestas!")

## b)
#mes = input("Ingrese un mes: ").strip().capitalize()
#match mes:
#    case "Julio" | "Agosto":
#        print("Abrigate que hace frio.")
#    case "Enero" | "Febrero" | "Marzo" | "Abril" | "Mayo" | "Junio":
#        print("Falta para el invierno.")
#    case "Septiembre" | "Octubre" | "Noviembre" | "Diciembre":
#        print("Ya pasamos el frio, ahora calor!")
#    case _:
#        print("Mes ingresado no válido.")

## c)
#mes = input("Ingrese un mes: ")
#match mes:
#    case "Febrero":
#        print("Este mes no tiene más de 29 días.")
#    case _:
#        print("Este mes tiene 30 o más días.")

##d)
#mes = input("Ingrese un mes: ")
#match mes:
#    case "Febrero":
#        print("Tiene 28 días.")
#    case "Abril" | "Junio" | "Septiembre" | "Noviembre":
#        print("Tiene 30 días.")
#    case "Enero" | "Marzo" | "Mayo" | "Julio" | "Agosto" | "Octubre" | "Diciembre":
#        print("Tiene 31 días.")
#    case _:
#        print("Mes no válido.")

##e)
#hora = int(input("Ingrese una hora del día: "))
#match hora:
#    case 7 | 8 | 9 | 10 | 11:
#        print("Es de mañana.")

##f)
#hora = int(input("Ingrese una hora del día (0 a 23): "))
#match hora:
#    case 7 | 8 | 9 | 10 | 11:
#        print("Es de mañana.")
#    case 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19:
#        print("Es de tarde.")
#    case 20 | 21 | 22 | 23 | 0 | 1 | 2 | 3 | 4 | 5 | 6:
#        print("Es de noche.")
#    case _:
#        print("La hora no existe.")

##g)
#numero_uno = int(input("Ingrese el primer número: "))
#numero_dos = int(input("Ingrese el segundo número: "))
#opcion = input("Seleccione una opción (Sumar / Restar / Multiplicar / Dividir): ")
#
#match opcion:
#    case "Sumar":
#        print(f"La suma es {numero_uno + numero_dos}")
#    case "Restar":
#        print(f"La resta es {numero_uno - numero_dos}")
#    case "Multiplicar":
#        print(f"La multiplicación es {numero_uno * numero_dos}")
#    case "Dividir":
#        if numero_dos != 0:
#            print(f"La división es {numero_uno / numero_dos}")
#        else:
#            print("Error: No es posible dividir entre cero.")
#    case _:
#        print("Opción no válida.")


#### 3\. Estructuras de Control Repetitivas (for)

## a) Secuencia ascendente de 1 a 10 
#for i in range(1, 11):
#    print(i)

## b) Secuencia descendente de 10 a 1 
#for i in range(10, 0, -1):
#    print(i)

## c) 
#n = int(input("Ingrese cantidad de repeticiones: "))
#for i in range(n):
#    print("Hola UTN FRA")

## d) 
#n = int(input("Ingrese un número: "))
#for i in range(1, n + 1):
#    if i % 2 == 0:
#        print(i)

## e) 
#n = int(input("Ingrese número límite: "))
#for i in range(1, n + 1):
#    if i % 2 != 0:
#        print(i)

## f) 
#numero = int(input("Ingrese un número mayor a 0: "))
#while numero > 0:
#    numero = int(input("Ingrese un número mayor a 0: "))

### 4\. Estructuras de Control Repetitivas (while)

## a) 
#i = 1
#while i <= 10:
#    print(i)
#    i+= 1

## b) 
#i = 10
#while i >= 1:
#    print(i)
#    i-= 1
#
## c) 
#numero= int (input ("Ingrese un número entre 0 y 9: "))
#print (numero)
#while numero > 9 or numero < 0:
#    numero = int(input("No es correcto, por favor, ingrese un número entre 0 y 9: "))
#    print(numero)

## d)
#genero = input("Ingrese género (F/M): ")
#while genero != "F" and genero != "M"and genero != "m" and genero != "f":
#        genero = input("No es correcto, ingrese género (F/M): ")
#      
#if genero == "F" or genero == "f":
#        print("FEMENINO")
#else:
#        print("MASCULINO")
 
## e) 
#print ("Debe ingresar 5 números positivos")
#suma = 0
#i = 0
#while i < 5:
#    numero = float(input(f"Ingrese un número: "))
#    suma += numero
#    i += 1
#promedio = suma / 5
#print(f"Suma de los 5 números: {suma}")
#print(f"Promedio de los 5 números: {promedio}")

## f) 
#i = 0
#suma = 0
#entrada = input("Ingrese un número (o escriba 'fin' para terminar): ")
#while entrada != 'fin':
#    suma += float(entrada)
#    entrada = input("Ingrese un número (o escriba 'fin' para terminar): ")
#    i += 1
#
#if i > 1:
#    print(f"Suma total: {suma}")
#    print(f"Promedio: {suma / i}")
#else:
#    print("No se registraron ingresos.")

## g) 
suma_positivos = 0
producto_negativos = 1
hay_negativo = False
entrada = input("Ingrese un número (o escriba 'fin' para terminar): ")

while entrada != 'fin':
    num = float(entrada)
    if num > 0:
        suma_positivos += num
    elif num < 0:
        producto_negativos *= num
        hay_negativo = True
    entrada = input("Ingrese un número (o escriba 'fin' para salir): ")
    
if suma_positivos > 0: 
    print(f"Suma de números positivos: {suma_positivos}")
if hay_negativo:
    print(f"Multiplicación de números negativos: {producto_negativos}")
