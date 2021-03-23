
def run():# funcion principal

# inicializando variables ----------------------------
	alumnos_sistemas=0
	alumnos_software=0
	alumnos_electronica=0
	suma_edad_sistemas=0
	suma_edad_software=0
	suma_edad_electronic=0
	mayor_edad_sistemas=0
	mayor_edad_software=0
	mayor_edad_electronica=0
	menor_edad_sistemas=999
	menor_edad_software=999
	menor_edad_electronica=999

	n=int(input("Digite la cantidad de estudiantes: "))
#--------------------------- para cada estudiante solicitar los datos---------------------------------
	for i in range(n):
		print(f"\tAlumno {i+1}")
		codigo=input("Digite el codigo: ")
		nombre=input("Digite el nombre: ")
		apellido=input("Digite el  apellido: ")
		sexo=int(input("Digite el sexo (masculino=1)(femenino=2): "))
		edad=int(input("Digite la edad: "))
		carrera=int(input("Digite la carrera (ingenieria sistemas=1),(ingenieria software=2),(ingenieria electronica=3): "))

		if carrera==1:# si es de sistemas
			alumnos_sistemas+=1
			suma_edad_sistemas+=edad
			if edad>mayor_edad_sistemas:
				mayor_edad_sistemas=edad
			if edad<menor_edad_sistemas:
				menor_edad_sistemas=edad

		elif carrera==2:# si es de software
			alumnos_software+=1
			suma_edad_software+=edad
			if edad>mayor_edad_sistemas:
				mayor_edad_software=edad
			if edad<menor_edad_software:
				menor_edad_software=edad

		elif carrera==3: # si es de electronica
			alumnos_electronica+=1
			suma_edad_electronic+=edad
			if edad>mayor_edad_sistemas:
				mayor_edad_electronica=edad
			if edad<menor_edad_electronica:
				menor_edad_electronica=edad

#----------------------------------imprimiendo -------------------------------------------------
	print("\nLa sumatoria y cantidad de edades por carrera profesional es respectivamente: ")

	print(f"ingenieria sistemas sumatoria y cantidad : {suma_edad_sistemas}, {alumnos_sistemas}")
	print(f"ingenieria software sumatoria y cantidad : {suma_edad_software}, {alumnos_software}")
	print(f"ingenieria electronica sumatoria y cantidad : {suma_edad_electronic}, {alumnos_electronica}")
	print("\nEl mayor y menor edad de estudiantes de todas las carreras respectivamente: ")

	if mayor_edad_sistemas>0:
		print(f"ingenieria sistemas mayor edad: {mayor_edad_sistemas}")
	if menor_edad_sistemas!=999:
		print(f"ingenieria sistemas menor edad: {menor_edad_sistemas}")
	if mayor_edad_software>0:
		print(f"ingenieria software mayor edad: {mayor_edad_software}")
	if menor_edad_software!=999:
		print(f"ingenieria software menor edad: {menor_edad_software}")
	if mayor_edad_electronica>0:
		print(f"ingenieria electronica mayor edad: {mayor_edad_electronica}")
	if menor_edad_electronica!=999:
		print(f"ingenieria electronica menor edad: {menor_edad_electronica}")

if __name__ == '__main__':
	run()