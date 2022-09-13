print("Bienvenido a mi trivia")
print("                                                                                                      ")
print("Pondremos a prueba tus conocimientos")
print("                                                                                                      ")
nombre = input("ingrese su nombre porfavor: ")
print("\n Hola" , nombre, " responde las siguientes preguntas. \n")
puntaje=0
print ("tienes", puntaje, "puntos")
print("                                                                                                      ")
print("Primera pregunta")
print("¿Cual es el lugar mas frio de la tierra?")
print("Tienes las opciones: a, b, c, d")
print("\n alternativas : " "   "
      "a) Siberia" "  "
      "b) Oymyakon" "  "
      "c)Verjoyansk" "  "
      "d) La Antartida \n")
      
respuesta_1 = input ("Tu respuesta: ")
while respuesta_1 not in ("a" , "b", "c", "d"):
    respuesta_1 = input (" debes responder a, b ,c ,d. ingresa tu respuesta: ")
if respuesta_1 == "a":
    print("Incorrecto!", nombre, "el lugar mas frio es la antartida")
elif respuesta_1 =="b":
    print("Incorrecto!", nombre, "el lugar mas frio es la antartida ")
elif respuesta_1 =="c":
    print("Incorrecto!", nombre, "el lugar mas frio es la antartida")
else:
    puntaje +=10
    print("muy bien!", nombre)
print("                                                                ")
print("Segunda pregunta")
print("                                                                ")
print("¿Cuantos huesos tiene el cuerpo humano?")
print("\n alternativas : " "   "
      "a) 301" "  "
      "b) 206" "  "
      "c) 205" "  "
      "d) 204 \n")  
respuesta_2= input ("Tu respuesta: ")
while respuesta_2 not in ("a" , "b", "c", "d"):
    respuesta_2 = input (" debes responder a, b ,c ,d. ingresa tu respuesta: ")

if respuesta_2 == "a":
    print("Incorrecto!", nombre, "el cuerpo humano posee 206 huesos y los recien nacidos +300")
elif respuesta_2 =="c":
    print("Incorrecto!", nombre, "el cuerpo humano posee 206 huesos y los recien nacidos +300")
elif respuesta_2 =="d":
    print("Incorrecto!", nombre, "el cuerpo humano posee 206 huesos y los recien nacidos +300")
else:
    puntaje +=10
    print("Muy bien!", nombre)
print("                                                                ")
print ("Gracias", nombre, "por jugar mi trivia"", " "alcanzaste: " , puntaje, "puntos")
