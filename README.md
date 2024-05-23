# Django REST API Exemplo

## Visão Geral

Este projeto é uma API RESTful construída com Django e Django REST Framework. O projeto também usa IPython para fornecer um shell interativo aprimorado para facilitar o desenvolvimento e a depuração.

## Requisitos

- Python 3.10
- Django 3.2+
- Django REST Framework 3.12+
- IPython

## Configuração do Ambiente

1. **Clone o repositório**:
    ```sh
    git clone https://github.com/flaviomouracarvalho/api_todo.git
    cd api_todo
    ```

2. **Crie e ative um ambiente virtual**:
    ```sh
    python3.10 -m venv venv
    source venv/bin/activate
    ```

3. **Instale as dependências**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Execute as migrações**:
    ```sh
    python manage.py migrate
    ```

5. **Inicie o servidor de desenvolvimento**:
    ```sh
    python manage.py runserver
    ```