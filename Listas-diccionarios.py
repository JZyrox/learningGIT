# Lista vacía para almacenar los estudiantes
estudiantes = []

# Función para agregar un estudiante
def agregar_estudiante(nombre, edad, calificaciones):
    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "calificaciones": calificaciones  # lista de diccionarios
    }
    estudiantes.append(estudiante)
    print(f"✅ Estudiante {nombre} agregado correctamente.")

# Función para eliminar un estudiante por nombre
def eliminar_estudiante(nombre):
    global estudiantes
    estudiantes = [est for est in estudiantes if est["nombre"] != nombre]
    print(f"🚮 Estudiante {nombre} eliminado (si existía en la lista).")

# Función para calcular el promedio de un estudiante
def calcular_promedio(nombre):
    for est in estudiantes:
        if est["nombre"] == nombre:
            notas = [materia["calificacion"] for materia in est["calificaciones"]]
            promedio = sum(notas) / len(notas)
            print(f"📊 El promedio de {nombre} es: {promedio:.2f}")
            return promedio
    print(f"❗ Estudiante {nombre} no encontrado.")
    return None



# Ejemplo de como se usa el programa.

# Agregar estudiantes
agregar_estudiante("Daniela", 20, [
    {"materia": "Matemáticas", "calificacion": 90},
    {"materia": "Historia", "calificacion": 85},
    {"materia": "Programación", "calificacion": 95},
    {"materia": "Inglés", "calificacion": 80}
])

agregar_estudiante("Jesús", 22, [
    {"materia": "Matemáticas", "calificacion": 70},
    {"materia": "Historia", "calificacion": 65},
    {"materia": "Programación", "calificacion": 75},
    {"materia": "Inglés", "calificacion": 60}
])

# Calcular promedio
calcular_promedio("Daniela")
calcular_promedio("Jesús")

# Eliminar un estudiante
eliminar_estudiante("Jesús")

# Intentar calcular promedio de Jesús después de eliminarlo
calcular_promedio("Jesús")
