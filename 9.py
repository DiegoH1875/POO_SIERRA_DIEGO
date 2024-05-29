# Pregunta al usuario por una contraseña hasta que introduzca la contraseña correcta
CONTRASEÑA_CORRECTA = "POO123"
contraseña_usuario = ""
# Pedir al usuario por la contraseña
while True:
    contrasena_usuario = input("Introduce la contraseña: ")
    if contrasena_usuario == CONTRASEÑA_CORRECTA:
        print("Contraseña correcta, acceso permitido")
        break
    else:
        print("Contraseña incorrecta, intenta de nuevo")
        continue

