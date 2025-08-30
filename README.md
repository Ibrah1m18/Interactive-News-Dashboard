# 📰 News Dashboard

## Project Description

**News Dashboard** is an interactive Python application that fetches news articles from NewsAPI based on a keyword and country. It displays the news, visualizes article distribution with Bar and Pie Charts, generates a Word Cloud from headlines, and automatically saves each search as a CSV file for further analysis.

The dashboard allows you to:

* Enter a **Keyword** and **Country** to search for news.
* Display a list of news articles (Title + Source + URL).
* Automatically save each search in a **CSV** file for each keyword + country.
* Show quick statistics: total articles, top source.
* Display **Bar Chart** and **Pie Chart** of articles per source.
* Generate a **Word Cloud** of the most common words in headlines.

---

## Requirements

* Python 3.9+
* Python libraries:

```bash
pip install streamlit pandas matplotlib wordcloud requests python-dotenv
```

* A NewsAPI key stored in a `.env` file as follows:

```
NEWS_API_KEY=47cf5113d643461987b560412f147f77
```

---

## How to Run

1. Open **Terminal / Command Prompt** in the project folder.
2. Run the dashboard using Streamlit:

```bash
git clone https://github.com/Ibrah1m18/Interactive-News-Dashboard.git
cd Interactive-News-Dashboard
pip install -r requirements.txt
streamlit run news_dashboard.py
```

3. Open the link that appears in your browser (usually [http://localhost:8501](http://localhost:8501)).
4. Enter **Keyword** and **Country**, then click **Fetch News**.
5. The dashboard will display the news articles, charts, and Word Cloud.
6. Each search will automatically save a CSV file named:

```
news_{keyword}_{country}.csv
```

---

## Project Structure

```
news_dashboard/
├── news_dashboard.py   # Main Streamlit script
├── .env                # API Key file
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation
└── (CSV files)         # Automatically saved news data
```

---

## Dashboard Preview
![Dashboard Preview](Interactive-News-Dashboard/news_dashboard_preview.pdf)

---

## Notes

* Any warnings in the console (e.g., missing ScriptRunContext) can be safely ignored.
* Make sure the `.env` file **is not uploaded to GitHub** to protect your API key.
* The code can be easily extended to add more **visualizations or statistics**.

---

## Example Usage

1. Keyword: `AI`
2. Country: `us`

The dashboard will fetch the latest news about AI in the United States, display it, and save it as:

```
news_AI_us.csv
```

---

## License

MIT License
