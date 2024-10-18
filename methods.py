print('Seleccione el proceso que desea aplicar')
def es_numero():
    print('1: Ingresar puntuación y comentario')
    print('2: Comprueba los resultados obtenidos hasta ahora.')
    print('3: Finalizar')
    num = input()
    if num.isdecimal():
        num = int(num)
        if num > 3 or num < 1:
            print("Ingrese un valor del 1 a 3")
            es_numero()
        else:
            admin_metodos(num)
    else:
        print("Por favor ingrese un numero")
        es_numero()


def valoracion():
    print("Ingrese puntaje de valoracion (1 a 5)")
    puntaje = input()
    if puntaje.isdecimal():
        puntaje = int(puntaje)
        if puntaje >= 1 and puntaje <= 5:
            print("Introduce un comentario")
            comment = input()
            post = f'punto: {puntaje} comentario: {comment}'
            archivo = open("data.txt", 'a')
            archivo.write(f'{post} \n' )
            archivo.close()
            es_numero()
            
        else:
            print("Ingrese un puntaje del 1 a 5")
            valoracion()
    else:
        print("Ingrese un numero")
        valoracion()
    


def results():
    print("Resultados hasta ahora")
    archivo = open("data.txt", "r")
    print(archivo.read())
    archivo.close
    es_numero()



def admin_metodos(valor):
    if valor == 1:
        valoracion()
    elif valor == 2:
        results()
    else:
        print("Fin")
        exit()


es_numero()