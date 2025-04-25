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
    # Güncellenmiş Chrome ayarları
    options.binary_location = "/usr/bin/google-chrome"  # Doğru Chrome yolu
    options.add_argument("--headless=new")  # Yeni headless mod
    options.add_argument("--no-sandbox")  # Render için zorunlu
    options.add_argument("--disable-dev-shm-usage")  # Bellek sorunlarını önleme
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")  # Ekran boyutu ayarı

    # WebDriverManager ile ChromeDriver kurulumu
    service = Service(ChromeDriverManager().install())
    
    try:
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(url)

        # Bekleme süresini optimize etme
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.p-card-wrppr"))
        )

        results = []
        last_height = driver.execute_script("return document.body.scrollHeight")
        
        for _ in range(scroll_times):
            # Daha etkili scroll işlemi
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2.5)  # Optimize edilmiş bekleme süresi
            
            # Yeni yüklenen ürünleri bulma
            new_items = driver.find_elements(
                By.CSS_SELECTOR, "div.p-card-wrppr:not(.processed)"
            )
            
            for item in new_items[:max_results - len(results)]:
                try:
                    # XPath yerine CSS Selector kullanımı
                    name = item.find_element(
                        By.CSS_SELECTOR, "div.prdct-desc-cntnr-name"
                    ).text
                    price = item.find_element(
                        By.CSS_SELECTOR, "div.prc-box-dscntd"
                    ).text
                    link = item.find_element(
                        By.CSS_SELECTOR, "a"
                    ).get_attribute("href")
                    image = item.find_element(
                        By.CSS_SELECTOR, "img"
                    ).get_attribute("src")

                    results.append({
                        "title": name.strip(),
                        "price": price.strip(),
                        "link": link,
                        "image": image
                    })
                    
                    # İşlenen öğeleri işaretleme
                    driver.execute_script(
                        "arguments[0].classList.add('processed')", item
                    )
                except Exception as e:
                    print(f"Ürün çekme hatası: {str(e)[:100]}...")
                    continue

            if len(results) >= max_results:
                break

            # Yeni scroll height kontrolü
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        return results[:max_results]

    except Exception as e:
        print(f"Beklenmeyen hata: {str(e)}")
        return []
    finally:
        if 'driver' in locals():
            driver.quit()