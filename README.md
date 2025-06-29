# 🛋️ divan-lighting-parser

Этот проект содержит парсеры для сайта [divan.ru](https://www.divan.ru), разработанные с использованием фреймворков **Scrapy** и **Selenium**.

## 📌 Описание

Репозиторий включает несколько парсеров, каждый из которых собирает данные о товарах с различных категорий сайта:

### ✅ Используемые технологии:
- `Scrapy` — быстрый и удобный фреймворк для веб-скрапинга
- `Selenium` — браузерная автоматизация (используется для более сложных случаев)
- `Python 3.13`

---

## 🔧 Структура

### 📁 Scrapy-парсеры:

1. `divannewpars.py` — парсит диваны с сайта  
   🔗 URL: `https://www.divan.ru/category/divany-i-kresla`

2. `svet_spider.py` — парсит светильники  
   🔗 URL: `https://www.divan.ru/category/svet`

📤 Результаты сохраняются в `result.csv`

---

### 📁 Selenium-парсер:

Файл: `selenium_divan_parser.py`  
Парсит карточки диванов с использованием браузера. Подходит для динамической подгрузки товаров.

📤 Сохраняет результат в `result.json`

> ⚠️ Убедитесь, что у вас установлен [chromedriver](https://sites.google.com/chromium.org/driver/) и путь указан в `driver_path`.

---

## 🚀 Как запустить

### Scrapy
```bash
scrapy crawl svet
scrapy crawl divannewpars
