# Тестовое задание

## Стек технологий

* Python,
* Django,
* DRF,
* PostgreSQL

## Запуск проекта в dev-режиме

- Клонировать репозиторий и перейти в него в командной строке.
- Установите и активируйте виртуальное окружение:

```bash
python -m venv venv
```

```bash
source venv/Scripts/activate
```

```bash
python -m pip install --upgrade pip
```

- Затем нужно установить все зависимости из файла requirements.txt

```bash
cd TestTask
```

```bash
pip install -r requirements.txt
```

- Выполняем миграции:

```bash
cd TestTask
```

```bash
python manage.py migrate
```

- Создаем суперпользователя:

```bash
python manage.py createsuperuser
```

- Запускаем проект:

```bash
python manage.py runserver
```

## Примеры работы с API для GET запросов

```r
GET api/weather/ - получить погоду в Саратове
GET api/articles/<int:pk>/ - получение конкретной статьи
GET api/articles/ - получение списка статей
```

## Примеры работы с API для остальных запрсосов

- Для отправки письма адресанту:

```r
POST /api/sendmail/
```

в body

```json
{
"email": string,
"message": string
}
```

- Сортировка массива:

```r
POST /api/sort/
```

в body

```json
{
"numbers": array,
"algorithm": int (любое число от 1 до 4х, где 1 - быстрая сортировка, 2 - пузырьковая, 3 - Timsort, 4 - вставками)
}
```

- Создание новой статьи

```r
POST /api/articles/
```

в body

```json
{
"title": string,
"text": string
}
```

- Обновление конкретной публикации:

```r
PUT /api/articles/<int:pk>/
```

- Удаление конкретной публикации:

```r
DELETE /api/articles/<int:pk>/
```



Автор: 
* Григорьев Олег Андреевич
