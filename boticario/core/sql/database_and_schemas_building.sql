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

CREATE TABLE load.spotify_data_hackers_50
(
    audio_preview_url      VARCHAR encode zstd,
    description            VARCHAR(65535) encode zstd,
    duration_ms            BIGINT encode zstd,
    "explicit"             bool encode zstd,
    external_urls          VARCHAR encode zstd,
    href                   VARCHAR encode zstd,
    html_description       VARCHAR(65535) encode zstd,
    id                     VARCHAR encode zstd,
    images                 VARCHAR(65535) encode zstd,
    is_externally_hosted   bool encode zstd,
    is_playable            bool encode zstd,
    "language"             VARCHAR encode zstd,
    languages              VARCHAR encode zstd,
    name                   VARCHAR(500) encode zstd,
    release_date           VARCHAR encode zstd,
    release_date_precision VARCHAR encode zstd,
    "type"                 VARCHAR encode zstd,
    "uri"                  VARCHAR encode zstd
);

CREATE TABLE load.spotify_data_hackers_full
(
    audio_preview_url      VARCHAR encode zstd,
    description            VARCHAR(65535) encode zstd,
    duration_ms            BIGINT encode zstd,
    "explicit"             bool encode zstd,
    external_urls          VARCHAR encode zstd,
    href                   VARCHAR encode zstd,
    html_description       VARCHAR(65535) encode zstd,
    id                     VARCHAR encode zstd,
    images                 VARCHAR(65535) encode zstd,
    is_externally_hosted   bool encode zstd,
    is_playable            bool encode zstd,
    "language"             VARCHAR encode zstd,
    languages              VARCHAR encode zstd,
    name                   VARCHAR(500) encode zstd,
    release_date           VARCHAR encode zstd,
    release_date_precision VARCHAR encode zstd,
    "type"                 VARCHAR encode zstd,
    "uri"                  VARCHAR encode zstd
);
