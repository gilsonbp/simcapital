# Sim Capital
SIM Capital Challenge Project


## Instalação:
> Será necessário o `docker` e `docker-compose`

- Após do download do sistema acesse a pasta do projeto e execute o comando abaixo para inicializar:
    - `docker-compose up -d`
- Para executar os testes execute o comando:
    - `docker-compose exec web python manage.py test`
- Para criar um super usuário execute o comando:
    - `docker-compose exec web python manage.py createsuperuser`
- Acesse os logs através dos comandos:
    - `tail -f logs/gunicorn_error.log`
    - `tail -f logs/gunicorn_access.log`