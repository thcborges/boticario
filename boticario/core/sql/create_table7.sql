DROP TABLE IF EXISTS official.tabela7;
CREATE TABLE official.tabela7 AS
SELECT id, name, description, release_date, duration_ms, language, "explicit", type
FROM load.spotify_data_hackers_full
WHERE 
    (name ilike '%data hackers%' OR name ilike '%staff+ podcast%') AND 
    (name LIKE '%Grupo Boticário%' OR description LIkE '%Grupo Boticário%');