# Base de Datos: Geografía PostgreSQL

## Descripción

Este proyecto crea una base de datos local en **PostgreSQL** llamada `geografia_db`, que contiene una tabla `palabras_clave` con información relacionada al tema **Geografía**.

Cada registro representa una palabra clave asociada a la disciplina, junto con un **porcentaje de identidad** (qué tanto se asocia al tema) y **sinónimos** que ayudan a ampliar la búsqueda semántica.

---

## Estructura de la tabla

| Columna              | Tipo de dato       | Descripción                                                        |
| -------------------- | ------------------ | ------------------------------------------------------------------ |
| id                   | SERIAL PRIMARY KEY | Identificador único                                                |
| palabra              | VARCHAR(50)        | Palabra principal relacionada con Geografía                        |
| porcentaje_identidad | DECIMAL(5,2)       | Valor numérico del 0 al 100 que representa la relación con el tema |
| sinonimos            | TEXT               | Lista de sinónimos o términos relacionados                         |

---

## Contenido

La tabla contiene más de 15 palabras representativas de la Geografía, como:

- Mapa
- Clima
- Relieve
- Continente
- País
- Territorio
- Océano
- Latitud
- Longitud
- Región
- Cultura
- Población
- Recursos naturales
- Ecosistema
- Frontera
- Capital
- Coordenadas

Cada palabra incluye su **porcentaje de identidad** y **sinónimos**.

---

## Cómo ejecutar

1. Abrir la terminal de Windows o Visual Studio Code.
2. Conectarse al servidor PostgreSQL con tu usuario (por ejemplo `postgres`):

```bash
psql -U postgres
```
