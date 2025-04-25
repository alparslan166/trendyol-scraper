from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_trendyol(query, max_results=60, scroll_times=3):
    query = query.replace(" ", "+")
    url = f"https://www.trendyol.com/sr?q={query}"

    options = Options()
    options.add_argument("user-agent=Mozilla/5.0")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    # Burada chrome yerine chromium yolu kullanıyoruz
    options.binary_location = "/usr/bin/chromium"  # Render'da genellikle bu yol doğru olacaktır.

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)

    try:
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "p-card-wrppr")))
    except Exception as e:
        print(f"Sayfa yüklenemedi: {e}")
        driver.quit()
        return []

    results = []

    for _ in range(scroll_times):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)  # Sayfanın yüklenmesi için bekleme

        items = driver.find_elements(By.CLASS_NAME, "p-card-wrppr")
        print(f"Bu bölümde bulunan ürün sayısı: {len(items)}")

        for i, item in enumerate(items[:max_results - len(results)]):
            try:
                name = item.find_element(By.XPATH, ".//div[contains(@class, 'prdct-desc')]").text
                price = item.find_element(By.XPATH, ".//div[contains(@class, 'price')]").text
                link = item.find_element(By.TAG_NAME, "a").get_attribute("href")
                image = item.find_element(By.TAG_NAME, "img").get_attribute("src")

                results.append({
                    "title": name,
                    "price": price,
                    "link": link,
                    "image": image
                })
            except Exception as e:
                print(f"Hata: {e}")
                continue

        if len(results) >= max_results:
            break  # 60 ürün alındığında durdur

    driver.quit()
    return results
