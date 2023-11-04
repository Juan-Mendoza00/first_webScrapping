DROP DATABASE IF EXISTS libros;
CREATE DATABASE libros;
-- Ejecutar desde aqui si la base de datos ya está creada.
USE libros;

DROP TABLE IF EXISTS libros_semana;
CREATE TABLE libros_semana (
	IdLibro INT NOT NULL AUTO_INCREMENT,
    Titulo VARCHAR(150),
    Fecha_Publicación DATE,
    URL VARCHAR(150),
    Precio DOUBLE,
    Precio_USD DOUBLE,
    Precio_DolarBlue DOUBLE,
    Fecha_carga DATE,
    PRIMARY KEY(IdLibro)
);

DROP TABLE IF EXISTS auditoria_errores;
CREATE TABLE auditoria_errores (
	IdError INT NOT NULL AUTO_INCREMENT,
    Titulo VARCHAR(150),
    URL VARCHAR(150),
    PRIMARY KEY(IdError)
);