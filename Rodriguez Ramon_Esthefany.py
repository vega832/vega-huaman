#EJERCICIO_01
cliente,producto_1,producto_2,cant_1,cant_2,costo_uni_1,costo_uni_2="","","",0,0,0.0,0.0
cliente=str(input("cliente:"))
producto_1=str(input("producto 1:"))
producto_2=str(input("producto 2:"))
cant_1=str(input("cantidad 1:"))
cant_2=str(input("cantidad 2:"))
costo_uni_1=float(input("cosoto unitario 1:"))
costo_uni_2=float(input("costo unitario 2:"))

# PROCESSING
total=cant_1*costo_uni_1+cant_2*costo_uni_2
calidad_de_algodon=(total > 180)
if(calidad_de_algodon):
    print("Calidad de algodon")
#fin_if


#EJERCICIO_02
cliente,producto_1,producto_2,producto_3,cant_1,cant_2,cant_3,costo_uni_1,costo_uni_2,costo_uni_3="","","","",0,0,0,0.0,0.0,0.0
cliente=str(input("cliente:"))
producto_1=str(input("producto 1:"))
producto_2=str(input("producto 2:"))
producto_3=str(input("producto 3:"))
cant_1=str(input("cantidad 1:"))
cant_2=str(input("cantidad 2:"))
cant_3=str(input("cantidad 3:"))
costo_uni_1=float(input("costo unitario 1:"))
costo_uni_2=float(input("costo unitario 2:"))
costo_uni_3=float(input("cosoto unitario 3:"))

# PROCESSING
total=cant_1*costo_uni_1+cant_2*costo_uni_2+cant_3*costo_uni_3
marca=(total > 250)
if(marca):
    print("Marca")
#fin_if


#EJERCICIO_03
nombre_del_alumno,nota_1,nota_2,nota_3="",0,0,0
nombre_del_alumno=str(input("nombre del alumno:"))
nota_1=str(input("nota 1:"))
nota_2=str(input("nota 2:"))
nota_3=str(input("nota 3:"))

# PROCESSING
promedio=(nota_1+nota_2+nota_3)/3
nota_aprobatoria=(promedio > 11)
if(nota_aprobatoria):
    print("Nota aprobatoria")
#fin_if


#EJERCICIO_04
cliente,cantidad_de_libros,visita_por_semana="",0,0
cliente=str(input("cliente:"))
cantidad_de_libros=str(input("cantidad de libros:"))
visita_por_semana=str(input("visita por semana:"))

# PROCESSING
total_de_visita=cantidad_de_libros*visita_por_semana
visita_compulsiva_a_una_libreria=(total_de_visita > 20)
if(visita_compulsiva_a_una_libreria):
    print("Visita compulsiva a una libreria")
#fin_if


#EJERCICIO_05
usuario,red_social_1,red_social_2,red_social_3,cant_de_hora_diarias_1,cant_de_hora_diarias_2,cant_de_hora_diarias_3="","","","",0,0,0
usuario=str(input("usuario:"))
red_social_1=str(input("red social 1:"))
red_social_2=str(input("red social 2:"))
red_social_3=str(input("red social 3:"))
cant_de_hora_diarias_1=str(input("cantidad de hora diarias 1:"))
cant_de_hora_diarias_2=str(input("cantidad de hora diarias 2:"))
cant_de_hora_diarias_3=str(input("cantidad de hora diarias 3"))

# PROCESSING
total_de_horas_por_dia=cant_de_hora_diarias_1+cant_de_hora_diarias_2+cant_de_hora_diarias_3
adiccion_de_las_redes_sociales=(total_de_horas_por_dia > 15)
if(adiccion_de_las_redes_sociales):
    print("Adiccion de las redes sociales")
#fin_if


#EJERCICIO_06
nombre,deporte1,deporte2,deporte3,cant_de_hora_diarias_1,cant_de_hora_diarias_2,cant_de_hora_diarias_3="","","","",0,0,0
nombre=str(input("nombre:"))
deporte1=str(input("deporte 1:"))
deporte2=str(input("deporte 2:"))
deporte3=str(input("deporte 3:"))
cant_de_hora_diarias_1=str(input("cantidad de hora diarias 1:"))
cant_de_hora_diarias_2=str(input("cantidad de hora diarias 2:"))
cant_de_hora_diarias_3=str(input("cantidad de hora diarias 3:"))

# PROCESSING
total_de_horas_por_dia=cant_de_hora_diarias_1+cant_de_hora_diarias_2+cant_de_hora_diarias_3
gusto_por_el_deporte=(total_de_horas_por_dia > 6 )
if(gusto_por_el_deporte):
    print("Gusto por el deporte")
#fin_if


#EJERCICIO_07
paciente,medicamento_1,medicamento_2,cant_de_medicamento1_por_dia,cant_de_medicamento2_por_dia="","","",0,0
paciente=str(input("paciente:"))
medicamento_1=str(input("medicamento 1:"))
medicamento_2=str(input("medicamento 2:"))
cant_de_medicamento1_por_dia=str(input("cantidad de medicamento 1 por dia:"))
cant_de_medicamento2_por_dia=str(input("cantidad de medicamento 2 por dia:"))

# PROCESSING
total_de_medicamentos_por_semana=cant_de_medicamento1_por_dia*7+cant_de_medicamento2_por_dia*7
automedicacion=(total_de_medicamentos_por_semana > 20 )
if(automedicacion):
    print("Automedicacion")
#fin_if


#EJERCICIO_08
alumno,horas_dedicadas_al_estudio_por_dia="",0
alumno=str(input("alumno:"))
horas_dedicadas_al_estudio_por_dia=str(input("horas dedicadas al estudio por dia:"))

# PROCESSING
total_de_horas_por_semana=horas_dedicadas_al_estudio_por_dia*7
bajo_rendimiento_academico=(total_de_horas_por_semana < 35)
if(bajo_rendimiento_academico):
    print("Bajo rendimiento academico")
#fin_if


#EJERCICIO_09
cliente,producto1,producto2,cant_de_producto1,cant_de_producto2,cost_uni1,cost_uni2="","","",0,0,0.0,0.0
cliente=str(input("cliente:"))
producto1=str(input("producto 1:"))
producto2=str(input("producto 2:"))
cant_de_producto1=str(input("cantidad de producto 1:"))
cant_de_producto2=str(input("cantidad de producto 2:"))
cost_uni1=float(input("costo unitario 1:"))
cost_uni2=float(input("costo unitario 2:"))

# PROCESSING
total=cant_de_producto1*cost_uni1+cant_de_producto2*cost_uni2
comprador_compulsivo=(total < 260)
if(comprador_compulsivo):
    print("Comprador compulsivo")
#fin_if


#EJERCICIO_10
cliente,producto_1,producto_2,cant_de_producto_1,cant_de_producto_2,cost_uni_1,cost_uni_2="","","",0,0,0.0,0.0,
cliente=str(input("cliente:"))
producto_1=str(input("producto 1:"))
producto_2=str(input("producto 2:"))
cant_de_producto_1=str(input("cantidad de producto 1:"))
cant_de_producto_2=str(input("cantidad de producto 2:"))
cost_uni_1=float(input("costo unitario 1:"))
cost_uni_2=float(input("costo unitario 2:"))

# PROCESSING
total=cant_de_producto_1*cost_uni_1+cant_de_producto2*costo_uni_2
comprador_pasivo=(total > 15)
if(comprador_pasivo):
    print("Comprador pasivo")
#fin_if


#EJERCICIO_11
empleado,nro_dias,costo_por_dia,horas_extra="",0,0.0,0
empleado=str(input("empleado:"))
nro_dias=str(input("numero dias:"))
costo_por_dia=float(input("costo por dia:"))
horas_extra=str(input("horas extras:"))

# PROCESSING
monto=(nro_dias*costo_por_dia)+(horas_extra*8)
sueldo_mensual=(total > 800 )
if(sueldo_mensual):
    print("Sueldo mensual")
#fin_if


#EJERCICIO_12
cliente,producto_1,producto_2,producto_3,costo_uni_1,costo_uni_2,costo_uni_3,cant_de_producto_1,cant_de_producto_2,cant_de_producto_3="","","","",0.0,0.0,0.0,0,0,0
cliente=str(input("cliente:"))
producto_1=str(input("producto 1:"))
producto_2=str(input("producto 2:"))
producto_3=str(input("producto 3:"))
costo_uni_1=float(input("costo unitario 1:"))
costo_uni_2=float(input("costo unitario 2:"))
costo_uni_3=float(input("costo unitario 3:"))
cant_de_producto_1=str(input("cantidad de producto 1:"))
cant_de_producto_2=str(input("cantidad de producto 2:"))
cant_de_producto_3=str(input("cantidad de producto 3:"))

# PROCESSING
total=(costo_uni_1*cant_de_producto1)+(costo_uni_2*cant_de_producto_2)+(costo_uni_3*cant_de_producto_3)
lista_de_compras=(total > 30 )
if(lista_de_compras):
    print("Lista de compras")
#fin_if


#EJERCICIO_13
alumno,nota_1,nota_2,nota_3,="",0,0,0
alumno=str(input("alumno:"))
nota_1=str(input("nota 1:"))
nota_2=str(input("nota 2:"))
nota_3=str(input("nota 3:"))

# PROCESSING
total=(nota_1+nota_2+nota_3)/3
alumno_desaprobado=(total < 10 )
if(alumno_desaprobado):
    print("Alumno desaprobado")
#fin_if


#EJERCICIO_14
cliente,producto_1,producto_2,producto_3,costo_uni_1,costo_uni_2,costo_uni_3,cant_de_producto_1,cant_de_producto_2,cant_de_producto_3="","","","",0.0,0.0,0.0,0,0,0,0.0
cliente=str(input("cliente:"))
producto_1=str(input("producto 1:"))
producto_2=str(input("producto 2:"))
producto_3=str(input("producto 3:"))
costo_uni_1=float(input("cosot unitario 1:"))
costo_uni_2=float(input("costo unitario 2:"))
costo_uni_3=float(input("cosot unitario 3"))
cant_de_producto_1=str(input("cantidad de producto 1:"))
cant_de_producto_2=str(input("cantidad de producto 2:"))
cant_de_producto_3=str(input("cantidad de producto 3:"))

# PROCESSING
total=(costo_uni_1*cant_de_producto1)+(costo_uni_2*cant_de_producto_2)+(costo_uni_3*cant_de_producto_3)
gusto_por_golosinas=(total > 150 )
if(gusto_por_golosinas):
    print("Gusto por golosinas")
#fin_if


#EJERCICIO_15
paciente,medicamento_1,medicamento_2,medicamento_3,cant_de_medicamento_1_por_dia,cant_de_medicamento_2_por_dia,cant_de_medicamento_3_por_dia="","","","",0,0,0
paciente=str(input("paciente:"))
medicamento_1=str(input("medicamento 1:"))
medicamento_2=str(input("medicamento 2:"))
medicamento_3=str(input("medicamento 3:"))
cant_de_medicamento_1_por_dia=str(input("cantidad de medicamento 1 por dia:"))
cant_de_medicamento_2_por_dia=str(input("cantidad de medicamento 2 por dia:"))
cant_de_medicamento_3_por_dia=str(input("cantidad de medicamento 3 por dia:"))

# PROCESSING
total=cant_de_medicamento_1_por_dia+cant_de_medicamento_2_por_dia+cant_de_medicamento_3_por_dia
compra_excesiva_de_medicamento=(total > 50 )
if(compra_excesiva_de_medicamento):
    print("Compra excesiva de medicamentos")
#fin_if


#EJERCICIO_16
trabajador,horas_de_jornada_laboral_por_dia,dias_de_jornada_laboral="",0,0
trabajador=str(input("trabajador:"))
horas_de_jornada_laboral_por_dia=str(input("horas de jornada laboral por dia:"))
dias_de_jornada_laboral=str(input("dias de jornada laboral:"))

# PROCESSING
total=horas_de_jornada_laboral_por_dia*dias_de_jornada_laboral
incumplimiento_de_horas_de_trabajo=(total_de_horas_por_semana < 25 )
if(incumplimiento_de_horas_de_trabajo):
    print("Incumplimiento de horas de trabajo")
#fin_if


#EJERCICIO_17
nombre,horas_dedicadas_a_la_television_por_dia,horas_dedicadas_a_la_television_por_semana="",0,0
nombre=str(input("nombre:"))
horas_dedicadas_a_la_television_por_dia=str(input("horas dedicadas a la television por dia:"))
horas_dedicadas_a_la_television_por_semana=str(input("horas dedicadas a la television por semana:"))

# PROCESSING
total=horas_dedicadas_a_la_television_por_dia*horas_dedicadas_a_la_television_por_semana
ve_television_moderadamente=(total_de_horas_por_semana > 10 )
if(ve_television_moderadamente):
    print("Ve television moderadamente")
#fin_if


#EJERCICIO_18
nombre,numero_veces_al_dia_tomando_cafe,numero_veces_a_la_semana_tomando_cafe="",0,0
cliente=str(input("cliente:"))
numero_veces_al_dia_tomando_cafe=str(input("numero veces al dia tomando cafe:"))
numero_veces_a_la_semana_tomando_cafe=str(input("numero veces a la semana tomando cafe:"))

# PROCESSING
total=numero_veces_al_dia_tomando_cafe*numero_veces_a_la_semana_tomando_cafe
consumo_excesivo_de_cafe=(numero_veces_a_la_semana_tomando_cafe > 20 )
if(consumo_excesivo_de_cafe):
    print("Consumo excesivo de cafe")
#fin_if


#EJERCICIO_19
nombre,numero_viajes_a_la_semana,numero_viajes_al_mes="",0,0
nombre=str(input("nombre:"))
numero_viajes_a_la_semana=str(input("numero viajes a la semana:"))
numero_viajes_al_mes=str(input("numero viajes al mes:"))

# PROCESSING
total=numero_viajes_a_la_semana*numero_viajes_al_mes
gusta_viajar=(numero_viajes_al_mes > 15 )
if(gusta_viajar):
    print("Gusta viajar")
#fin_if


#EJERCICIO_20
cliente,numero_visitas_a_la_biblioteca_por_dia,numero_visitas_a_la_biblioteca_por_semana="",0,0
cliente=str(input("cliente:"))
numero_visitas_a_la_biblioteca_por_dia=str(input("numero visitas a la biblioteca por dia:"))
numero_visitas_a_la_biblioteca_por_semana=str(input("numero visitas a la biblioteca por semana:"))

# PROCESSING
total=numero_visitas_a_la_biblioteca_por_dia*numero_visitas_a_la_biblioteca_por_semana
disgusto_por_leer=(numero_visitas_a_la_biblioteca_por_semana < 2 )
if(disgusto_por_leer):
    print("Disgusto por la leer")
#fin_if


#EJERCICIO_21
nombre,fruta_1,fruta_2,cant_de_fruta_1_por_dia,cant_de_fruta_2_por_dia="","","",0,0
nombre=str(input("nombre:"))
fruta_1=str(input("fruta 1:"))
fruta_2=str(input("fruta 2:"))
cant_de_fruta_1_por_dia=str(input("cantidad de fruta 1 por dia:"))
cant_de_fruta_2_por_dia=str(input("cantidad de fruta 2 por dia:"))

# PROCESSING
total_de_fruta_por_semana=(cant_de_fruta_1_por_dia*7)+(cant_de_fruta_2_por_dia*7)
come_saludable=(total_de_fruta_por_semana > 25 )
if(come_saludable):
    print("Come saludable")
#fin_if


#EJERCICIO_22
nombre,horas_dedicadas_a_la_cocina_por_dia,horas_dedicadas_a_la_cocina_por_semana="",0,0
nombre=str(input("nombre:"))
horas_dedicadas_a_la_cocina_por_dia=str(input("horas dedicadas a la cocina por dia:"))
horas_dedicadas_a_la_cocina_por_semana=str(input("horas dedicadas a la cocina por semana:"))

# PROCESSING
total=horas_dedicadas_a_la_cocina_por_dia*horas_dedicadas_a_la_cocina_por_semana
disgusto_a_la_cocina=(total_de_horas_por_semana < 6 )
if(disgusto_a_la_cocina):
    print("Disgusto a la cocina")
#fin_if


#EJERCICIO_23
alumno,nota_01,nota_02,nota_03,nota_04="",0,0,0,0
alumno=str(input("alumno:"))
nota_01=str(input("nota 01:"))
nota_02=str(input("nota 02:"))
nota_03=str(input("nota 03:"))
nota_04=str(input("nota 04:"))

# PROCESSING
promedio=(nota_01+nota_02+nota_03+nota_04)/4
nota_aprobatoria_filosofia=(promedio > 14 )
if(nota_aprobatoria_filosofia):
    print("Nota aprobatoria filosofia")
#fin_if


#EJERCICIO_24
alumno,nota_01,nota_02,nota_03,nota_04="",0,0,0,0
alumno=str(input("alumno:"))
nota_01=str(input("nota 01:"))
nota_02=str(input("nota 02:"))
nota_03=str(input("nota 03:"))
nota_04=str(input("nota 04:"))

# PROCESSING
promedio=(nota_01+nota_02+nota_03+nota_04)/4
nota_aprobatoria_matematica=(promedio > 14 )
if(nota_aprobatoria_matematica):
    print("Nota aprobatoria matematica")
#fin_if



#EJERCICIO_25
nombre,horas_de_sueño_por_dia,horas_de_sueño_por_semana="",0,0
nombre=str(input("nombre:"))
horas_de_sueño_por_dia=str(input("horas de sueño por dia:"))
horas_de_sueño_por_semana=str(input("horas de sueño por semana:"))

# PROCESSING
total=horas_de_sueño_por_dia*horas_de_sueño_por_semana
sufre_imsomnio=(total_de_horas_por_semana < 50 )
if(sufre_imsomnio):
    print("Sufre imsomnio")
#fin_if


#EJERCICIO_26
paciente,cajetilla_1,cantidad_de_cigarros_por_dia="",0,0
paciente=str(input("paciente:"))
cajetilla_1=str(input("cajetilla 1:"))
cantidad_de_cigarros_por_dia=str(input("cantidad de cigarros por dia:"))

# PROCESSING
cantidad_de_cigarros_por_semana=(cantidad_de_cigarros_por_dia*cajetilla_1)
fumador_activo=(cantidad_de_cigarros_por_dia > 5 )
if(fumador_activo):
    print("Fumador activo")
#fin_if


#EJERCICIO_27
usuario,red_social_1,red_social_2,cant_de_hora_diarias_1,cant_de_hora_diaria_2="","","",0,0
usuario=str(input("usuario:"))
red_social_1=str(input("red social 1:"))
red_social_2=str(input("red social 2: "))
cant_de_hora_diarias_1=int(input("cantidad de horas diarias 1:"))
cant_de_hora_diarias_2=int(input("cantidad de horas diarias 2:"))

#PROCESSING
total_de_horas_por_dia=(cant_de_hora_diarias_1+cant_de_hora_diarias_2)
uso_moderado_de_redes_sociales=(total_de_horas_por_dia < 6 )
if(uso_moderado_de_redes_sociales):
    print("Uso moderado de redes sociales")
#fin_if


#EJERCICIO_28
nombre,horas_dedicadas_a_los_videojuegos_por_dia,horas_dedicadas_a_los_videojuegos_por_semana="",0,0
nombre=str(input("nombre:"))
horas_dedicadas_a_los_videojuegos_por_dia=str(input("horas dedicadas a los videojuegos por dia:"))
horas_dedicadas_a_los_videojuegos_por_semanaç=str(input("horas dedicadas a los videojuegos por semana:"))

# PROCESSING
total=horas_dedicadas_a_los_videojuegos_por_dia*horas_dedicadas_a_los_videojuegos_por_semana
adiccion_al_videojuego=(total_de_horas_por_semana > 30 )
if(adiccion_al_videojuego):
    print("Adiccion al videojuego")
#fin_if


#EJERCICIO_29
cliente,horas_viendo_peliculas_por_dia,horas_viendo_peliculas_por_semana="",0,0
cliente=str(input("cliente:"))
horas_viendo_peliculas_por_dia=str(input("horas viendo peliculas por dia:"))
horas_viendo_peliculas_por_semana=str(input("horas viendo peliculas por semana:"))

# PROCESSING
total=horas_viendo_peliculas_por_dia*horas_viendo_peliculas_por_semana
fanatico_del_cine=(total_de_horas_por_semana > 10 )
if(fanatico_del_cine):
    print("Fanatico del cine")
#fin_if


#EJERCICIO_30
alumna,horas_dedicadas_a_la_danza_por_dia,horas_dedicadas_a_la_danza_por_semana="",0,0
alumna=str(input("alumna:"))
horas_dedicadas_a_la_danza_por_dia=str(input("horas dedicadas a la danza por dia:"))
horas_dedicadas_a_la_danza_por_semana=str(input("horas dedicadas a la danza por semana:"))

# PROCESSING
total=horas_dedicadas_a_la_danza_por_dia*horas_dedicadas_a_la_danza_por_semana
inclinacion_por_la_danza=(total_de_horas_por_semana > 40 )
if(inclinacion_por_la_danza):
    print("Inclinacion por la danza")
#fin_if


#EJERCICIO_31
nombre,horas_dedicadas_a_la_musica_por_dia,horas_dedicadas_a_la_musica_por_semana="",0,0
nombre=str(input("nombre:"))
horas_dedicadas_a_la_musica_por_dia=str(input("horas dedicadas a la musica por dia:"))
horas_dedicadas_a_la_musica_por_semana=str(input("horas dedicadas a la musica por semana:"))

# PROCESSING
total=horas_dedicadas_a_la_musica_por_dia*horas_dedicadas_a_la_musica_por_semana
gusto_por_la_musica=(total_de_horas_por_semana > 40 )
if(gusto_por_la_musica):
    print("Gusto por la musica")
#fin_if


#EJERCICIO_32
empleado,horas_de_tardanza_al_trabajo_por_dia,horas_de_tardanza_al_trabajo_por_semana="",0,0
empleado=str(input("empleado:"))
horas_de_tardanza_al_trabajo_por_dia=str(input("horas de tardanza al trabajo por dia:"))
horas_de_tardanza_al_trabajo_por_semana=str(input("horas de tardanza al trabajo por semana:"))

# PROCESSING
total=horas_de_tardanza_al_trabajo_por_dia*horas_de_tardanza_al_trabajo_por_semana
desempleado=(total_de_horas_por_semana > 10 )
if(desempleado):
    print("Desempleado")
#fin_if


#EJERCICIO_33
nombre,carne_1,carne_2,cant_de_consumo_de_carne_1_por_dia,cant_de_consumo_de_carne_2_por_dia="","","",0,0
nombre=str(input("nombre:"))
carne_1=str(input("carne 1:"))
carne_2=str(input("carne 2:"))
cant_de_consumo_de_carne_1_por_dia=str(input("cantidad de consumo de carne 1 por dia:"))
cant_de_consumo_de_carne_2_por_dia=str(input("cantidad de consumo de carne 2 por dia:"))

# PROCESSING
total_de_consumo_de_carne_por_semana=(cant_de_consumo_de_carne_1_por_dia*7)+(cant_de_consumo_de_carne_2_por_dia*7)
gusto_por_la_carne=(total_de_consumo_de_carne_por_semana > 36 )
if(gusto_por_la_carne):
    print("Gusto por la carne")
#fin_if


#EJERCICIO_34
alumno,nota_01,nota_02,nota_03="",0,0,0
alumno=str(input("alumno:"))
nota_01=str(input("nota 01:"))
nota_02=str(input("nota 02:"))
nota_03=str(input("nota 03:"))

# PROCESSING
promedio=(nota_01+nota_02+nota_03)/3
nota_desaprobatoria_ingles=(promedio < 55 )
if(nota_desaprobatoria_ingles):
    print("Nota desaprobatoria ingles")
#fin_if


#EJERCICIO_35
alumno,nota_01,nota_02,nota_03="",0,0,0
alumno=str(input("alumno:"))
nota_01=str(input("nota 01:"))
nota_02=str(input("nota 02:"))
nota_03=str(input("nota 03:"))

# PROCESSING
promedio=(nota_01+nota_02+nota_03)/3
nota_aprobatoria_ingles=(promedio > 85 )
if(nota_aprobatoria_ingles):
    print("Nota aprobatoria ingles")
#fin_if


#EJERCICIO_36
nombre,horas_dedicadas_a_la_television_por_dia,horas_dedicadas_a_la_television_por_semana="",0,0
nombre=str(input("nombre:"))
horas_dedicadas_a_la_television_por_dia=str(input("horas dedicadas a la television por dia:"))
horas_dedicadas_a_la_television_por_semana=str(input("horas dedicadas a la television por semana:"))

# PROCESSING
total=horas_dedicadas_a_la_television_por_dia*horas_dedicadas_a_la_television_por_semana
gusto_a_la_television=(total_de_horas_por_semana > 9 )
if(gusto_a_la_television):
    print("Gusto a la television")
#fin_if


#EJERCICIO_37
alumno,nota_1,nota_2,nota_3,nota_4="",0,0,0,0
alumno=str(input("alumno:"))
nota_1=str(input("nota 1:"))
nota_2=str(input("nota 2:"))
nota_3=str(input("nota 3:"))
nota_4=str(input("nota4:"))

# PROCESSING
promedio=(nota_1+nota_2+nota_3+nota_4)/4
materia_aprobada=(promedio > 11)
if(materia_aprobada):
    print("Materia aprobada")
#fin_if


#EJERCICIO_38
alumna,nota_1,nota_2,nota_3,nota_4="",0,0,0,0
alumna=str(input("alumna:"))
nota_1=str(input("nota 1:"))
nota_2=str(input("nota 2:"))
nota_3=str(input("nota 3:"))
nota_4=str(input("nota4:"))

# PROCESSING
promedio=(nota_1+nota_2+nota_3+nota_4)/4
materia_desaprobada=(promedio < 10)
if(materia_desaprobada):
    print("Materia desaprobada")
#fin_if


#EJERCICIO_39
nombre,verdura1,verdura2,cant_de_verdura1_por_dia,cant_de_verdura2_por_dia="","","",0,0
nombre=str(input("nombre:"))
verdura1=str(input("verdura 1:"))
verdura2=str(input("verdura 2:"))
cant_de_verdura1_por_dia=str(input("cantidad de verdura 1 por dia:"))
cant_de_verdura2_por_dia=str(input("cantidad de verdura 2 por dia:"))

# PROCESSING
total_de_verdura_por_semana=(cant_de_verdura1_por_dia*7)+(cant_de_verdura2_por_dia*7)
alimentacion_saludable=(total_de_verdura_por_semana > 25 )
if(alimentacion_saludable):
    print("Alimentacion saludable")
#fin_if


#EJERCICIO_40
paciente,horas_en_hospital_por_dia,horas_en_hospital_por_semana="",0,0
paciente=str(input("pacinete:"))
horas_en_hospital_por_dia=str(input("horas en hospital por dia:"))
horas_en_hospital_por_semana=str(input("horas en hospital por semana:"))

# PROCESSING
total=horas_en_hospital_por_dia*horas_en_hospital_por_semana
orden_de_alta=(total_de_horas_por_semana > 20 )
if(orden_de_alta):
    print("Orden de alta")
#fin_if


#EJERCICIO_41
nombre_del_alumno,nota_1,nota_2,nota_3,nota_4="",0,0,0,0
nombre_del_alumno=str(input("nombre del alumno:"))
nota_1=str(input("nota 1:"))
nota_2=str(input("nota 2:"))
nota_3=str(input("nota 3:"))
nota_4=str(input("nota4:"))

# PROCESSING
promedio=(nota_1+nota_2+nota_3+nota_4)/4
alumno_regular=(promedio > 15)
if(alumno_regular):
    print("Alumno regular")
#fin_if


#EJERCICIO_42
nombre_del_alumno,nota_1,nota_2,nota_3,nota_4="",0,0,0,0
nombre_del_alumno=str(input("nombre del alumno:"))
nota_1=str(input("nota 1:"))
nota_2=str(input("nota 2:"))
nota_3=str(input("nota 3:"))
nota_4=str(input("nota4:"))

# PROCESSING
promedio=(nota_1+nota_2+nota_3+nota_4)/4
alumno_becado=(promedio > 18)
if(alumno_becado):
    print("Alumno becado")
#fin_if


#EJERCICIO_43
nombre,horas_dedicadas_a_la_musica_por_dia,horas_dedicadas_a_la_musica_por_semana="",0,0
nombre=str(input("nombre:"))
horas_dedicadas_a_la_musica_por_dia=str(input("horas dedicadas a la musica por dia:"))
horas_dedicadas_a_la_musica_por_semana=str(input("horas dedicadas a la musica por semana:"))

# PROCESSING
total=horas_dedicadas_a_la_musica_por_dia*horas_dedicadas_a_la_musica_por_semana
gusto_por_la_musica=(total_de_horas_por_semana > 30 )
if(gusto_por_la_musica):
    print("Gusto por la musica")
#fin_if


#EJERCICIO_44
nombre,horas_dedicadas_a_la_musica_por_dia,horas_dedicadas_a_la_musica_por_semana="",0,0
nombre=str(input("nombre:"))
horas_dedicadas_a_la_musica_por_dia=str(input("horas dedicadas a la musica por dia:"))
horas_dedicadas_a_la_musica_por_semana=str(input("horas dedicadas a la musica por semana:"))

# PROCESSING
total=horas_dedicadas_a_la_musica_por_dia*horas_dedicadas_a_la_musica_por_semana
disgusto_a_la_musica=(total_de_horas_por_semana < 8 )
if(disgusto_a_la_musica):
    print("Disgusto por la musica")
#fin_if


#EJERCICIO_45
cliente,horas_dedicadas_al_gimnasio_por_dia,horas_dedicadas_al_gimnasio_por_semana="",0,0
cliente=str(input("cliente:"))
horas_dedicadas_al_gimnasio_por_dia=str(input("horas dedicadas al gimnasio por dia:"))
horas_dedicadas_al_gimnasio_por_semana=str(input("horas dedicadas al gimnasio por semana:"))

# PROCESSING
total=horas_dedicadas_al_gimnasio_por_dia*horas_dedicadas_al_gimnasio_por_semana
visita_regular_al_gimnasio=(total_de_horas_por_semana < 15 )
if(visita_regular_al_gimnasio):
    print("Visita regular al gimnasio")
#fin_if


#EJERCICIO_46
vendedor,venta_de_lote_por_dia,venta_de_lote_por_semana="",0,0
vendedor=str(input("vendedor:"))
venta_de_lote_por_dia=str(input("venta de lote por dia:"))
venta_de_lote_por_semana=str(input("venta de lote por semana:"))

# PROCESSING
total=venta_de_lote_por_dia*venta_de_lote_por_semana
buen_vendedor=(total_venta_por_semana > 8000 )
if(buen_vendedor):
    print("Buen vendedor")
#fin_if


#EJERCICIO_47
empleada,venta_de_utiles_escolares_por_dia,venta_de_utiles_escolares_por_semana="",0,0
empleada=str(input("empleada:"))
venta_de_utiles_escolares_por_dia=str(input("venta de utiles escolares por dia:"))
venta_de_utiles_escolares_por_semana=str(input("venta de utiles escolares por semana:"))

# PROCESSING
total=venta_de_utiles_escolares_por_dia*venta_de_utiles_escolares_por_semana
ventas_bajas=(total_venta_por_semana < 800 )
if(ventas_bajas):
    print("Ventas bajas")
#fin_if


#EJERCICIO_48
nombre,horas_dedicadas_a_tocar_guitarra_por_dia,horas_dedicadas_a_tocar_guitarra_por_semana="",0,0
nombre=str(input("nombre:"))
horas_dedicadas_a_tocar_guitarra_por_dia=str(input("horas dedicadas a tocar guitarra por dia:"))
horas_dedicadas_a_tocar_guitarra_por_semanaç=str(input("horas dedicadas a tocar guitarra por semana:"))

# PROCESSING
total=horas_dedicadas_a_tocar_guitarra_por_dia*horas_dedicadas_a_tocar_guitarra_por_semana
aprende_a_tocar_guitarra=(total_de_horas_por_semana > 20 )
if(aprende_a_tocar_guitarra):
    print("Aprende a tocar guitarra")
#fin_if


#EJERCICIO_49
alumna,horas_dedicadas_a_tocar_violin_por_dia,horas_dedicadas_a_tocar_violin_por_semana="",0,0
alumna=str(input("alumna:"))
horas_dedicadas_a_tocar_violin_por_dia=str(input("horas dedicadas a tocar violin por dia:"))
horas_dedicadas_a_tocar_violin_por_semanaç=str(input("horas dedicadas a tocar violin por semana:"))

# PROCESSING
total=horas_dedicadas_a_tocar_violin_por_dia*horas_dedicadas_a_tocar_violin_por_semana
aprende_a_tocar_violin=(total_de_horas_por_semana > 25 )
if(aprende_a_tocar_violin):
    print("Aprende a tocar violin")
#fin_if


#EJERCICIO_50
alumna,horas_dedicadas_a_tocar_piano_por_dia,horas_dedicadas_a_tocar_piano_por_semana="",0,0
alumna=str(input("alumna:"))
horas_dedicadas_a_tocar_piano_por_dia=str(input("horas dedicadas a tocar piano por dia:"))
horas_dedicadas_a_tocar_piano_por_semanaç=str(input("horas dedicadas a tocar piano por semana:"))

# PROCESSING
total=horas_dedicadas_a_tocar_piano_por_dia*horas_dedicadas_a_tocar_piano_por_semana
no_aprende_a_tocar_piano=(total_de_horas_por_semana < 5 )
if(no_aprende_a_tocar_piano):
    print("No aprende a tocar violin")
#fin_if

