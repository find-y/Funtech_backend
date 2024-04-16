# Funtech_backend

[![CI/CD](https://github.com/Team88888/Funtech_backend/actions/workflows/ci_cd.yml/badge.svg)](https://github.com/Team88888/Funtech_backend/actions/workflows/ci_cd.yml)

Проект развернут на сервере:<br>
https://funtech-team8.duckdns.org/api/v1/<br>

  Администрирование приложения может быть осуществлено:
  - через админ панель по адресу https://funtech-team8.duckdns.org/admin<br>
  <a href="#t1">Учетные данные</a> для входа в админ-зону
  - через Swagger доступный по адресу https://funtech-team8.duckdns.org/docs

  Техническая документация:
  - Redoc доступен по адресу https://funtech-team8.duckdns.org/redoc
  - Скачать yaml-файл можно по адресу https://funtech-team8.duckdns.org

<br>

## Оглавление
- [Технологии](#технологии)
- [Описание работы](#описание-работы)
- [Установка приложения](#установка-приложения)
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

**!!! Для пользователей Windows обязательно выполнить команду:** иначе файл start.sh при клонировании будет бракован:
```bash
git config --global core.autocrlf false
```

Клонируйте репозиторий с GitHub и введите данные для переменных окружения (значения даны для примера, но их можно оставить):

```bash
git clone https://github.com/Team88888/Funtech_backend.git
cd Funtech_backend
cp env_example .env
nano .env
```

[⬆️Оглавление](#оглавление)

<br>

## Запуск приложения:

1. Из корневой директории проекта выполните команду:
```bash
docker compose -f infra/local/docker-compose.yml --env-file .env up -d --build
```
  Проект будет развернут в docker-контейнерах по адресу http://localhost/api/v1

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


```bash
docker compose -f infra/tests/docker-compose.yml --env-file .env up --build --abort-on-container-exit && \
docker compose -f infra/tests/docker-compose.yml --env-file .env down -v && \
docker system prune -f
```


```bash
pytest -x --cov --cov-config=.coveragerc
```
