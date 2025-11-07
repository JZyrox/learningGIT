CREATE DATABASE geografia_db;
\c geografia_db;

CREATE TABLE palabras_clave (
    id SERIAL PRIMARY KEY,
    palabra VARCHAR(50) NOT NULL,
    porcentaje_identidad DECIMAL(5,2) NOT NULL,
    sinonimos TEXT
);

INSERT INTO palabras_clave (palabra, porcentaje_identidad, sinonimos) VALUES
('Mapa', 95.00, 'cartografía, plano, croquis'),
('Territorio', 90.00, 'región, zona, área'),
('Clima', 92.50, 'meteorología, tiempo atmosférico'),
('Relieve', 88.00, 'topografía, orografía'),
('Continente', 93.00, 'masa continental, subcontinente'),
('Océano', 91.00, 'mar, cuerpo de agua'),
('Latitud', 89.50, 'coordenada norte-sur'),
('Longitud', 89.50, 'coordenada este-oeste'),
('Región', 87.00, 'zona, área geográfica'),
('Cultura', 82.00, 'costumbres, tradiciones'),
('Población', 90.00, 'habitantes, demografía'),
('Recursos naturales', 85.00, 'materias primas, bienes naturales'),
('Ecosistema', 84.50, 'hábitat, bioma'),
('Frontera', 86.00, 'límite, borde, divisoria'),
('País', 94.00, 'nación, estado, territorio'),
('Capital', 80.00, 'ciudad principal, sede del gobierno'),
('Coordenadas', 88.50, 'ubicación geográfica, latitud y longitud');
