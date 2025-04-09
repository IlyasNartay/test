from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(
    "https://kaspi.kz/shop/c/smartphones/?q=%3Acategory%3ASmartphones%3AavailableInZones%3AMagnum_ZONE1&sort=rating&sc")

try:
    # 2. Выставить фильтр на модель телефонов Samsung
    wait = WebDriverWait(driver, 20)

    # Ждем появления фильтра брендов и скроллим к нему
    brand_filter = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//div[contains(@class, 'filters__filter') and contains(., 'Бренд')]")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", brand_filter)
    time.sleep(1)

    # Находим чекбокс Samsung через JavaScript клик, чтобы избежать перехвата
    samsung_checkbox = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                  "//div[contains(@class, 'filters__filter-row') and contains(., 'Samsung')]//input[@type='checkbox']")))
    driver.execute_script("arguments[0].click();", samsung_checkbox)

    # Даем время для применения фильтра
    time.sleep(3)

    # 3. Скопировать все названия моделей с первой страницы
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "item-card")))

    # Прокручиваем страницу вниз для загрузки всех элементов
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    page_html = driver.page_source
    soup = BeautifulSoup(page_html, 'html.parser')

    # Собираем названия моделей (уточните селекторы по реальной странице)
    model_names = []
    items = soup.find_all('div', class_='item-card')

    for item in items:
        name_element = item.find('a', class_='item-card__name-link') or item.find('div', class_='item-card__name')
        if name_element:
            model_names.append(name_element.text.strip())

    # 4. Сохранить в файл
    with open('Модели.txt', 'w', encoding='utf-8') as f:
        for model in model_names:
            f.write(model + '\n')

    print(f"Сохранено {len(model_names)} моделей в файл 'Модели.txt'")

except Exception as e:
    print(f"Произошла ошибка: {str(e)}")
    driver.save_screenshot('error.png')

finally:
    driver.quit()