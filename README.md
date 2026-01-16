# AQA Python – Тесты логина (SauceDemo)

## Описание
Автоматизированные UI-тесты функционала авторизации на сайте  
https://www.saucedemo.com

Используемый стек:
Python, Playwright, Pytest, Allure  
Архитектура: Page Object Model (POM)

Проект демонстрирует базовый подход к AQA-тестированию с отчётами Allure и понятной структурой.

---

## Структура проекта
src/
pages/        – Page Object'ы (описание страниц)
tests/        – UI-тесты
utils/        – Вспомогательные модули и конфигурации
conftest.py   – Pytest-фикстуры (page и др.)
requirements.txt
Dockerfile
README.md

---

## Требования
Python 3.10+
Playwright
Allure CLI
Docker (опционально)

---

## Запуск локально

1. Установка зависимостей
pip install -r requirements.txt

2. Установка браузеров Playwright
playwright install

3. Запуск тестов с генерацией отчёта
pytest --alluredir=allure-results

4. Просмотр Allure-отчёта
allure serve allure-results

---

## Запуск через Docker

Сборка Docker-образа
docker build -t aqa-tests .

Запуск тестов в контейнере
docker run aqa-tests

---

## Покрываемые сценарии авторизации

1. Успешный логин  
standard_user / secret_sauce

2. Логин с неверным паролем

3. Заблокированный пользователь  
locked_out_user

4. Логин с пустыми полями

5. Пользователь с задержками  
performance_glitch_user

---

## Особенности проекта
• Используется Page Object Model  
• Чистое разделение логики тестов и страниц  
• Allure-отчёты с feature и story  
• Код легко читать и расширять

---

## Настройка проекта в IDE (PyCharm)

После открытия проекта в PyCharm рекомендуется пометить папку `src` как **Source Root**:

1. Нажать правой кнопкой мыши на папку `src`
2. Выбрать **Mark Directory as → Sources Root**

Это необходимо, чтобы:
- корректно работали импорты (`from pages.login_page import LoginPage`)
- IDE правильно находила модули проекта

