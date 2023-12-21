tiempo = input("Introduce la hora por la que pasa el corredor a la hora indicada: ")
km = input("Introduce el punto kilométrico por el que pasa el corredor a la hora indicada: ")
carrera = input("¿El corredor ha acabado la carrera, si o no?: ")
corredor = {tiempo:km}
while carrera == "no":
    tiempo = input("Introduce la hora por la que pasa el corredor a la hora indicada: ")
    km = input("Introduce el punto kilométrico por el que pasa el corredor a la hora indicada: ")
    carrera = input("¿El corredor ha acabado la carrera, si o no?: ")
if carrera == "si":
    print("El corredor a las", tiempo, "estaba en el km", km)