# Trendyol Scraper

Bu proje, **Trendyol**'dan ürün verilerini çekmek için geliştirilmiş bir Python uygulamasıdır. Kullanıcılar belirli bir ürün ismi girerek, Trendyol üzerindeki ilgili ürünleri listeleyebilirler.

## Teknolojiler
- Python 3.x
- Selenium
- WebDriver Manager

## Kurulum

1. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

2. WebDriver'ı otomatik olarak yönetmek için `webdriver-manager` kullanıyoruz. WebDriver'ınızın doğru sürümde olduğundan emin olun.

## Kullanım

1. `app.py` dosyasını çalıştırarak uygulamayı başlatın.
   ```bash
   python app.py
   ```

2. Uygulama çalışmaya başladığında, girilen ürün ismine göre Trendyol'dan sonuçları listeleyecektir.
![İlk Ekran](https://github.com/alparslan166/trendyol-scraper/blob/main/images/ilkEkran.png)

## Özellikler
- **Arama**: Kullanıcılar ürün adı girerek Trendyol'daki ilgili ürünleri listeleyebilir.
- **Filtreleme**: (Opsiyonel olarak eklenebilir) Fiyat, renk veya diğer filtrelerle ürünleri sıralama imkanı.

![program](https://github.com/alparslan166/trendyol-scraper/blob/main/images/program.png)
![ürünler](https://github.com/alparslan166/trendyol-scraper/blob/main/images/ürünler.png)

## Katkıda Bulunma

1. Fork yapın
2. Yeni bir özellik için branch oluşturun (`git checkout -b feature/your-feature`)
3. Yaptığınız değişiklikleri commit edin (`git commit -am 'Add new feature'`)
4. Değişiklikleri push edin (`git push origin feature/your-feature`)
5. Pull request açın

## Lisans

Bu projede **MIT Lisansı** kullanılmıştır. Daha fazla bilgi için [LICENSE](LICENSE) dosyasına bakabilirsiniz.
