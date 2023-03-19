CREATE DATABASE boticario;

CREATE SCHEMA load;
CREATE SCHEMA official;

CREATE TABLE load.base
(
    ID_MARCA   BIGINT encode zstd,
    MARCA      VARCHAR encode zstd,
    ID_LINHA   BIGINT encode zstd,
    LINHA      VARCHAR encode zstd,
    DATA_VENDA TIMESTAMP encode zstd,
    QTD_VENDA  BIGINT encode zstd,
    filename   VARCHAR encode zstd
);
