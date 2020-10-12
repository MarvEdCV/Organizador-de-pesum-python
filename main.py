# -------------------------------------------------IMPORTACION DE LIBRERIAS-------------------------------------#
import os
import time

from Datos import *

# -------------------------------------------------FIN DEIMPORTACION DE LIBRERIAS-------------------------------------#

# -------------------------------------------------INICIALIZACION DE VARIABLES GLOBALES-------------------------------#
op = 0
op1 = 0
listaCursos = []
lineas = ''


# -------------------------------------------------FIN DE VARIABLES GLOBALES------------------------------------------#
# -------------------------------------------------Metodos o funciones de errores----------------------------------
def opcionErronea(op, limI, limS):
    if limI > op or op > limS:
        print("\nSu opcion esta fuera de los parametros, intente ingresar una opcion correcta\n")
    else:
        print("Opcion valida\n")


# -------------------------------------------------fin deMetodos o funciones de errores----------------------------------


# Funcion de informacion
def infoDess():
    global op

    print('\n*-*-*-*-*-*-*-*-*-*-Lenguajes Formales de Programacion Seccion E*-*-*-*-*-*-*-*-*-*-\n'
          '*-*-*-*-*-*-*-*-*-*-           201905554                        *-*-*-*-*-*-*-*-*-*-\n'
          '*-*-*-*-*-*-*-*-*-*-     Marvin Eduardo Catalan Veliz           *-*-*-*-*-*-*-*-*-*-')
    input("\nPresione enter para continuar:")


infoDess()


def cargar():  # para cargar archivos csv en la memoria
    global op, listaCursos, lineas

    datos = input(
        'Escriba la ruta del archivo csv: (aquí puede ingresar archivo_ejemplo.csv o Pensum_sistemas.csv)\n')  # Aqui leo la URL de mi archivo
    archivo = open(datos, 'r',
                   encoding='UTF-8')  # Abro el archivo en modo lectura (Con encoding utf-8 para que salgan bien las tildes)
    lineas = archivo.readlines()  # le digo que tome todas las lineas del archivo y las ponga en un vector
    archivo.close()  # Cierro el archivo porque ya lei lo necesario

    for linea in lineas:  # Recorro todas las lineas con un foreach
        linea_spliteada = linea.split(
            ",")  # le aplico un split a cada linea para que cada valor separado por coma lo ponga en una posicion de un vector
        # En la lista de cursos general que cree al inicio comenzare a insertar objetos de tipo Curso, con la ayuda de la clase curso que defini en el archivo Datos.py
        listaCursos.append(
            Curso(linea_spliteada[0], linea_spliteada[1], linea_spliteada[2].split(";"), linea_spliteada[3],
                  linea_spliteada[4], linea_spliteada[5], linea_spliteada[6]))
        # Cuando agrego los datos a mi lista de cursos spliteo el campo de pre requisitos por ";" para que en esa posicion me guarde una lista con los codigos de los pre requisitos

    # Ahora ya tengo los cursos guardados en memoria... construire un .dot para graficarlos)
    print("Archivo cargado con exito")
    op = 0
    menuPrincipal()

def menuGestion():  # Para gestionar los datos obtenidos y guardados
    global Datos
    global op1
    while op1 < 1 or op1 > 6:
        print("**********Gestion de cursos**********\n"
              " 1--Listar cursos\n 2--Mostrar curso\n 3--Agregar curso\n 4--Editar curso\n 5--Eliminar curso\n6--Regresar a menu principal")
        op1 = int(input("Seleccione la opcion que necesita:"))
        opcionErronea(op1, 1, 6)

        if op1 is 1:
            op1 = 0
            for Datos in listaCursos:
                print(Datos.codigo,'-->',Datos.nombre)
            print('')

        if op1 is 2:
            op1 = 0
            i = 0
            nombrecuros = input('Por favor digite el #Codigo del curso que desea ver: ')
            for Datos in listaCursos:

                if (Datos.codigo == nombrecuros):
                    print('\nEl codigo"', Datos.codigo, '"pertenece a la clase:"', Datos.nombre, '"los pre-requisitos son:>>',
                          Datos.pre_requisitos, '<<\n',
                          'La opcionalidad es:"', Datos.opcionalidad, '"(Si es 1=obligatorio, si es 0=No obligatorio)',
                          'pertenece al semestre #', Datos.semestre,
                          ',otorga', Datos.creditos, 'creditos', 'y el estado del curso es:', Datos.estado,
                          '(0=aprobado,1=cursando,-1=pendiente)\n')
                    menuGestion()
                else:
                    i += 1

                if (i >= len(listaCursos)):
                    print('No existe ese curso\n')
                    menuGestion()
        if op1 is 3:
            op1 = 0
            i = 0
            cod = input('Ingrese codigo para verificar si existe: ')
            for Datos in listaCursos:
                if (Datos.codigo == cod):
                    print('\nEste curso ya existe, permanecera igual.Agrege un curso con codigo inexistente\n')
                else:
                    i += 1
            if (i >= len(listaCursos)):
                print('El curso no existe, se agregara uno nuevo al Pensum:\n')
                name = input('Ingrese el nombre del nuevo curso:\n')
                prerr = input(
                    'Ingrese los codigos de los cursos que se necesitan como pre-requisitos para cursar este curso: NOTA(si es mas de 1 pre-requisito separar por ";")\n')
                opcionalidad = input('digite una opcion para la opcionalidad\n1)obligatorio\n0)no obligatorio\n')
                semestre = input('Ingrese el semestre al que pertenece el curso:\n')
                creditos = input('Ingrese creditos por ganar el curso:\n')
                destado = input('digite la opcion para el estado del curso\n0)Aprobado\n1)Cursando\n-1)Pendiente\n')
                listaCursos.append(Curso(cod, name, prerr.split(';'), opcionalidad, semestre, creditos, destado))
            menuGestion()
        if op1 is 4:
            op1 = 0
            i = 0
            cod = input('Ingrese codigo para editar un curso: ')
            for Datos in listaCursos:
                if (Datos.codigo == cod):
                    print('\n*EL CODIGO SOLICITADO EXISTE\n')
                    print('Datos de curso: codigo:', Datos.codigo, " Nombre:", Datos.nombre, " Prerrequisitos:",
                              Datos.pre_requisitos, " opcionalidad:", Datos.opcionalidad,
                              " semestre:", Datos.semestre, " Creditos:", Datos.creditos,
                              " Estado:", Datos.estado)
                    opp = 0
                    while opp < 8 or opp > 1:
                        print("1)Codigo\n2)Nombre\n3)Pre-requisitos"
                              "\n4)Opcionalidad\n5)Semestre\n6)Creditos\n7)Estado\n8)Regresar a gestion de cursos")
                        opp = int(
                            input('Seleccione que atributos del curso desea editar\n(Si desea regresar teclee "8")\n'))
                        opcionErronea(opp, 1, 8)
                        if opp is 1:
                            ncod = input('Ingrese el nuevo codigo para el curso: ')
                            Datos.codigo=ncod
                            print('Se ha editado el codigo con exito\n')
                            opp = 8
                        if opp is 2:
                            nnom = input('Ingrese el nuevo nombre para el curso: ')
                            Datos.nombre=nnom
                            print('Se ha editado el nombre con exito\n')
                            opp = 8
                        if opp is 3:
                            npr = input('IMPORTANTE\nsi ingresara mas de un pre-rrequisito debe separarlos'
                                        'por punto y coma ";"\nIngrese el o los nuevos pre-requisitos para el curso:  ')
                            Datos.pre_requisitos=npr
                            print('Se ha editado el o los pre-requisitos con exito con exito\n')
                            opp = 8
                        if opp is 4:
                            nop = input(
                                '0=Opcional\n1=Obligatoria\n Teclee "0" o "1"\nIngrese la nueva opcionalidad del curso para el curso: ')
                            Datos.opcionalidad=nop
                            print('Se ha editado la opcionalidad del curso con exito\n')
                            opp = 8
                        if opp is 5:
                            nsem = input('Ingrese el nuevo semestre  para cursar el curso: ')
                            Datos.semestre=nsem
                            print('Se ha editado el semestre del curso con exito\n')
                            opp = 8
                        if opp is 6:
                            ncred = input('Ingrese el nuevo valor de creditos para el curso: ')
                            Datos.creditos=ncred
                            print('Se ha editado el numero de creditos para el curso con exito\n')
                            opp = 8
                        if opp is 7:
                            nest = input('Ingrese el nuevo estado del curso: ')
                            Datos.estado=nest
                            print('Se ha editado el estado del curso con exito\n')
                            opp = 8
                        if opp is 8:
                            menuGestion()
                else:
                    i += 1
                if (i >= len(listaCursos)):
                    print("El codigo ingresado no pertenece a ningun curso del Pensum")
                    menuGestion()
        if op1 is 5:
            op1 = 0
            i = 0
            cod = input('Ingrese codigo para eliminar un curso: ')
            for Datos in listaCursos:
                if (Datos.codigo == cod):
                    print('\n*EL CODIGO INGRESADO EXISTE\n')
                    print('Datos de curso a eliminar: codigo:', Datos.codigo, " Nombre:", Datos.nombre, " Prerrequisitos:",
                          Datos.pre_requisitos, " opcionalidad:", Datos.opcionalidad,
                          " semestre:", Datos.semestre, " Creditos:", Datos.creditos,
                          " Estado:", Datos.estado)
                    listaCursos.remove(Datos)
                else:
                    i += 1
                if (i >= len(listaCursos)):
                    print("El codigo ingresado no pertenece a ningun curso del Pensum")
                    menuGestion()
        if op1 is 6:
            menuPrincipal()

def conteo():  # Para contar los creditos
    global Datos
    import math
    suma=0
    suma1=0
    suma2=0
    suma3=0
    suma4=0
    suma5=0
    opc=0

    for Datos in listaCursos:
        for estado in Datos.estado:
            if estado == '-':
                for creditos in Datos.creditos:
                    suma2 += int(creditos)

    while opc < 1 or opc > 6:
        print("**********Conteo de Creditos**********\n"
              " 1--Contar todos los créditos aprobados:\n 2--Contar créditos cursando:\n 3--Contar créditos pendientes:\n"
              " 4--Contar créditos obligatorios hasta el semestre n:\n 5--Créditos del semestre:\n 6--Regresar a menu principal")
        opc = int(input("Seleccione la opcion que necesita:"))
        opcionErronea(opc, 1, 6)
        if opc is 1:

            for Datos in listaCursos:
                for estado in Datos.estado:
                    if estado == '0':
                        for creditos in Datos.creditos:
                            suma+=int(creditos)
            print('La sumatoria total de todos los creditos de cursos APROBADOS es: ',suma,'Creditos\n')
            conteo()

        if opc is 2:
            for Datos in listaCursos:
                for estado in Datos.estado:
                    if estado=='1':
                        for creditos in Datos.creditos:
                            suma1 += int(creditos)
            print('La sumatoria total de todos los creditos de cursos CURSANDO es: ', suma1-suma2, 'Creditos\n')
            conteo()
        if opc is 3:
            print('La sumatoria total de todos los creditos de cursos PENDIENTES es: ', suma2, 'Creditos\n')
            conteo()
        if opc is 4:

            n=input("\nIngrese numero de semestre n: \n")
            for Datos in listaCursos:
                for semestre in Datos.semestre:
                    if(semestre<=n):
                        for opcionalidad in Datos.opcionalidad:
                            if opcionalidad=='1':
                                for creditos in Datos.creditos:
                                    suma3 += int(creditos)
            print('La sumatoria total de todos los creditos de cursos OBLIGATORIOS desde el semestre 1 '
                  'hasta el semestre',n,'es: ', suma3, 'Creditos\n')
            conteo()
        if opc is 5:
            n1 = input("\nIngrese numero de semestre : \n")
            for Datos in listaCursos:
                for semestre in Datos.semestre:
                    if (semestre == n1):
                        for estado in Datos.estado:
                            if estado == '0':
                                for creditos in Datos.creditos:
                                    suma4 += int(creditos)
                                    print(suma4)
            for Datos in listaCursos:
                for semestre in Datos.semestre:
                    if (semestre == n1):
                        for estado in Datos.estado:
                            if estado == '-':
                                for creditos in Datos.creditos:
                                    suma5 += int(creditos)
            print('La sumatoria total de todos los creditos de cursos APROBADOS en el semestre '
                  , n1, 'es: ', suma4, 'Creditos\n')
            print('La sumatoria total de todos los creditos de cursos PENDIENTES en el semestre '
                  , n1, 'es: ', suma5, 'Creditos\n')
            conteo()
        if opc is 6:
            menuPrincipal()



def mapaDeCursos():
    global Datos
    global listaCursos
    global Curso
    import os
    import time
    f = open('archivo.dot', 'w', encoding='utf-8')
    f.write("digraph dibujo{\n")
    f.write('rankdir=LR;\n')
    f.write('node [shape = record, style=filled,fontname="Agency FB"];\n')

    # Hago un primer recorrido para nombrar los nodos de los cursos con sus etiquetas
    for Datos in listaCursos:
        for estado in Datos.estado:
            if(estado == '0'):
                f.write(
                    'curso' + Datos.codigo + '[ label ="Codigo: ' + Datos.codigo + ' | ' + Datos.nombre + '"'',fillcolor="green"];\n')
        for estado in Datos.estado:
            if estado=='1':
                f.write(
                    'curso' + Datos.codigo + '[ label ="Codigo: ' + Datos.codigo + ' | ' + Datos.nombre + '"'',fillcolor="yellow"];\n')
        for estado in Datos.estado:
            if estado == '-':
                f.write(
                    'curso' + Datos.codigo + '[ label ="Codigo: ' + Datos.codigo + ' | ' + Datos.nombre + '"'',fillcolor="red"];\n')



    # Hago un segundo recorrido para colocar las relaciones de los nodos
    for Datos in listaCursos:
        if (Datos.pre_requisitos[0] != ''):
            for pre_requisito in Datos.pre_requisitos:
                f.write('curso' + pre_requisito + '->curso' + Datos.codigo + ';\n')

    f.write('}')  # Termino de escribir el codigo dot
    f.close()  # Cierro el archivo

    """Ahora ya está listo el archivo.dot entonces:
    Con esta linea ejecuto la línea para interpretar el archivo .dot y generar la imagen. 
    Le paso como parámetro lo que escribía en el cmd la presentación 3."""
    os.system('dot -Tpng archivo.dot -o salida.png')

    """Con esta línea se abrirá la imagen con el visor de imágenes predeterminado en mi sistema """
    print('Hago una pausa de tres segundos para que termine de generar la imagen...')
    time.sleep(3)
    # Ahora si ya le digo que abra la imagen :D
    os.system('salida.png')

    menuPrincipal()


#Funcion del menu principal
def menuPrincipal():
    global op
    op=0
    # Menu principal y validacion de seleccion de opcion
    while op < 1 or op > 4:
        print('\n*-*-*-*-*-*-*-*-*-*-          Menu Principal                    *-*-*-*-*-*-*-*-*-*-\n'
              '*-*-*-*-*-*-*-*-*-*-1)Cargar archivo de entrada                 *-*-*-*-*-*-*-*-*-*-\n'
              '*-*-*-*-*-*-*-*-*-*-2)Gestionar cursos                          *-*-*-*-*-*-*-*-*-*-\n'
              '*-*-*-*-*-*-*-*-*-*-3)Conteo de creditos                        *-*-*-*-*-*-*-*-*-*-\n'
              '*-*-*-*-*-*-*-*-*-*-4)Mapa de cursos                            *-*-*-*-*-*-*-*-*-*-\n')
        op = int(input('Seleccione la opcion deseada: '))
        opcionErronea(op, 1, 4)
        if op is 1:
            cargar()
        elif op is 2:
            menuGestion()
        elif op is 3:
            conteo()
        if op is 4:
            mapaDeCursos()

menuPrincipal()
