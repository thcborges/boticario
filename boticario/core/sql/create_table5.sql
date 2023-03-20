DROP TABLE IF EXISTS official.tabela5;
CREATE TABLE official.tabela5 AS
SELECT name,
       description,
       id,
       regexp_substr(regexp_substr(name, '(Episódio|Podcast)[\\s| ](\\d{{2}})'), '\\d{{2}}')::INT as total_episodes
FROM load.spotify_data_hackers_50;
