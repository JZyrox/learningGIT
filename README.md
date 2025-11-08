Design Document

Proyecto: Análisis de Texto Geográfico
Autor: Daniela Hernández
Versión: 1.0
Fecha: 8 de noviembre de 2025

1. Propósito del proyecto

El objetivo de este proyecto es proporcionar la base de datos y el texto fuente utilizados en un análisis geográfico.
Los archivos incluidos permiten crear una base de datos en PostgreSQL con términos relacionados con la geografía y un texto de ejemplo para futuras pruebas o análisis semánticos.

2. Alcance

El contenido del proyecto está diseñado como base para prácticas o proyectos educativos enfocados en el procesamiento de lenguaje natural (NLP) o análisis de textos geográficos.
Puede utilizarse en aplicaciones que requieran la detección de palabras clave relacionadas con la geografía o el medio ambiente.

3. Arquitectura general
   3.1 Diagrama conceptual
   +----------------+ +---------------------+
   | parrafo.txt | ---> | PostgreSQL Database |
   | (texto fuente) | | (palabras_clave) |
   +----------------+ +---------------------+

El archivo parrafo.txt sirve como entrada textual, mientras que geografia.sql define la estructura de la base de datos y los términos de referencia

4. Estructura del proyecto

BASEDATOS/
│
├── geografia.sql # Script SQL que crea la base de datos y tabla de palabras clave
├── parrafo.txt # Texto descriptivo geográfico a analizar
└── .venv/ # Entorno virtual (dependencias locales de Python)

5. Componentes principales
   5.1 Archivo SQL – geografia.sql

Nombre de la base de datos: geografia_db
Tabla: palabras_clave

| Campo                | Tipo de dato       | Descripción                                 |
| -------------------- | ------------------ | ------------------------------------------- |
| id                   | SERIAL PRIMARY KEY | Identificador único                         |
| palabra              | VARCHAR(50)        | Término geográfico clave                    |
| porcentaje_identidad | DECIMAL(5,2)       | Grado de relevancia o similitud             |
| sinonimos            | TEXT               | Lista de sinónimos o conceptos relacionados |

Ejemplo de registros incluidos:

('Mapa', 95.00, 'cartografía, plano, croquis')
('Territorio', 90.00, 'región, zona, área')
('Clima', 92.50, 'meteorología, tiempo atmosférico')
('País', 94.00, 'nación, estado, territorio')

Este script permite crear y poblar automáticamente la tabla con términos geográficos relevantes.

5.2 Archivo de texto – parrafo.txt

Contenido:
El mapa del territorio mexicano muestra el relieve y el clima de cada región.
Este mapa ayuda a comprender cómo el clima influye en la población y los recursos naturales del país.
En todo el territorio, el relieve determina las actividades humanas, mientras que el clima afecta los ecosistemas presentes en cada región del país.

Este texto sirve como entrada de prueba para realizar análisis de coincidencia o extracción de palabras clave utilizando la base de datos creada por geografia.sql.

6. Flujo básico de uso

1.Crear la base de datos en PostgreSQL:
\i geografia.sql

2.Leer el texto del archivo parrafo.txt.

3.Comparar palabras clave:
Un script (no incluido en esta versión) podría analizar el texto, eliminar conectores y buscar coincidencias exactas en la tabla palabras_clave.

4.Mostrar resultados:
Se pueden listar las palabras encontradas junto con su porcentaje de identidad y sinónimos.

7. Ejemplo de coincidencias esperadas
   Del texto incluido, se podrían detectar las siguientes palabras en la base de datos:
   | Palabra detectada | Porcentaje | Sinónimos |
   | ----------------- | ---------- | -------------------------------- |
   | Mapa | 95.00% | cartografía, plano, croquis |
   | Territorio | 90.00% | región, zona, área |
   | Clima | 92.50% | meteorología, tiempo atmosférico |
   | Relieve | 88.00% | topografía, orografía |
   | País | 94.00% | nación, estado, territorio |
   | Región | 87.00% | zona, área geográfica |

8. Requisitos técnicos

Software

- PostgreSQL 14 o superior
- (Opcional) Python 3.12+ si se desea automatizar el análisis

Dependencias sugeridas

Si se emplea Python:
pip install psycopg2 pandas

9. Posibles mejoras futuras

Agregar un script en Python para automatizar el análisis de coincidencias.

Implementar una interfaz web (por ejemplo, con Streamlit).

Incorporar más términos geográficos o científicos en la base de datos.

Aplicar análisis semántico mediante NLP.

10. Autoría

Desarrollado por Daniela Hernández
Proyecto académico – Curso de Programación Lógica (7º semestre)
