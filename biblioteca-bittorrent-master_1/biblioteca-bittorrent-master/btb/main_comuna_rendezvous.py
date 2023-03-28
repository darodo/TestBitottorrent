from persona     import Persona
from recurso     import Recurso

from comuna      import Comuna



if __name__ == "__main__":

    # Crea el recurso que si tiene los datos (algo así como crear el torrent)
    imagen = Recurso('malla_411.png')

    curso = Recurso('curso.png')

    # Este sería el código de verdad
    # Esta soy yo... una persona dentro de la comuna
    print('malla', imagen.info_hash)
    print('curso', curso.info_hash)

    comuna = Comuna(6666)
    comuna.registrar_recurso_local(imagen)
    comuna.registrar_recurso_local(curso)

    print("Todo listo, presione q e intro para terminar.")
    esperar = 'a'
    while esperar != 'q':
        esperar = input()

    comuna.cerrar_comuna()
