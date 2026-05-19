# Google Search Analysis with Python

## 📌 Project Overview
This project analyzes Google search trends using Python and the PyTrends library. It helps in understanding:
- Top countries searching for a keyword
- Search trends over time
- Keyword comparison analysis
- World map visualization of search interest

Google Trends data acts as a reliable source for analyzing public interest and market trends.

---

## 🚀 Features
- Search trend analysis for any keyword
- Top 15 countries visualization
- Interactive world map using Plotly
- Time-series trend analysis
- Multiple keyword comparison

---

## 🛠️ Technologies Used
- Python
- Pandas
- Matplotlib
- Seaborn
- Plotly
- PyTrends

---

## 📦 Installation

Install all required libraries:

```bash
pip install pytrends pandas matplotlib seaborn plotly
```

---

## 📂 Project Structure

```bash
├── solve_data.py
├── README.md
└── requirements.txt
```

---

## ▶️ How to Run the Project

Run the Python file:

```bash
python solve_data.py
```

---

## 📊 Functionalities

### 1. Keyword Search Analysis
You can change the keyword directly in the script:

```python
keyword = "cloud computing"
```

---

### 2. Top Countries Analysis
Displays the top 15 countries searching for the selected keyword using a bar chart.

---

### 3. World Map Visualization
Creates an interactive choropleth map showing worldwide search interest.

---

### 4. Time-wise Trend Analysis
Analyzes how the keyword trend changes over time.

---

### 5. Multiple Keyword Comparison
Compare multiple keywords together:

```python
kw_list = ["cloud computing", "data science", "machine learning"]
```

---

## 📷 Output
The project generates:
- Bar Plot of Top Countries
- World Map Visualization
- Search Trend Line Graph
- Multiple Keyword Comparison Graph

---

## 📌 Sample Code

```python
from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360)

keyword = "cloud computing"

pytrends.build_payload([keyword], timeframe='today 12-m')

data = pytrends.interest_over_time()

print(data.head())
```

---

## 📈 Use Cases
- Market Research
- SEO Keyword Analysis
- Trend Forecasting
- Competitive Analysis
- Public Interest Analysis

---

## 👨‍💻 Author
Shreya Srivastava

---

## 📜 License
This project is created for educational and learning purposes only.