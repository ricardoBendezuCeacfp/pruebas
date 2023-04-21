'''
    - Al menos 2 de cada uno de lo siguiente:
        - mayúsculas
        - minúsculas
        - números
        - símbolos    
    - mínimo de caracteres: 8
    - orden aleatorio de los los caracteres
    
    librerias:
        - random
        - string
        
    Función generadora de iteradores que me devuelva una contraseña segura
'''


import random as rd
import string as st
def generadoraContraseña(lenContraseña):
    if lenContraseña < 8:
        yield "La contraseña debe de tener al menos 8 caracteres"
    else:
        caracteresValidos = list(set(st.ascii_letters + st.digits + st.punctuation))
        while True:
            listaCaracteresContraseña= rd.choices(caracteresValidos, k=lenContraseña)
            contraseñaFinal= ''.join(listaCaracteresContraseña)
            
            minusculasPresentes=comprobarCaracteres(contraseñaFinal, st.ascii_lowercase)
            mayusculasPresentes=comprobarCaracteres(contraseñaFinal, st.ascii_uppercase)
            numerosPresentes=comprobarCaracteres(contraseñaFinal, st.digits)
            caracteresEspecialesPresentes=comprobarCaracteres(contraseñaFinal, st.punctuation)
            
            if minusculasPresentes and mayusculasPresentes and numerosPresentes and caracteresEspecialesPresentes:
                yield contraseñaFinal
            else:
                print("Contraseña NO valida", contraseñaFinal)

def comprobarCaracteres(contraseña,caracteresAComprobar):
    contadorCaracteres=0
    for caracterInContraseña in contraseña:
        if caracterInContraseña in caracteresAComprobar:
            contadorCaracteres+=1
            if contadorCaracteres == 3:
                return True
    return False
iterador =generadoraContraseña(12)

print(next(iterador))


