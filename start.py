#Nombre: Kaory Henríquez
#Matrícula: 19-1416
#Fecha: 4/26/2021
#GitHub del projecto: https://github.com/Kaory-lang/Sistema_Gestion_Universitaria.git

import mysql.connector
from functions import *

#Database conecction
mydb = mysql.connector.connect(host='localhost', user='root', password='root', database='universidad')
cursor = mydb.cursor(buffered=True)
int_checker(2)##quitar
#Inicio de sesion
print('Inicio de sesión al sistema de Gestión Universitaria\n')

intentos = 3
validation = None

while intentos > 0:
    nombre = input('Inserte nombre de Usuario>> ')
    cursor.execute(f'select psw from usuarios where nombre = "{nombre}"')

    validation = cursor.fetchall()

    if len(validation) < 1:
        intentos = intentos - 1
        print('\nUsuario no encontrado, intentos restantes =', intentos, '\n')
    else:
        break
while intentos > 0:
    print (validation[0][0])
    password = input('Inserte contraseña>> ')

    if password == validation[0][0]:
        print('Acceso Autorizado\n')
        intentos = -1
    else:
        intentos = intentos - 1
        print('Contraseña incorrecta, intentos restantes =', intentos, '\n')

if intentos == 0:
    exit()

#Menu de opciones del Sistema de Gestion Universitaria
layer = 0
layers_aceptados = [0,1,2,3,4,5,6,7]
while True:
    #Menu principal
    if layer == 0:
        print('Con que desea trabajar? Seleccione el numero y pulse ENTER\n')
        change_layer = input('[1]Materias\t\t\t\t[2]Carreras\n[3]Materias x Carrera\t\t\t[4]Estudiantes\n[5]Profesores\t\t\t\t[6]Materias(secciones) x Estudiante\n[7]Materias(secciones) x Profesores\n\n>> ')
        layer = float_checker(change_layer, layer)
    #Menu materias
    try:
        if layer == 1:
            print('Que desea hacer? Seleccione el numero y pulse ENTER\n')
            print('Menu Materias\n')
            change_layer = input('[1.1]Registrar\t\t[1.2]Consultar\n[1.3]Listar\t\t[1.4]Actualizar\n[1.5]Eliminar\t\t[0]Menú principal\n\n>> ')
            layer = float_checker(change_layer, layer)

            #Sub Menus Materias
            if layer == 1.1:
                nombre_mat = normalize(input('Introduzca el nombre de la materia>> '))
                cursor.execute(f'insert into materias (nombre) values (\'{nombre_mat}\')')
                mydb.commit()
                print('\n---Materias agregada correctamente.---\nPulse enter para continuar\n')
                layer = 1
            if layer == 1.2:
                layer = consult_materia(cursor)
            if layer == 1.3:
                cursor.execute('Select * from materias')
                print('ID\tMateria')
                for x in cursor:
                    print(f'{x[0]}-------{x[1]}')
                input('\nPulsa enter para continuar')
                layer = 1
            if layer == 1.4:
                layer = update_materias(cursor)
                mydb.commit()
            if layer == 1.5:
                layer = delete_materias(cursor)
                mydb.commit()
    except:
        input('[Error]>> Al intentar hacer la accion\nEnter para continuar')
        layer = 0
    #Menu carreras
    try:
        if layer == 2:
            print('Que desea hacer? Seleccione el numero y pulse ENTER\n')
            print('Menu Carreras\n')
            change_layer = input('[2.1]Registrar\t\t[2.2]Consultar\n[2.3]Listar\t\t[2.4]Actualizar\n[2.5]Eliminar\t\t[0]Menú principal\n\n>> ')
            layer = float_checker(change_layer, layer)

            #Sub Menus Carreras
            if layer == 2.1:
                layer = registrar_carrera(cursor)
                mydb.commit()
            if layer == 2.2:
                layer = consult_carrera(cursor)
            if layer == 2.3:
                cursor.execute('Select * from carreras')
                print('ID\tMateria\t\tID Materias')
                for x in cursor:
                    print(f'{x[0]}-------{x[1]}-------{x[2]}')
                input('\nPulsa enter para continuar')
                layer = 2
            if layer == 2.4:
                layer = update_carreras(cursor)
                mydb.commit()
            if layer == 2.5:
                layer = delete_carreras(cursor)
                mydb.commit()
    except:
        input('[Error]>> Al intentar hacer la accion\nEnter para continuar')
        layer = 2

    #Menu Meteria x Carrera
    try:
        if layer == 3:
            print('Menu Materias x Carrera\n')
            carrera = normalize(input('Introduzca el nombre o ID de la carrera>> '))

            if int_checker(carrera) == False:
                cursor.execute(f'select materias from carreras where nombre = "{carrera}"')
            else:
                cursor.execute(f'select materias from carreras where id  = {carrera}')

            print('\nLas materias para la carrera son>>\n')
            result = cursor.fetchall()[0][0].split(',')
            for x in result:
                cursor.execute(f'select nombre from materias where id = {int(x)}')
                print(cursor.fetchall()[0][0])
            input('\nPulse enter para continuar')
            layer = 0
    except:
        input('[Error]>> Al intentar hacer la accion\nEnter para continuar')
        layer = 0

    #Menu Estudiantes
    try:
        if layer == 4:
            print('Que desea hacer? Seleccione el numero y pulse ENTER\n')
            print('Menu Estudiantes\n')
            change_layer = input('[4.1]Registrar\t\t[4.2]Consultar\n[4.3]Listar\t\t[4.4]Actualizar\n[4.5]Eliminar\t\t[0]Menú principal\n\n>> ')
            layer = float_checker(change_layer, layer)

            #Sub Menus Estudiantes
            if layer == 4.1:
                layer = registrar_estudiante(cursor)
                mydb.commit()
            if layer == 4.2:
                layer = consult_estudiantes(cursor)
            if layer == 4.3:
                layer = list_estudinates(cursor)
            if layer == 4.4:
                layer = update_estudiantes(cursor)
                mydb.commit()
            if layer == 4.5:
                layer = delete_estudiante(cursor)
                mydb.commit()
    except:
        input('[Error]>> Al intentar hacer la accion\nEnter para continuar')
        layer = 4
    #Menu Profesores
    if layer == 5:
        print('Que desea hacer? Seleccione el numero y pulse ENTER\n')
        print('Menu Profesores\n')
        change_layer = input('[5.1]Registrar\t\t[5.2]Consultar\n[5.3]Listar\t\t[5.4]Actualizar\n[5.5]Eliminar\t\t[0]Menú principal\n\n>> ')
        layer = float_checker(change_layer, layer)

        #Sub Menus Profesores
        if layer == 5.1:
            try:
                layer = registrar_profesor(cursor)
                mydb.commit()
            except:
                input('[Error]>> Al intentar registar al profesor\nEnter para continuar')
                layer = 5
        if layer == 5.2:
            try:
                layer = consult_profesores(cursor)
            except:
                input('[Error]>> Al intentar consultar a la base de datos\nEnter para continuar')
                layer = 5
        if layer == 5.3:
            try:
                layer = list_profesores(cursor)
            except:
                input('[Error]>> Al intentar listar\nEnter para continuar')
                layer = 5
        if layer == 5.4:
            try:
                layer = update_profesores(cursor)
                mydb.commit()
            except:
                input('[Error]>> Al intentar actualizar la base de datos\nEnter para continuar')
                layer = 5
        if layer == 5.5:
            try:
                layer = delete_profesores(cursor)
                mydb.commit()
            except:
                input('[Error]>> Al intentar borrar de la base de datos\nEnter para continuar')
                layer = 5
    
    #Menu Materias(secciones) x Estudiante y profesores
    try:
        if layer == 6:
            print('Materias(secciones) x Estudiante\n')
            layer = materiasXsecciones(cursor, 'estudiantes')
        if layer == 7:
            print('Materias(secciones) x Profesores\n')
            layer = materiasXsecciones(cursor, 'profesores')
    except:
        input('[Error]>> Al intentar hacer la accion\nEnter para continuar')
        layer = 0
    
    miss = layers_aceptados.count(layer)
    if miss == 0:
        input('Introduzca un número correcto\nEnter para continuar\n')
        layer = 0
