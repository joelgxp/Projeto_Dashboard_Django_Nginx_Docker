# Projeto_Dashboard_Django_Nginx_Docker
 Sistema web desenvolvido com Django, Nginx e Docker

## Pré-requisitos

- Python (versão 3.8.5-alpine)
- Django (versão 3.0.8)
- Gunicorn (versão 20.0.04)

## Configuração do Ambiente

1. Clone o repositório:

2. Crie e ative um ambiente virtual:
- python -m venv venv
- source venv/bin/activate  # No Windows, use `venv\Scripts\activate`

3. Instale as dependências:
- pip install -r requirements.txt

4. Execute as migrações:
- python manage.py migrate

5. Inicie o servidor de desenvolvimento:
- python manage.py runserver

Acesse http://localhost:8000/ em seu navegador.

