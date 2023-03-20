DROP TABLE IF EXISTS official.tabela6;
CREATE TABLE official.tabela6 AS
SELECT id, name, description, release_date, duration_ms, language, "explicit", type
FROM load.spotify_data_hackers_full
WHERE name ilike '%data hackers%' OR name ilike '%staff+ podcast%';