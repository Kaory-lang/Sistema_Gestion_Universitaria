#Funciones generales
def float_checker(numero, layer):
    try:
        return float(numero)
    except: 
        print('!!!INSERTE UN NÚMERO VALIDO!!!')
        return layer

def int_checker(numero):
    try:
        return int(numero)
    except: 
        return False

def normalize(string):
    if type(string) == str:
        string = string.casefold().capitalize()
    return string

#Funciones de materias
def consult_materia(cursor):
    mat_consul = normalize(input('Introduzca el nombre o ID de la materia>> '))
    if int_checker(mat_consul) == False:
        cursor.execute(f'select * from materias where nombre = \'{mat_consul}\'')
        print('ID\tMateria')
        for x in cursor:
            print(f'{x[0]}-------{x[1]}')
        input('\nPulsa enter para continuar')
    else:
        cursor.execute(f'select * from materias where id = {mat_consul}')
        print('ID\tMateria')
        for x in cursor:
            print(f'{x[0]}-------{x[1]}')
        input('\nPulsa enter para continuar')
    return 1

def update_materias(cursor):
    mat_update = normalize(input('Introduzca el nombre o ID de la materia>> '))
    mat_updated = normalize(input('Introduzca el nuevo nombre de la meteria>> '))
    if int_checker(mat_update) == False:
        cursor.execute(f'update materias set nombre = "{mat_updated}" where nombre = "{mat_update}"')
        input('\nMateria cambiada exitosamente\nPulsa enter para continuar')
    else:
        cursor.execute(f'update materias set nombre = "{mat_updated}" where id = {mat_update}')
        input('\nMateria cambiada exitosamente\nPulsa enter para continuar')
    return 1

def delete_materias(cursor):
    del_mat = normalize(input('Introduzca el nombre o ID de la materia>> '))
    if int_checker(del_mat) == False:
        cursor.execute(f'delete from materias where nombre = "{del_mat}"')
        input('\nMateria eliminada exitosamente\nPulsa enter para continuar')
    else:
        cursor.execute(f'delete from materias where id = {del_mat}')
        input('\nMateria eliminada exitosamente\nPulsa enter para continuar')
    return 1

#Funciones de Carrera
def registrar_carrera(cursor):
    nombre_car = normalize(input('Introduzca el nombre de la carrera>> '))
    materias_car = input('Introduzca los ID de las meterias de la carrera separados por ",">> ')
    cursor.execute(f'insert into carreras (nombre, materias) values ("{nombre_car}", "{materias_car}")')
    input('\n---Carrera agregada correctamente.---\nPulse enter para continuar\n')
    return 2

def consult_carrera(cursor):
    car_consul = normalize(input('Introduzca el nombre o ID de la carrera>> '))
    if int_checker(car_consul) == False:
        cursor.execute(f'select * from carreras where nombre = \'{car_consul}\'')
        print('ID\tCarrera\t\tID materias')
        for x in cursor:
            print(f'{x[0]}-------{x[1]}-------{x[2]}')
        input('\nPulsa enter para continuar')
    else:
        cursor.execute(f'select * from carreras where id = {car_consul}')
        print('ID\tCarrera\t\tID materias')
        for x in cursor:
            print(f'{x[0]}-------{x[1]}-------{x[2]}')
        input('\nPulsa enter para continuar')
    return 2

def update_carreras(cursor):
    car_update = normalize(input('Introduzca el nombre o ID de la carrera>> '))
    car_updated = normalize(input('Introduzca el nuevo nombre de la meteria>> '))
    car_mat_update = normalize(input('Introduzca nuevos ID de las meteria(Dejar vacio si son las mismas)>> '))

    if int_checker(car_update) == False:
        if car_mat_update == '':
            cursor.execute(f'update carreras set nombre = "{car_updated}" where nombre = "{car_update}"')
        else:
            cursor.execute(f'update carreras set nombre = "{car_updated}", materias = "{car_mat_update}" where nombre = "{car_update}"')
        input('\nMateria cambiada exitosamente\nPulsa enter para continuar')
    else:
        if car_mat_update == '':
            cursor.execute(f'update carreras set nombre = "{car_updated}" where id = {car_update}')
        else:
            cursor.execute(f'update carreras set nombre = "{car_updated}", materias = "{car_mat_update}" where id = {car_update}')
        input('\nMateria cambiada exitosamente\nPulsa enter para continuar')
    return 2

def delete_carreras(cursor):
    del_car = normalize(input('Introduzca el nombre o ID de la carrera a eliminar>> '))
    if int_checker(del_car) == False:
        cursor.execute(f'delete from carreras where nombre = "{del_car}"')
        input('\nCarrera eliminada exitosamente\nPulsa enter para continuar')
    else:
        cursor.execute(f'delete from carreras where id = {del_car}')
        input('\nCarrera eliminada exitosamente\nPulsa enter para continuar')
    return 2

#Funciones Estudiantes
def registrar_estudiante(cursor):
    nombre_est = normalize(input('Introduzca el nombre del estudiante>> '))
    car_est = normalize(input('Introduzca el ID de la carrera que estudia el estudiante>> '))
    mat_est = normalize(input('Introduzca los ID de las materias que esta cursando el estudiante separados por "," >> '))
    sec_est = normalize(input('Introduzca las secciones a las que asiste respectivamente a las materias introducidas EJ:01,02S,03 >> '))

    if int_checker(car_est) == False:
        print('\n[ERROR]>> No se ha encontrado una carrera existente a el ID carrera introducido')
        input('Pulsar enter para continuar\n')
        return 4
    else:
        cursor.execute(f'select nombre from carreras where id = {int(car_est)}')
        car_est = cursor.fetchall()[0][0]

    cursor.execute(f'insert into estudiantes (nombre, carrera, materias, secciones) values ("{nombre_est}", "{car_est}", "{mat_est}", "{sec_est}")')
    return 4

def consult_estudiantes(cursor):
    id_mat = []
    secciones_est = []
    index = 0
    consul_estudiante = normalize(input('Introduzca el nombre o ID del estudiante>> '))

    if int_checker(consul_estudiante) == False:
        cursor.execute(f'select * from estudiantes where nombre = "{consul_estudiante}"')
        print('ID\tNombre\t\tCarrera\t\tMaterias[Sección]')

        #Cambia los ID por nombre de materias
        cursor.execute(f'select nombre from materias where id in ({cursor.fetchall()[0][3]})')
        for x in cursor:
            id_mat.append(x)

        #Guarda las secciones en listas
        cursor.execute(f'select secciones from estudiantes where nombre = "{consul_estudiante}"')
        for x in cursor:
            secciones_est = x[0].split(',')

        cursor.execute(f'select * from estudiantes where nombre = "{consul_estudiante}"')
    else:
        cursor.execute(f'select * from estudiantes where id = {int(consul_estudiante)}')
        print('ID\tNombre\t\tCarrera\t\tMaterias[Sección]')

        #Cambia los ID por nombre de materias
        cursor.execute(f'select nombre from materias where id in ({cursor.fetchall()[0][3]})')
        for x in cursor:
            id_mat.append(x)
        #Guarda las secciones en listas
        cursor.execute(f'select secciones from estudiantes where id = {consul_estudiante}')
        for x in cursor:
            secciones_est = x[0].split(',')

        cursor.execute(f'select * from estudiantes where id = {consul_estudiante}')

    #Imprime en consola de manera ordenada
    for x in cursor:
        print(f'{x[0]}-------{x[1]}-------{x[2]}-------', end='')
        for i in id_mat:
            print(f'{i[0]}[{secciones_est[index]}] ', end='')
            index = index + 1
    input('\nPulsa enter para continuar')
    return 4

def list_estudinates(cursor):
    id_mat = []
    secciones_est = []
    index = 0
    sub_index = 0

    print('ID\tNombre\t\tCarrera\t\tMaterias[Sección]\n')

    cursor.execute('select * from estudiantes')
    all_students = cursor.fetchall()
    
    for student in all_students:
        #Cambia los ID por nombre de materias
        try:
            cursor.execute(f'select nombre from materias where id in ({student[3]})')
            id_mat.append(cursor.fetchall())
        except: continue

    #Guarda las secciones en listas
    cursor.execute('select secciones from estudiantes')
    for x in cursor:
        secciones_est.append(x[0].split(','))

    cursor.execute(f'select * from estudiantes')
    #Imprime en consola de manera ordenada
    for x in cursor:
        print(f'{x[0]}-------{x[1]}-------{x[2]}-------', end='')
        for _i in id_mat[sub_index]:
            print(f'{id_mat[sub_index][index][0]}[{secciones_est[sub_index][index]}] ', end='')
            index = index + 1
        print('')
        index = 0
        sub_index = sub_index + 1
    input('\nPulsa enter para continuar')
    return 4

def update_estudiantes(cursor):
    est_update = normalize(input('Introduzca el nombre o ID del estudiante>> '))
    est_updated = normalize(input('Introduzca el nuevo nombre del estudiante>> '))
    est_mat_update = normalize(input('Introduzca nuevos ID de las meteria separados por "," (Dejar vacio si son las mismas)>> '))
    est_car_update = normalize(input('Introduzca nuevo nombre de la carrera(Dejar vacio si es la misma)>> '))
    est_sec_update = normalize(input('Introduzca las nuevas secciones separadas por "," (Dejar vacio si es la misma)>> '))

    if int_checker(est_update) == False:
        if est_mat_update != '':
            cursor.execute(f'update estudiantes set materias = "{est_mat_update}" where nombre = "{est_update}"')
        if est_car_update != '':
            cursor.execute(f'update estudiantes set carrera = "{est_car_update}" where nombre = "{est_update}"')
        if est_sec_update != '':
            cursor.execute(f'update estudiantes set secciones = "{est_sec_update}" where nombre = "{est_update}"')

        cursor.execute(f'update estudiantes set nombre = "{est_updated}" where nombre = "{est_update}"')
        input('\nCambio exitoso\nPulsa enter para continuar')
    else:
        if est_mat_update != '':
            cursor.execute(f'update estudiantes set materias = "{est_mat_update}" where id = {est_update}')
        if est_car_update != '':
            cursor.execute(f'update estudiantes set carrera = "{est_car_update}" where id = {est_update}')
        if est_sec_update != '':
            cursor.execute(f'update estudiantes set secciones = "{est_sec_update}" where id = {est_update}')

        cursor.execute(f'update estudiantes set nombre = "{est_updated}" where id = {est_update}')
        input('\nCambio exitoso\nPulsa enter para continuar')
    return 4

def delete_estudiante(cursor):
    del_est = normalize(input('Introduzca el nombre o ID del estudiante a eliminar>> '))
    if int_checker(del_est) == False:
        cursor.execute(f'delete from estudiantes where nombre = "{del_est}"')
        input('\nEstudiante eliminado exitosamente\nPulsa enter para continuar')
    else:
        cursor.execute(f'delete from estudiantes where id = {del_est}')
        input('\nEstudiante eliminado exitosamente\nPulsa enter para continuar')
    return 2

#Funciones Estudiantes
def registrar_profesor(cursor):
    f = ''
    nombre_prof = normalize(input('Introduzca el nombre del profesor>> '))
    car_prof = normalize(input('Introduzca los ID de las carreras que da el profesor separados por "," >> '))
    mat_prof = normalize(input('Introduzca los ID de las materias que esta dando el profesor separados por "," >> '))
    sec_prof = normalize(input('Introduzca las secciones a las que imparte clases respectivamente a las materias introducidas EJ: 01,02S,03 >> '))

    cursor.execute(f'select nombre from carreras where id in ({car_prof})')
    car_prof = cursor.fetchall()

    #Crea un str con las carreras correctamente ordenadas
    for x in car_prof:
        f = str(f) + str(x[0]) + ','

    cursor.execute(f'insert into profesores (nombre, carrera, materias, secciones) values ("{nombre_prof}", "{f[:-1]}", "{mat_prof}", "{sec_prof}")')
    input('Profesor agregado exitosamente\nPulsa enter para continuar')
    return 5

def consult_profesores(cursor):
    id_mat = []
    secciones_prof = []
    index = 0
    consul_profesor = normalize(input('Introduzca el nombre o ID del profesor>> '))

    if int_checker(consul_profesor) == False:
        cursor.execute(f'select * from profesores where nombre = "{consul_profesor}"')
        print('ID\tNombre\t\tCarrera\t\tMaterias[Sección]')

        #Cambia los ID por nombre de materias
        cursor.execute(f'select nombre from materias where id in ({cursor.fetchall()[0][3]})')
        for x in cursor:
            id_mat.append(x)

        #Guarda las secciones en listas
        cursor.execute(f'select secciones from profesores where nombre = "{consul_profesor}"')
        for x in cursor:
            secciones_prof = x[0].split(',')

        cursor.execute(f'select * from profesores where nombre = "{consul_profesor}"')
    else:
        cursor.execute(f'select * from profesores where id = {consul_profesor}')
        print('ID\tNombre\t\tCarrera\t\tMaterias[Sección]')

        #Cambia los ID por nombre de materias
        cursor.execute(f'select nombre from materias where id in ({cursor.fetchall()[0][3]})')
        for x in cursor:
            id_mat.append(x)

        #Guarda las secciones en listas
        cursor.execute(f'select secciones from profesores where id = {consul_profesor}')
        for x in cursor:
            secciones_prof = x[0].split(',')
        cursor.execute(f'select * from profesores where id = {consul_profesor}')
        #Imprime en consola de manera ordenada
    for x in cursor:
        print(f'{x[0]}-------{x[1]}-------{x[2]}-------', end='')
        for i in id_mat:
            print(f'{i[0]}[{secciones_prof[index]}] ', end='')
            index = index + 1
    input('\nPulsa enter para continuar')
    return 5

def list_profesores(cursor):
    id_mat = []
    secciones_prof = []
    index = 0
    sub_index = 0

    print('ID\tNombre\t\tCarrera\t\tMaterias[Sección]\n')

    cursor.execute('select * from profesores')
    all_profesores = cursor.fetchall()
    
    for student in all_profesores:
        #Cambia los ID por nombre de materias
        try:
            cursor.execute(f'select nombre from materias where id in ({student[3]})')
            id_mat.append(cursor.fetchall())
        except: continue

    #Guarda las secciones en listas
    cursor.execute('select secciones from profesores')
    for x in cursor:
        secciones_prof.append(x[0].split(','))

    cursor.execute(f'select * from profesores')
    #Imprime en consola de manera ordenada
    for x in cursor:
        print(f'{x[0]}-------{x[1]}-------{x[2]}-------', end='')
        for _i in id_mat[sub_index]:
            print(f'{id_mat[sub_index][index][0]}[{secciones_prof[sub_index][index]}] ', end='')
            index = index + 1
        print('')
        index = 0
        sub_index = sub_index + 1
    input('\nPulsa enter para continuar')
    return 5

def update_profesores(cursor):
    prof_update = normalize(input('Introduzca el nombre o ID del profesor>> '))
    prof_updated = normalize(input('Introduzca el nuevo nombre del profesor>> '))
    prof_mat_update = normalize(input('Introduzca nuevos ID de las meterias separados por "," (Dejar vacio si son las mismas)>> '))
    prof_car_update = normalize(input('Introduzca nuevos nombres de las carreras(Dejar vacio si es las mismas)>> '))
    prof_sec_update = normalize(input('Introduzca las nuevas secciones separadas por "," (Dejar vacio si es la misma)>> '))

    if int_checker(prof_update) == False:
        if prof_mat_update != '':
            cursor.execute(f'update profesores set materias = "{prof_mat_update}" where nombre = "{prof_update}"')
        if prof_car_update != '':
            cursor.execute(f'update profesores set carrera = "{prof_car_update}" where nombre = "{prof_update}"')
        if prof_sec_update != '':
            cursor.execute(f'update profesores set secciones = "{prof_sec_update}" where nombre = "{prof_update}"')

        cursor.execute(f'update profesores set nombre = "{prof_updated}" where nombre = "{prof_update}"')
        input('\nCambio exitoso\nPulsa enter para continuar')
    else:
        if prof_mat_update != '':
            cursor.execute(f'update profesores set materias = "{prof_mat_update}" where id = {prof_update}')
        if prof_car_update != '':
            cursor.execute(f'update profesores set carrera = "{prof_car_update}" where id = {prof_update}')
        if prof_sec_update != '':
            cursor.execute(f'update profesores set secciones = "{prof_sec_update}" where id = {prof_update}')

        cursor.execute(f'update profesores set nombre = "{prof_updated}" where id = {prof_update}')
        input('\nCambio exitoso\nPulsa enter para continuar')
    return 5

def delete_profesores(cursor):
    del_prof = normalize(input('Introduzca el nombre o ID del estudiante a eliminar>> '))
    if int_checker(del_prof) == False:
        cursor.execute(f'delete from profesores where nombre = "{del_prof}"')
        input('\nProfesor eliminado exitosamente\nPulsa enter para continuar')
    else:
        cursor.execute(f'delete from profesores where id = {del_prof}')
        input('\nProfesor eliminado exitosamente\nPulsa enter para continuar')
    return 5

#Funciones Materias(secciones) x Estudiante y Profesores
def materiasXsecciones(cursor, tabla):
    id_mat = []
    secciones_est = []
    index = 0

    if tabla == 'profesores':
        consul_estudiante = normalize(input('Introduzca el nombre o ID del profesor>> '))
    else:
        consul_estudiante = normalize(input('Introduzca el nombre o ID del estudiante>> '))

    if int_checker(consul_estudiante) == False:
        cursor.execute(f'select * from {tabla} where nombre = "{consul_estudiante}"')
        print('ID\tNombre\t\tCarrera\t\tMaterias[Sección]')

        #Cambia los ID por nombre de materias
        cursor.execute(f'select nombre from materias where id in ({cursor.fetchall()[0][3]})')
        for x in cursor:
            id_mat.append(x)

        #Guarda las secciones en listas
        cursor.execute(f'select secciones from {tabla} where nombre = "{consul_estudiante}"')
        for x in cursor:
            secciones_est = x[0].split(',')

        cursor.execute(f'select * from {tabla} where nombre = "{consul_estudiante}"')
    else:
        cursor.execute(f'select * from {tabla} where id = {consul_estudiante}')
        print('ID\tNombre\t\tMaterias[Sección]')

        #Cambia los ID por nombre de materias
        cursor.execute(f'select nombre from materias where id in ({cursor.fetchall()[0][3]})')
        for x in cursor:
            id_mat.append(x)
        #Guarda las secciones en listas
        cursor.execute(f'select secciones from {tabla} where id = {consul_estudiante}')
        for x in cursor:
            secciones_est = x[0].split(',')

        cursor.execute(f'select * from {tabla} where id = {consul_estudiante}')

    #Imprime en consola de manera ordenada
    for x in cursor:
        print(f'{x[0]}-------{x[1]}-------', end='')
        for i in id_mat:
            print(f'{i[0]}[{secciones_est[index]}] ', end='')
            index = index + 1
    input('\nPulsa enter para continuar')
    return 0