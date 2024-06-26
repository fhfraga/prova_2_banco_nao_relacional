# Prova Banco de dados não-relacionais
Este projeto é referente a 2º prova da disciplina de banco de dados não relacionais

# Configuração
Para rodar este projeto, basta seguir os seguintes passos:

## Django
Na pasta principal do projeto, vá no terminal e digite.
```bash
$ poetry install
$ poetry shell
$ python manage.py runserver 8080
```

Seu projeto django ficará na url [http://127.0.0.1:8080/](http://127.0.0.1:8080/)

## FastAPI
Vá para a pasta `web_message` e dentro dela abra um terminal e digite.

`OBS.: O ambiente na pasta principal já tem que está rodando, recomendamos rodar o django primeiro, já que o mesmo precisa do ambiente rodando também`

```bash
$ uvicorn main:app --reload
```

# Programa em utilização
Neste [Link](https://www.youtube.com/watch?v=XRP4PmsqbPM) há um vídeo com o funcionamento do projeto.

