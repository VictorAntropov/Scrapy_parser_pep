# Асинхронный парсер PEP.
## Цель проекта:
- Создание парсера для сбора информации о PEP на базе фреймворка Scrapy.
---
## Описание проекта:
- Сбор данных о PEP, анализ и сохранение в формате CSV.
- Первый файл .csv в директории results/ содержит информацию о списке всех PEP c официального сайта, их номера, названия, статусы.
- Второй файл .csv в директории results/ содержит сводку по статусам PEP(Количество документов в каждом статусе, а также суммарное количество).
---
### Запуск проекта в dev-режиме:

- Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone https://github.com/VictorAntropov/scrapy_parser_pep.git
```

- Cоздать виртуальное окружение:

```
python -m venv venv
```

* Активировать виртуальное окружение:

 ```bash
source venv/Scripts/activate
```

- Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```
```
python -m pip install --upgrade pip
```
- Запустить парсер из командной строки:

```
scrapy crawl pep
```

##  Автор проекта:
### Антропов Виктор:
```
e-mail: AntropovVictor.V@yandex.ru
GitHub: github.com/VictorAntropov
```