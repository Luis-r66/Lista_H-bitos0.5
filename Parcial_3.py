class ListaHabitos:
    def __init__(self):
        self.habitos = []

    def agregar_habito(self, nombre, frecuencia, duracion):
        habito = [nombre, frecuencia, duracion]
        self.habitos.append(habito)
        self.ordenar_habitos()
        print(f"Hábito '{nombre}' agregado.")

    def eliminar_habito(self, nombre):
        self.habitos = [habito for habito in self.habitos if habito[0] != nombre]
        self.ordenar_habitos()
        print(f"Hábito '{nombre}' eliminado.")

    def mostrar_habitos(self):
        if self.habitos:
            print("Hábitos:")
            for habito in self.habitos:
                print(f"[Nombre: {habito[0]}, Frecuencia: {habito[1]} veces/semana, Duración: {habito[2]} minutos]")
        else:
            print("No hay hábitos registrados.")

    def ordenar_habitos(self):
        self.habitos.sort(key=lambda x: x[0])
        print("Hábitos ordenados por nombre.")

def main():
    lista_habitos = ListaHabitos()

    while True:
        print("\nMenú:")
        print("1. Ingresar hábito")
        print("2. Eliminar hábito")
        print("3. Mostrar hábitos")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del hábito: ")
            frecuencia = int(input("Ingrese la frecuencia del hábito (por semana): "))
            duracion = int(input("Ingrese la duración del hábito (en minutos): "))
            lista_habitos.agregar_habito(nombre, frecuencia, duracion)
        elif opcion == "2":
            nombre = input("Ingrese el nombre del hábito a eliminar: ")
            lista_habitos.eliminar_habito(nombre)
        elif opcion == "3":
            lista_habitos.mostrar_habitos()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
