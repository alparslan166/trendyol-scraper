from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def scrape_trendyol(query, max_results=20):
    query = query.replace(" ", "+")
    url = f"https://www.trendyol.com/sr?q={query}"

    options = Options()
    options.add_argument("--headless")  # Tarayıcıyı başsız çalıştırmak için
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    # Tarayıcı yolu ve web driver
    options.binary_location = "/usr/bin/google-chrome-stable"  # Google Chrome için
    # Eğer Chromium kullanıyorsanız:
    # options.binary_location = "/usr/bin/chromium-browser"  # Chromium için

    # ChromeDriver'ı otomatik yüklemek için webdriver_manager'ı kullanıyoruz
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
