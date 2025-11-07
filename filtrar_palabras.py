import psycopg2

# --- 1. Conexión a la base de datos ---
conexion = psycopg2.connect(
    dbname="geografia_db",
    user="postgres",        
    password="vaporwave",
    host="localhost",
    port="5432"
)
cursor = conexion.cursor()

# --- 2. Cargar conectores desde conectores.txt ---
try:
    with open("conectores.txt", "r", encoding="utf-8") as f:
        conectores = [line.strip().lower() for line in f.readlines()]
except FileNotFoundError:
    print("No se encontró el archivo 'conectores.txt'.")
    conectores = []

# --- 3. Leer el párrafo desde parrafo.txt ---
try:
    with open("parrafo.txt", "r", encoding="utf-8") as f:
        parrafo = f.read().strip()
except FileNotFoundError:
    print("No se encontró el archivo 'parrafo.txt'.")
    parrafo = ""

# --- 4. Procesamiento del texto ---
if parrafo:
    # Limpia signos de puntuación comunes
    for signo in [".", ",", ";", ":", "¿", "?", "¡", "!", "(", ")", "\""]:
        parrafo = parrafo.replace(signo, "")
    
    # Divide y pasa todo a minúsculas
    palabras = parrafo.lower().split()
    
    # Elimina conectores
    palabras_filtradas = [p for p in palabras if p not in conectores]

    print("\n Palabras importantes detectadas:")
    print(palabras_filtradas)

    print("\n Coincidencias encontradas en la base de datos:\n")

    for palabra in palabras_filtradas:
        cursor.execute("SELECT palabra, porcentaje_identidad, sinonimos FROM palabras_clave WHERE LOWER(palabra) = %s;", (palabra,))
        resultado = cursor.fetchone()
        
        if resultado:
            print(f"Palabra: {resultado[0]} | Identidad: {resultado[1]}% | Sinónimos: {resultado[2]}")
        else:
            print(f"'{palabra}' no se encontró en la base de datos.")
else:
    print("No se pudo leer ningún párrafo para analizar.")

# --- 5. Cierre de conexión ---
cursor.close()
conexion.close()
