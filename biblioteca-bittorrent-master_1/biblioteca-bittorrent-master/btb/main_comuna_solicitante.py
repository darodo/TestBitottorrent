from persona     import Persona
from recurso     import Recurso

from comuna      import Comuna


    

if __name__ == "__main__":


    # Este sería el código de verdad
    # Esta soy yo... una persona dentro de la comuna
    comuna = Comuna(7777)

    comuna_remota = Persona('127.0.0.1', 6666)
    comuna_remota.comuna = True

    comuna.registrar_comuna(comuna_remota)
    comuna.solicitar_personas()

    import time
    time.sleep(3)

    for persona in comuna.comité_registro.personas_remotas:
        if persona.comuna == True:
            comuna.comité_registro.solicitar_recursos(persona)

    time.sleep(2)

    for persona_remota in comuna.comité_registro.personas_remotas:
        if persona_remota.comuna == True:
            for recurso in persona_remota.recursos:
                comuna.comité_registro.solicitar_detalle_recurso(persona_remota, recurso.info_hash)

    time.sleep(1)

    """
    for persona in comuna.comité_registro.personas_remotas:
        print(persona)
        if persona.recursos != []:
            print(persona.recursos[0].info_hash)
    """

    recursos = comuna.listar_recursos_locales()
    print(recursos)
    recursos = comuna.listar_recursos_remotos()
    print(recursos)

    recurso = Recurso()
    recurso.cargar_archivo_meta_info('curso.png.vttorrent')

    print('Traer este recurso', recurso.info_hash) 
    comuna.gestionar_recurso_remoto(recurso)

    print('#############')
    recursos = comuna.listar_recursos_locales()
    print(recursos)
    print('$$$$$$$$$$$$$')
    recursos = comuna.listar_recursos_remotos()
    print(recursos)
    print('=============')

    print("Todo listo")
    print("Presione q e intro para salir")

    a = 'a'
    while a != 'q':
        a = input()

    comuna.cerrar_comuna()
