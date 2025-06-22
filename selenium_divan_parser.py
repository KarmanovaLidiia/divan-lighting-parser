from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import json
import os

# 1. Настройка пути к chromedriver
driver_path = "C:/Users/karml/chromedriver-win64/chromedriver-win64/chromedriver.exe"

# 2. Настройки браузера
options = Options()
options.add_argument("--headless")  # Не открывать окно
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service, options=options)

# 3. Переход на сайт
url = "https://www.divan.ru/category/pryamye-divany"
driver.get(url)

# 4. Дать время странице загрузиться
time.sleep(5)

# 5. Найти карточки товаров
products = driver.find_elements(By.CSS_SELECTOR, 'div[data-testid="product-card"]')

results = []

for product in products:
    try:
        name = product.find_element(By.CSS_SELECTOR, "div[itemprop='name']").text
        price = product.find_element(By.CSS_SELECTOR, "meta[itemprop='price']").get_attribute("content")
        results.append({
            "название": name,
            "цена": f"{price} руб."
        })
    except Exception as e:
        print(f"❌ Ошибка в карточке: {e}")

# 6. Проверяем путь, куда сохраняем
save_path = os.path.join(os.getcwd(), "result.json")

# 7. Сохраняем в JSON файл
if results:
    try:
        with open(save_path, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print(f"\n✅ Сохранено {len(results)} товаров в файл:\n{save_path}")
        os.startfile(save_path)  # Автооткрытие файла в системе Windows
    except Exception as e:
        print(f"❌ Не удалось сохранить файл: {e}")
else:
    print("⚠️ Товары не найдены, файл не создан.")

# 8. Завершить работу драйвера
driver.quit()
