import requests
import json
from bs4 import BeautifulSoup

url = "https://market.todaypricerates.com/Tamil-Nadu-vegetables-price"

# Send an HTTP GET request to the URL
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the table containing the data
    table = soup.find("div", class_="Table")

    # Initialize an empty list to store the scraped data
    vegetable_data = []

    # Find all rows in the table
    rows = table.find_all("div", class_="Row")

    for row in rows:
        cells = row.find_all("div", class_="Cell")

        # Extract data from each cell
        vegetable_name = cells[0].text.strip()
        unit = cells[1].text.strip()
        market_price = cells[2].text.strip()
        retail_price = cells[3].text.strip()
        shopping_mall = cells[4].text.strip()

        # Create a dictionary for the current row
        vegetable_info = {
            "Vegetable Name": vegetable_name,
            "Unit": unit,
            "Market price": market_price,
            "Retail Price": retail_price,
            "Shopping Mall": shopping_mall,
        }

        # Append the dictionary to the list
        vegetable_data.append(vegetable_info)

    # Save the scraped data to a JSON file
    with open("vegetable_data.json", "w", encoding="utf-8") as json_file:
        json.dump(vegetable_data, json_file, ensure_ascii=False, indent=4)

    print("Data scraped and saved to vegetable_data.json")
else:
    print("Failed to retrieve the webpage.")


url = "https://market.todaypricerates.com/Tamil-Nadu-fruits-price"

# Send an HTTP GET request to the URL
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the table containing the data
    table = soup.find("div", class_="Table")

    # Initialize an empty list to store the scraped data
    fruits_data = []

    # Find all rows in the table
    rows = table.find_all("div", class_="Row")

    for row in rows:
        cells = row.find_all("div", class_="Cell")

        # Extract data from each cell
        fruits_name = cells[0].text.strip()
        unit = cells[1].text.strip()
        market_price = cells[2].text.strip()
        retail_price = cells[3].text.strip()
        shopping_mall = cells[4].text.strip()

        # Create a dictionary for the current row
        fruits_info = {
            "Fruits Name": fruits_name,
            "Unit": unit,
            "Market price": market_price,
            "Retail Price": retail_price,
            "Shopping Mall": shopping_mall,
        }

        # Append the dictionary to the list
        fruits_data.append(fruits_info)

    # Save the scraped data to a JSON file
    with open("Fruits_data.json", "w", encoding="utf-8") as json_file:
        json.dump(fruits_data, json_file, ensure_ascii=False, indent=4)

    print("Data scraped and saved to Fruits_data.json")
else:
    print("Failed to retrieve the webpage.")