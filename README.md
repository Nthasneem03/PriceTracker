# PriceTracker
A Python script to track and notify when products on Snapdeal are available at or below a specified target price.

This project is a simple Python script that scrapes product prices from Snapdeal and checks if they meet a specified target price. If the product is available at or below the target price, the script records this in a text file.


## Features

- Monitors product prices on Snapdeal.
- Compares the current price with the target price set by the user.
- Notifies the user when the product is available at or below the target price by writing to a text file.

### Prerequisites

- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/Nthasneem03/PriceTracker.git
    cd PriceTracker
    ```

2. Install the required libraries:
   use:

    ```bash
    pip install -r requirements.txt
    ```
    or
   ```bash
   pip install bs4
   pip install requests

## Usage

1. Open the `price_tracker.py` file.

2. Add or modify the products in the `products` list, specifying their `prod_url`, `name`, and `target_price`.

3. Run the script:

    ```bash
    python price_tracker.py
    ```

4. Check the `result_file.txt` for the results.

## Code Explanation

- **`products`**: A list of dictionaries, each containing the URL, name, and target price of a product.
- **`give_product_price(url)`**: A function that takes a product URL, scrapes the webpage using `requests` and `BeautifulSoup`, and returns the current price of the product.
- **`result_file.txt`**: A text file where the results are written, indicating whether a product is available at or below the target price.

## Contributing

Feel free to contribute to this project by opening a pull request or an issue if you find any bugs or have suggestions for improvements.


## Note

You can use this script to track prices on any e-commerce website. Just inspect the product page to find the price details in the product URL and check the HTML tag containing the price when using the `find` method.
