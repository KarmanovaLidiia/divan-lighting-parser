# Scrapy Spider — Парсер освещения с сайта divan.ru

## 📌 Описание

Этот проект — Scrapy-паук, собирающий данные о товарах в категории "Свет" с сайта [divan.ru](https://www.divan.ru/category/svet). 
Сохраняет данные о:

- названии товара
- цене
- ссылке на карточку товара

Результаты сохраняются в `svet.json`.

## 🔧 Установка

```bash
pip install scrapy

scrapy crawl svet -o svet.json
