from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

def scrape_trendyol(query, max_results=20):
    query = query.replace(" ", "+")
    url = f"https://www.trendyol.com/sr?q={query}"

    options = Options()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)

    # Sayfanın tamamen yüklenmesini bekle
    try:
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "p-card-wrppr")))
    except Exception as e:
        print(f"Sayfa yüklenemedi: {e}")
        driver.quit()
        return []

    # Sayfayı aşağı kaydır
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)  # Yeni öğelerin yüklenmesini bekle

    items = driver.find_elements(By.CLASS_NAME, "p-card-wrppr")
    print(f"Toplam ürün bulundu: {len(items)}")
    results = []

    for i, item in enumerate(items[:max_results]):
        try:
            # Ürün başlığını almak için XPath kullan
            name = item.find_element(By.XPATH, ".//div[contains(@class, 'prdct-desc')]").text
            
            # Fiyatı almak için alternatif bir XPath kullan
            price = item.find_element(By.XPATH, ".//div[contains(@class, 'price')]").text  # Alternatif fiyat seçici
            
            link = item.find_element(By.TAG_NAME, "a").get_attribute("href")

            results.append({
                "Ürün Adı": name,
                "Fiyat": price,
                "Link": link
            })
        except Exception as e:
            print(f"Bir hata oluştu: {e}")
            continue

    driver.quit()
    return results

def save_to_excel(data, filename="output.xlsx"):
    if data:
        df = pd.DataFrame(data)
        df.to_excel(filename, index=False)
        print(f"{filename} dosyasına başarıyla kaydedildi.")
    else:
        print("Veri kaydedilemedi.")

if __name__ == "__main__":
    query = input("Ne aramak istersiniz? ")
    results = scrape_trendyol(query)

    if results:
        save_to_excel(results)
    else:
        print("Hiç ürün bulunamadı.")
