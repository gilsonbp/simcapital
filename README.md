# Sim Capital
SIM Capital Challenge Project


## Instalação:
> Será necessário o `docker` e `docker-compose`

- Após do download do sistema acesse a pasta do projeto e execute o comando abaixo para inicializar:
    - `docker-compose up -d`
    > Esse processo pode demorar uns 40 segundos. Se tentar executar os demais comandos antes pode receber uma mensagem pois o banco de dados ainda está sendo criado.
    > Se preferir pode remover o parâmetro `-d` para visualizar a inicialização.
- Para executar os testes execute o comando:
    - `docker-compose exec web python manage.py test`
    - Para gerar um relatório de cobertura de testes execute o comando abaixo:
        - `docker-compose exec web coverage run --source='.' manage.py test`
    - Acessando o relatório gerado:
        - `docker-compose exec web coverage report`
- Para criar um super usuário execute o comando:
    - `docker-compose exec web python manage.py createsuperuser`
- Acesse os logs através dos comandos:
    - `tail -f logs/gunicorn_error.log`
    - `tail -f logs/gunicorn_access.log`
- Acessando o sistema:
    - Após inicializar é possível acessar o sistema através dos endpoints:
        - [Acesse a documentação da API](https://github.com/gilsonbp/simcapital/wiki)