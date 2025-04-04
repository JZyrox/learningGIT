def busca_arreglo(busca):
    """Busca una palabra en un arreglo predefinido."""
    arreglo_palabras = ["rojo", "verde", "azul", "negro", "morado"]
    return "Encontrada en arreglo" if busca.lower() in arreglo_palabras else "No se encontró en el arreglo"

def busca_en_archivo(busca, archivo):
    """Busca una palabra en un archivo de texto."""
    try:
        with open(archivo, 'r', encoding='utf-8') as file:
            return busca.lower() in file.read().lower()
    except FileNotFoundError:
        print(f"Error: Archivo {archivo} no encontrado.")
        return False

def verificar_palabra(busca):
    """Verifica una palabra en todos los recursos disponibles."""
    if busca_arreglo(busca) == "Encontrada en arreglo":
        return "✅ Palabra encontrada en el diccionario."
    if busca_en_archivo(busca, 'palabras.txt'):
        return "📖 Palabra encontrada en el archivo principal."
    if busca_en_archivo(busca, 'groserias.txt'):
        return "🚫 Palabra no permitida encontrada."
    return "🔍 Palabra no encontrada en ningún recurso."