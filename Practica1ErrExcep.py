# Excepcion para validar entradas incorrectas
class EntradaInvalidaError(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

# Clase Alumno con atributos y metodos
class Alumno:
    def __init__(self, nombre, apellido, edad, matricula):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.matricula = matricula

    # Metodo para mostrar la informacion de un alumno
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre} {self.apellido}, Edad: {self.edad}, Matricula: {self.matricula}")

    # Metodo estatico que compara dos alumnos y devuelve el de mayor edad
    @staticmethod
    def comparar_edad(alumno1, alumno2):
        return alumno1 if alumno1.edad > alumno2.edad else alumno2

# Funcion para llenar la lista de alumnos con validacion de datos
def llenar_lista_alumnos():
    alumnos = []
    try:
        cantidad = int(input("Cuantos alumnos quieres registrar? "))
        for i in range(cantidad):
            print(f"\nAlumno #{i+1}")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")

            # Validacion de edad
            try:
                edad = int(input("Edad: "))
                if edad <= 0:
                    raise EntradaInvalidaError("La edad debe ser un numero positivo.")
            except ValueError:
                raise EntradaInvalidaError("Edad invalida. Debe ser un numero entero.")

            matricula = input("Numero de matricula: ")

            # Se crea el objeto Alumno y se agrega a la lista
            alumnos.append(Alumno(nombre, apellido, edad, matricula))

        return alumnos

    except ValueError:
        raise EntradaInvalidaError("Cantidad invalida. Debe ser un numero entero.")

# Lista global para almacenar alumnos
alumnos = []

# Funcion principal con menu interactivo
def main():
    global alumnos
    while True:
        print("\n--- Menu ---")
        print("1. Registrar alumnos")
        print("2. Mostrar informacion de los alumnos")
        print("3. Comparar edades de dos alumnos")
        print("4. Salir")

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            # Registro de alumnos con manejo de errores
            try:
                alumnos = llenar_lista_alumnos()
                print("\nAlumnos registrados correctamente.")
            except EntradaInvalidaError as e:
                print(f"Error: {e}")

        elif opcion == "2":
            # Mostrar informacion de todos los alumnos
            if not alumnos:
                print("No hay alumnos registrados.")
            else:
                print("\nInformacion de los alumnos:")
                for alumno in alumnos:
                    alumno.mostrar_informacion()

        elif opcion == "3":
            # Comparar edades de dos alumnos
            if len(alumnos) < 2:
                print("Debes registrar al menos dos alumnos.")
            else:
                try:
                    print("\nLista de alumnos:")
                    for i, alumno in enumerate(alumnos):
                        print(f"{i}: {alumno.nombre} {alumno.apellido}")

                    a = int(input("Escribe el numero del primer alumno a comparar: "))
                    b = int(input("Escribe el numero del segundo alumno a comparar: "))

                    if 0 <= a < len(alumnos) and 0 <= b < len(alumnos):
                        mayor = Alumno.comparar_edad(alumnos[a], alumnos[b])
                        print("\nEl alumno de mayor edad es:")
                        mayor.mostrar_informacion()
                    else:
                        print("Indices fuera de rango.")

                except ValueError:
                    print("Debes ingresar un numero valido.")

        elif opcion == "4":
            # Salir del programa
            print("Gracias por usar el sistema.")
            break

        else:
            print("Opcion invalida. Por favor elige entre 1 y 4.")

# Llamar a la funcion principal para iniciar el programa
if __name__ == "__main__":
    main()