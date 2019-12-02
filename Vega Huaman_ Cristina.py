#ejercicio 01
#Declarar
Usuario,clave="",""
Usuario=str(input("Usuario:"))
clave=str(input("clave"))
#processing
if (Usuario=="cristina")and(clave=="1234"):
  print("Acceso correcto")
#fin_if

#ejercicio 02
#declarar
trabajador,renumeracion_mensual,numero_de_meses="",0.0,0
trabajador=str (input("ingrese nombre del trabajador:"))
renumeracion_mensual=float(input("ingrese renumeracion mensual:"))
numero_de_meses=int(input("ingrese numero de meses:"))
#PROCESSING
M=renumeracion_mensual*numero_de_meses
if (M>30):
    print("tiene reunmeracion anual")
#fin_if

#ejercicio 03
#declarar
cliente,producto,cantidad,costo_de_unidad="","",0,0.0
cliente=str(input("ingrese nombre del cliente:"))
producto=str(input(input("ingrese nomnre del  producto: ")))
cantidad=int(input("ingrese cantidad: "))
costo_de_unidad=float(input("ingrese el costo de unidad:"))
#PROCESING
T=cantidad*costo_de_unidad
comprador_impulsivo=T>250
if (comprador_impulsivo):
    print("comprador impulsivo")
else:
    print("no es comprador impulsivo")

#ejercicio 04
#empleado="
#unidad_producida=0
#costo_por_trabajo=0.0
#Declarar
empleado,unidad_producida,costo_por_trabajo="",0,0.
empleado=str(input("ingrese nombre del empleado:"))
unidad_producida=int(input("ingrese unidad producida:"))
costo_por_trabajo=float(input("ingrese el costo por trabajo:"))

#PROCESSING
M=unidad_producida*costo_por_trabajo
if (M>40):
    print("calidad de trabajo")
#fin_if

#ejercicio 05
#Declarar
trabajador,renumeracion_neta_anual,tasa="",0.0,0.0
trabajador=str(input("ingrese nombre del trabajador:"))
renumeracion_neta_anual=float(input("ingrese renumeracion neta anual:"))
tasa=float(input("ingrese tasa "))

#PROCESSING
T=renumeracion_neta_anual*tasa
if (T>20):
    print("inpuesto mensual")
#fin_if

#ejercicio 06
#Declarar
producto,costo_de_producto,descuento="",0.0,0.0
producto=str(input("ingrese el nombre del producto:"))
costo_de_producto=float(input("ingrese costo de producto:"))
descuento=float(input("ingrese descuento"))
#PROCESING
total=costo_de_producto*descuento
if (total>10):
    print("descuento")
#fin_if

#ejercicio 07
#Declarar
cantidad_de_rubios,total_de_alumnos=0,0.0
cantidad_de_rubios=int(input("ingrese la cantidad de rubios:"))
total_de_alumnos=int(input("ingrese el total de alumnos:"))

#PROCESSING
porcentaje=(cantidad_de_rubios*100)/total_de_alumnos
if (porcentaje>6.5):
    print("alumnos rubios")
#fin_if

#ejercicio 08
#Declarar
precio,iva=0.0,0.0
precio=float(input("ingrese el precio:"))
iva=float(input("ingrese iva:"))

#PROCESING
pago_total_de_iva=precio*iva
if (pago_total_de_iva>36):
    print("iva")
#fin_if

#ejercicio 09
#Declarar
precio_sin_iva,total=0.0,0.0
precio_sin_iva=float(input("ingrese el precio sin iva:"))
total=float(input("ingrese total:"))

#PROCESING
total_iva=total-precio_sin_iva
if (total>5.6):
    print("iva incluido")
#fin_if

#ejercicio 10
#Declarar
valor_en_libro1,valor_en_libro2=0.0,0.0
valor_en_libro1=float(input("ingrese el valor del libro 1:"))
valor_en_libro2=float(input("ingrese el valor del libro 2:"))

#PROCESING
total=valor_en_libro1+valor_en_libro2
if (total<87):
    print("calidad del libro")

#fin_if

#ejercicio 11
#Declarar
total_danza_carnavalesca,total_danza_de_tijera=0,0
total_danza_carnavalesca=int(input("ingrese el total danza carnavalesca:"))
total_danza_de_tijera=int(input("ingrese el total danza de tijera:"))
#PROCESING
total_de_participacion=total_danza_carnavalesca+total_danza_de_tijera
if (total_de_participacion<40):
    print("participacion folklorica")
#fin_if

#ejercicio 12
#Declarar
edad=0
edad=int(input("ingresar edad:"))
#Procesing
#es mayor de edad=(edad>18)
if (edad > 18):
    print("Es mayor de edad")
#fin_if

#ejercicio13
#Declarar
compra=0.0
compra=float(input("ingrese cantidad de compra:"))
#processing
#pago en efectivo=(compra<100)
if (compra<100):
    print("pago en efectivo")
#fin_if

#ejercicio 14
nota1=0
nota2=0
nota3=0
nota1=int(input("ingrese la nota1:"))
nota2=int(input("ingrese la nota2:"))
nota3=int(input("ingrese la nota3:"))

#Procesing
promedio=(nota1+ nota2 + nota3) /3
if (promedio<10):
    print("reprobo el curso")
#fin_if

#ejercicio 15
#Declarar
Altura=0
Altura=float(input("ingrese su altura:"))
#Procesing
persona_de_altura_baja=(Altura<50)
if (Altura<50):
    print("persona de altura baja")
#fin_if

#ejercicio 16
#Declarar
valor=0
valor=int(input("ingrese valor:"))
#Procesing
el_valor_Es_negativo=(valor<0)
if (valor<0):
    print("el valor es negativo")
else:
    print("el valor es positivo")

#ejercicio 17
#Declarar
resultado=0
resultado=int(input("cuanto es 20+34:"))
#Procesing
if (resultado==54):
    print("respuesta correcta.felicitaciones!/n")
#fin_if

#ejercicio 18
#Declarar
sueldo=0.0
sueldo=float(input("ingrese el sueldo:"))
#procesing
esta_persona_debe_abonar_impuestos=(sueldo>200)
if (sueldo>200):
    print("esta persona debe abonar impuestos")
#fin_if


#ejercicio 19
#Declarar
sueldo=0.0
sueldo=float(input("ingrese el sueldo:"))
#procesing
esta_persona_debe_abonar_impuestos=sueldo*32
if (esta_persona_debe_abonar_impuestos>20):
    print("usted debe de abonar:",esta_persona_debe_abonar_impuestos)
#fin_if


#ejercicio 20
#Declarar
numero1=0
numero2=0
numero1=int(input("ingrese el numero 1:"))
numero2=int(input("ingrese el numero 2:"))
#procesing
if(numero1>numero2):
    print("numero1")
else:
    print("numero 2")


#ejercicio 21
#Declarar
edad1=0
edad2=0
edad1=int(input("ingrese el edad1:"))
edad2=int(input("ingrese el edad2:"))
#procesing
el_es_mayor=(edad1>edad2)
if(edad1>edad2):
    print("el es mayor")
#fin_if

#ejercicio 22
#Declarar
cuenta=0.0
Acumula=0
cuenta=float(input("ingrese cuenta:"))
Acumula=float(input("ingrese el acumulado:"))
#Procesing
promedio=cuenta/Acumula
if (promedio>13.0):
    print("tiene buen promedio")
#fin_if


#ejercicio 23
#Declarar
Dias=0
Dias=int(input("ingrese el numero de dias:"))
#Procesing
total=(Dias>365)
if (Dias>365):
    print("exceso de dias",Dias)
#fin_if

#ejercicio 24
#Declarar
meses=0
meses=int(input("ingrese el numero de meses:"))
#Procesing
total=(meses>12)
if (meses>12):
    print("exceso de meses",meses)
#fin_if


#ejercicio 25
#Declarar
velocidad_Constantes=0.0
tiempo=0.0
velocidad_Constantes=float(input("ingrese la velocidad constante:"))
tiempo=float(input("ingrese el tiempo:"))
#Procesing
distancia_recorrida=velocidad_Constantes*tiempo
if(distancia_recorrida>23):
    print("es buena")
else:
    print("es mala")

#ejercicio 26
#Declarar
numero=0
numero=int(input("ingrese un numero:"))
#procesing
N=(numero>20)
if(numero>20):
    print("el N es mayor")
#fin_if


#ejercicio 27
#Declarar
precio_tarifa=0.0
precio_final=0.0
precio_tarifa=float(input("ingrese el precio tarifa:"))
precio_final=float(input("ingrese el precion final:"))
#Procesing
Dto=(1-precio_final/precio_tarifa)*100
if(Dto>30):
    print("gano un descuento")
#fin_if

#ejercicio 28
#Declarar
numero_de_caja=0
numero_de_caja=int(input("ingrese el numero de caja:"))
#Procesing
total=numero_de_caja+5
if(total>10):
    print("mayor numero de caja")
else:
    print("menor numero de caja")

#ejercicio 29
#Declarar
cantidad_De_empleados=0
cantidad_de_horas=0
cantidad_De_empleados=int(input("ingrese la cantidad de empleados:"))
cantidad_de_horas=int(input("ingrese la cantidad de horas:"))
#Procesing
salario=cantidad_de_horas*cantidad_De_empleados
if (salario<40):
    print("bajo salario")
else:
    print("mayor salario")

#ejercicio 30
#Declarar
nombre,especie="",""
nombre=str(input("nombre:"))
especie=str(input("especie:"))
#processing
if (nombre=="oso panda")and(especie=="mamifero"):
  print("Dato Correcto")
#fin_if

#ejercicio 31
#Declarar
mascota,nombre="",""
nombre=str(input("nombre:"))
mascota=str(input("mascota:"))
#processing
if (nombre=="Doki")and(mascota=="perro"):
  print("Doki es un perro")
#fin_if


#ejercicio 32
#Declarar
cantidad_de_gatos=0
cantidad_de_gatos=int(input("ingrese la cantidad de gatos:"))
#processing
total=(cantidad_de_gatos>40)
if(cantidad_de_gatos>40):
    print("le gusta los gatos")
else:
    print("no le gusta los gatos")


#ejercicio 33
#Declarar
carrera_profesional=""
numero_de_estudiante=0
carrera_profesional=str(input("ingrese la carrera profesional:"))
numero_de_estudiante=int(input("ingrese el numero de estudiantes"))
#Procesing
Aula=(numero_de_estudiante<30)
if(numero_de_estudiante<30):
    print("Acceso ok")
#fin_if

#ejercicio 34
#Declarar
animal=""
animal=str(input("ingrese animal:"))
#processing
if (animal=="doki"):
  print("Gua,Gua")
#fin_if

#ejercicio 35
#Declarar
nombre=""
sueldo=0.0
nombre=str(input("ingrese nombre:"))
sueldo=float(input("ingrese sueldo:"))
#procesing
bono=sueldo*23
if(bono>89):
    print("buen bono")
#fin_if

#ejercicio 36
#Declarar
nombre=""
nombre=str(input("nombre:"))
#processing
if (nombre=="martillo"):
  print("objeto estatico")
else:
    print("objeto no estatico")
#fin_if


#ejercicio 37
#Declarar
numero_de_llantas=0
numero_de_llantas=int(input("ingrese el numero de llantas:"))

#Procesing
valor_en_llanatss=700*numero_de_llantas
if(valor_en_llanatss>5):
    print("el valor de las llanta es:",numero_de_llantas)
#fin_if

#ejercicio 38
#Declarar
total_De_compra=0
total_De_compra=int(input("ingrese el total de compra:"))
#procesing
dinero_Descontando=total_De_compra*34/100
if(dinero_Descontando>59):
    print("el dinero descontando es:",dinero_Descontando)
#fin_if

#ejercicio 39
#Declarar
total_De_ventas=0
total_De_ventas=int(input("ingrese el total de ventas:"))
#procesing
Descuento=total_De_compra*40/100
if(Descuento>59):
    print("el descuento es:",Descuento)
#fin_if

#ejercicio 40
#Declarar
numero_de_camisas=0
numero_de_camisas=int(input("ingrese el numero de camisas:"))

#Procesing
costo=700*numero_de_camisas
if(costo>500):
    print("el numero de camisas:",numero_de_camisas)
else:
    print("el numero de camisas:",costo)

#ejercicio 41
#Declarar
pago_cine=0.0
pago_cancha=0.0
pago_cine=float(input("ingrese el pago del cine:"))
pago_cancha=float(input(("ingrese el pago de la cancha:")))

#Procesing
costo=pago_cine+pago_cancha
if(costo<20):
    print("el costo es:",costo)
#fin_if


#ejercicio 42
#Declarar
pago_menu=0.0
pago_menu=float(input(("pago del menu:")))

#Procesing
servicio=(pago_menu>8)
if(pago_menu>8):
    print("excelente servicio")
#fin_if

#ejercicio 43
#Declarar
costo_tomate=0.0
costo_cebolla=0.0
costo_tomate=float(input("ingrese el costo de toamte:"))
costo_cebolla=float(input("ingrese el costo de cebola:"))

#Procesing
total=costo_tomate+costo_cebolla
if(total<20):
    print("esta barato")
else:
    print("esta caro")


#ejercicio 44
#Declarar
costo_tomate=0.0
costo_cebolla=0.0
costo_tomate=float(input("ingrese el costo de toamte:"))
costo_cebolla=float(input("ingrese el costo de cebola:"))

#Procesing
total=costo_tomate+costo_cebolla
if(total<36):
    print("pago total:",total)
#fin_if


#ejercicio 45
#Declarar
pago_cine=0.0
pago_cancha=0.0
pago_cine=float(input("ingrese el pago del cine:"))
pago_cancha=float(input(("ingrese el pago de la cancha:")))

#Procesing
costo=pago_cine+pago_cancha
if(costo<20):
    print("excelente servicio")
#fin_if


#ejercicio 46
#Declarar
altura=0.0
altura=float(input("ingrese la altura:"))
#procesing
pulgada=altura/2.54
if(pulgada>4):
    print("la altura en pulgada es:",pulgada)
#fin_if

#ejrcicio 47
#Declarar
pulgada=0.0
pulgada=float(input("ingrese pulgadas:"))
#procesing
pies=pulgada/12
if(pies>6):
    print("la altura en pies es:",pies)
#fin_if

#ejercicio 48
#Declarar
numero=0
numero=int(input("ingrese el numero:"))
#Procesing
x=(numero>0)
if(numero>0):
    print("el numero tiene signo positivo")
else:
    print("el numeor tiene sigo negativo")


#ejercicio 49
#Declarar
numero1=0
numero2=0
numero1=int(input("ingrese el numero 1"))
numero2=int(input("ingrese el numero 2:"))

#Procesing
resultado=numero1+numero2
if(resultado>0):
    print("el resultado es:",resultado)

#ejercicio 50
#Declarar
numero1=0
numero2=0
numero1=int(input("ingrese el numero 1:"))
numero2=int(input("ingrese el numero 2:"))

#Procesing
resultado=numero1+numero2
if(resultado>1000):
    print("indeterminado")
else:
    print("infinito")



