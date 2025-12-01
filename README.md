# Trendyol Scraper

This project is a Python application developed to extract product data from **Trendyol**. Users can search for products by entering a product name and get a list of related products from Trendyol.

## Technologies

- Python 3.x
- Selenium
- WebDriver Manager

## Installation

1. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

2. We use `webdriver-manager` to automatically manage WebDriver. Make sure your WebDriver is in the correct version.

## Usage

1. Start the application by running `app.py`:
   ```bash
   python app.py
   ```

2. Once the application starts, it will list results from Trendyol based on the entered product name.

![Initial Screen](https://github.com/alparslan166/trendyol-scraper/blob/main/images/ilkEkran.jpeg)

## Features

- **Search**: Users can list related products on Trendyol by entering a product name.

![Program](https://github.com/alparslan166/trendyol-scraper/blob/main/images/program.jpeg)

- **Filtering**: (Optionally can be added) Ability to sort products by price, color, or other filters.

![Products](https://github.com/alparslan166/trendyol-scraper/blob/main/images/ürünler.jpeg)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

## License

This project uses the **MIT License**. For more information, see the [LICENSE](LICENSE) file.
