<h1 align="center">Backend Python Wallet</h1>
<p align="center">Desafio para vaga de backend na MaisTodos</p>

## Prerequisitos
- python-dev ou python3-dev
- python3-venv
- make
- docker

## Passo a passo para rodar a aplicação
1) Instale os prerequisitos

### Banco de dados
Para criar o banco e deixa-lo configurado como necessitamos para a aplicação, devemos:

```
docker pull mariadb
docker run --name container -p 3306:3306 -e MYSQL_ROOT_PASSWORD=pass -d mariadb
docker cp ./scripts/sql/walletDB.sql container:/walletDB.sql
docker exec -it container bash
mysql -p (dê enter e digite a senha: pass)
source walletDB.sql
```

### Servidor
1) Rode no seu terminal `cat .env.example > .env` para criar um arquivo .env
2) Rode no seu terminal `make create_env` para criar um ambiente python do projeto
3) Rode no seu terminal `. ./env/bin/activate` para ativar esse ambiente
4) Rode no seu terminal `make install_packages` para instalar os pacotes
5) Rode no seu terminal `make run_server` e o servidor estará rodando na porta `8000`
6) Se quiser rodar os testes unitários, rode no seu terminal `make run_test`
7) Acesse `localhost:8000/docs` para acessar o Swagger do projeto onde encontrará todas as rotas implementadas

## Email e senha para autenticação
```
username: mais_tod@s.com
password: MeContrataNaHumilda
```

## Tests coverage
