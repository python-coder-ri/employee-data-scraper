# AJAX Employee Data Scraper (Selenium-based)

A Python script that uses Selenium to extract employee data from the dynamically loaded AJAX table at [DataTables.net](https://datatables.net/examples/data_sources/ajax.html).

## Features

- Automates Chrome in headless mode to access data
- Waits for dynamic AJAX content to load
- Extracts:
  - Name
  - Position
  - Office
  - Extension
  - Start Date
  - Salary
- Saves data into Excel (`.xlsx`) format

## Tech Stack

- Python
- Selenium
- WebDriver Manager
- Pandas
- OpenPyXL (for Excel export)

## Installation

Install the required packages:

```bash
pip install selenium webdriver-manager pandas openpyxl






