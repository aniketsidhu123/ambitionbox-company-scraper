# AmbitionBox Company Scraper

A Python web scraping project that extracts company information from AmbitionBox using **Requests**, **BeautifulSoup**, and **Pandas**. The scraper automatically navigates through multiple pages, collects company details, and exports the data into a structured CSV file for analysis.

---

## Features

- Scrapes multiple pages automatically
- Extracts company information including:
  - Company Name
  - Company Rating
  - Number of Reviews
  - Company Type
  - Headquarters
  - Highly Rated For
  - Critically Rated For
- Stores the scraped data in a Pandas DataFrame
- Exports the data to CSV

---

## Tech Stack

- Python
- Requests
- BeautifulSoup4
- Pandas
- lxml

---

## Project Structure

```
ambitionbox-company-scraper/
│
├── ambitionbox-company-scraper.ipynb
├── ambitionbox_companies.csv
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/aniketsidhu123/ambitionbox-company-scraper.git
```

Navigate to the project directory:

```bash
cd ambitionbox-company-scraper
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## Usage

Open the Jupyter Notebook and run all cells:

```bash
jupyter notebook
```

The scraper will scrape multiple pages from AmbitionBox and generate:

```
ambitionbox_companies.csv
```

---

## Sample Output

| Company Name | Rating | Reviews | Company Type | Headquarters |
|--------------|--------|----------|--------------|--------------|
| Example Company | 4.3 | 12.5k Reviews | IT Services | Bengaluru |

---

## Libraries Used

- requests
- beautifulsoup4
- pandas
- lxml
- openpyxl

---

## Disclaimer

This project is created for educational purposes to demonstrate web scraping using Python. Please ensure your usage complies with AmbitionBox's Terms of Service and applicable laws.

---

## Author

**Aniket Sidhu**

- GitHub: https://github.com/aniketsidhu123
- LinkedIn: https://linkedin.com/in/aniket-sidhu-9bb180373
