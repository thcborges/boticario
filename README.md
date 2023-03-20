# Grupo Boticário Case2


O projeto atual está configurado para rodar sobre linha de comando.



Para as bases recebidas, o acesso ao S3, local onde as bases estavam armazenadas 
foi gerenciado usando o [S3 Fuse](https://github.com/s3fs-fuse/s3fs-fuse)
possibilitando assim acesso local ao bucket do S3 como se estivesse acessando recurso local.

## Instalação

O projeto depende da instalação do [Poetry](https://python-poetry.org/docs/)


```Bash
curl -sSL https://install.python-poetry.org | python3 -
```

Com o Poetry instalado basta instalar o pacotte do projeto.


```Bash
poetry install
```

## Execução

A aplicação tem um CLI próprio para execução e pode ser executada com os comando a seguir:

```Bash
boticario base-ingestion-task && boticario base-create-table1-task && boticario base-create-table2-task && boticario base-create-table3-task && boticario base-create-table4-task
```

```Bash
 boticario spotify-50-task && boticario spotify-create-table5-task && boticario spotify-full-task && boticario spotify-create-table6-task && boticario spotify-create-table7-task
```


## Airflow

É possível instalar a wheel do projeto em um ambiente com airflow e usar as DAGs disponíveis na pasta [dag](https://github.com/thcborges/boticario/tree/main/dags).

Para construir a wheel do projeto: 

```Bash
poetry build
```

O poetry criará uma pasta chamada dist e dentro dela conterá a whell para instalação com o PIP. 
Então bastará instalar a wheel com o comando a seguir e copiar os arquivos dentro da pasta dag
para a pasta dag de dags do airflow.

Exemplo:
```Bash
pip install /home/ubuntu/projects/boticario/dist/boticario-0.1.0-py3-none-any.whl
```
