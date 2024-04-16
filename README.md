# Funtech_backend

[![CI/CD](https://github.com/Team88888/Funtech_backend/actions/workflows/ci_cd.yml/badge.svg)](https://github.com/Team88888/Funtech_backend/actions/workflows/ci_cd.yml)

Проект развернут на сервере:<br>
https://funtech-team8.duckdns.org/api/v1/ <br>
https://funtech-team8.duckdns.org/api/v2/ <br>

  Администрирование приложения может быть осуществлено:
  - через админ панель по адресу https://funtech-team8.duckdns.org/admin<br>
      <a href="#t1">Учетные данные</a> для входа в админ-зону
  - через Swagger доступный по адресу https://funtech-team8.duckdns.org/docs

  Техническая документация:
  - Redoc доступен по адресу https://funtech-team8.duckdns.org/redoc
  - Скачать yaml-файл можно по адресу https://funtech-team8.duckdns.org/schema

<br>

## Оглавление
- [Технологии](#технологии)
- [Установка приложения](#установка-приложения)
- [Запуск тестов](#запуск-тестов)
- [Запуск приложения](#запуск-приложения)
- [Удаление приложения](#удаление-приложения)
- [Авторы](#авторы)

<br>

## Установка приложения:

<details><summary>Предварительные условия</summary>

Предполагается, что пользователь установил [Docker](https://docs.docker.com/engine/install/) и [Docker Compose](https://docs.docker.com/compose/install/) на локальной машине. Проверить наличие можно выполнив команды:

```bash
    docker --version && docker-compose --version
```
</details>

<br>

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=250&width=435&lines=Для+пользователей+Windows:)](https://github.com/alexpro2022)

**!!! обязательно выполнить команду:** иначе файл start.sh при клонировании будет бракован:
```bash
    git config --global core.autocrlf false
```
<br><br>

Клонируйте репозиторий с GitHub и введите данные для переменных окружения (значения даны для примера, но их можно оставить):

```bash
    git clone https://github.com/Team88888/Funtech_backend.git
    cd Funtech_backend
    cp env_example .env
    nano .env
```

[⬆️Оглавление](#оглавление)

<br>

## Запуск тестов (Виртуальное окружение):

1. Создайте и активируйте виртуальное окружение и установите необходимые зависимости::
   * Если у вас Linux/macOS
   ```bash
    python -m venv venv && source venv/bin/activate
    python -m pip install --upgrade pip && pip install -r requirements/test.requirements.txt
   ```
   * Если у вас Windows
   ```bash
    python -m venv venv && source venv/Scripts/activate
    python -m pip install --upgrade pip && pip install -r requirements/test.requirements.txt
   ```

2. Из корневой директории проекта выполните команду:
```bash
    python funtech_proj/manage.py makemigrations
    pytest -x --cov --cov-config=.coveragerc
    deactivate
```

[⬆️Оглавление](#оглавление)

<br>

## Запуск приложения (Docker):

1. Из корневой директории проекта выполните команду:
```bash
    docker compose -f infra/local/docker-compose.yml --env-file .env up -d --build
```
  Проект будет развернут в docker-контейнерах по адресу <br>
  http://localhost/api/v1 <br>
  http://localhost/api/v2 <br>

  Администрирование приложения может быть осуществлено:
  - через админ панель по адресу http://localhost/admin
  - через Swagger доступный по адресу http://localhost/docs

  Техническая документация:
  - Redoc доступен по адресу http://localhost/redoc
  - Скачать yaml-файл можно по адресу http://localhost/schema

<h4 id="t1">Учетные данные для входа в админ-зону:</h4>
<ul>
  <li>login: adm@adm.com
  <li>password: admpw
</ul><br>

2. Остановить docker и удалить контейнеры можно командой из корневой директории проекта:

```bash
    docker compose -f infra/local/docker-compose.yml --env-file .env down
```

Если также необходимо удалить том базы данных:
```bash
    docker compose -f infra/local/docker-compose.yml --env-file .env down -v && docker system prune -f
```

[⬆️Оглавление](#оглавление)

<br>

## Удаление приложения:
Из корневой директории проекта выполните команду:
```bash
    cd .. && rm -fr Funtech_backend
```

[⬆️Оглавление](#оглавление)

<br>

## Авторы:
[Aleksei Proskuriakov](https://github.com/alexpro2022)

[⬆️В начало](#funtech_backend)
