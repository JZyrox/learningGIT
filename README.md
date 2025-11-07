# Design Document

**Proyecto:** Análisis de Texto Geográfico
**Autor:** Daniela Hernández
**Versión:** 1.1
**Fecha:** 6 de noviembre de 2025

---

## 1. Propósito del proyecto

El objetivo del sistema es **analizar un párrafo de texto**, eliminar palabras no relevantes (conectores) y **detectar términos geográficos clave** comparándolos con una base de datos PostgreSQL.
El programa muestra coincidencias con sus respectivos porcentajes de identidad y sinónimos, permitiendo identificar conceptos importantes en textos relacionados con geografía.

---

## 2. Alcance

El proyecto está pensado para ser una herramienta de análisis básico en el área educativa o de investigación.
Puede integrarse en plataformas que necesiten **procesamiento de texto semántico** para temas geográficos o lingüísticos.

---

## 3. Arquitectura general

### 3.1 Diagrama conceptual

```
+----------------+       +-------------------+       +---------------------+
|  parrafo.txt   | --->  | Procesamiento de  | --->  | PostgreSQL Database |
| (texto fuente) |       | texto en Python   |       | (palabras_clave)    |
+----------------+       +-------------------+       +---------------------+
         |                          |
         v                          v
  conectores.txt              Resultados mostrados
  (palabras irrelevantes)     en consola
```

---

## 4. Estructura del proyecto

El repositorio cuenta con los siguientes archivos dentro de la carpeta **BASEDATOS/**:

```
BASEDATOS/
│
├── conectores.txt        # Lista de conectores a eliminar del texto
├── filtrar_palabras.py   # Script principal en Python
├── geografia.sql         # Script SQL para crear la base de datos y tabla
├── parrafo.txt           # Párrafo a analizar
├── README.md             # Documentación general del proyecto
└── .venv/                # Entorno virtual (dependencias locales)
```

Esta estructura facilita mantener separado el código, los datos de entrada y los scripts de configuración de base de datos.

---

## 5. Componentes principales

### 5.1 Archivos externos

- **conectores.txt:** Lista de palabras comunes (como "y", "pero", "además") que serán filtradas.
- **parrafo.txt:** Texto a analizar.

### 5.2 Base de datos (PostgreSQL)

**Nombre:** `geografia_db`
**Tabla:** `palabras_clave`

| Campo                | Tipo de dato       | Descripción                                |
| -------------------- | ------------------ | ------------------------------------------ |
| id                   | SERIAL PRIMARY KEY | Identificador único                        |
| palabra              | VARCHAR(50)        | Palabra clave                              |
| porcentaje_identidad | DECIMAL(5,2)       | Grado de similitud o relevancia            |
| sinonimos            | TEXT               | Lista de sinónimos o términos relacionados |

Ejemplo de registro:

```
('Mapa', 95.00, 'cartografía, plano, croquis')
```

---

## 6. Flujo del programa

1. **Conexión:**
   El script se conecta a la base de datos PostgreSQL usando `psycopg2`.

2. **Carga de archivos:**

   - Lee `conectores.txt` para obtener las palabras a eliminar.
   - Lee `parrafo.txt` para extraer el texto que se analizará.

3. **Preprocesamiento del texto:**

   - Limpieza de signos de puntuación.
   - Conversión a minúsculas.
   - Separación por palabras.
   - Eliminación de conectores.

4. **Búsqueda en base de datos:**
   Para cada palabra filtrada:

   - Se busca una coincidencia exacta (`LOWER(palabra) = %s`).
   - Si se encuentra, se muestran el porcentaje y los sinónimos.
   - Si no, se indica que no hay coincidencia.

5. **Cierre:**
   Se cierra la conexión a la base de datos.

---

## 7. Ejemplo de ejecución

### Archivos:

**parrafo.txt**

```
El mapa del territorio muestra el relieve y los recursos naturales del país.
```

**conectores.txt**

```
el
del
y
los
de
```

### Salida esperada:

```
Palabras importantes detectadas:
['mapa', 'territorio', 'muestra', 'relieve', 'recursos', 'naturales', 'país']

Coincidencias encontradas en la base de datos:

Palabra: Mapa | Identidad: 95.0% | Sinónimos: cartografía, plano, croquis
Palabra: Territorio | Identidad: 90.0% | Sinónimos: región, zona, área
Palabra: Relieve | Identidad: 88.0% | Sinónimos: topografía, orografía
Palabra: País | Identidad: 94.0% | Sinónimos: nación, estado, territorio
'recursos' no se encontró en la base de datos.
```

---

## 8. Requisitos técnicos

### Software

- Python 3.12+
- PostgreSQL 14+
- Librería `psycopg2`

### Archivos requeridos

- `conectores.txt`
- `parrafo.txt`

### Dependencias

Instalación de librería:

```
pip install psycopg2
```

---

## 9. Posibles mejoras futuras

- Implementar coincidencias por similitud (usando `LIKE`, `LEVENSHTEIN`, o librerías NLP).
- Crear una interfaz web con Streamlit para subir archivos y mostrar resultados visualmente.
- Agregar soporte para más bases temáticas (historia, biología, etc.).
- Guardar resultados en una nueva tabla de análisis.

---

## 10. Autoría

Desarrollado por **Daniela Hernández**
Proyecto académico – Curso de Programación Lógica (7º semestre)
