# 📊 Automobile Sales Dashboard with Interactive Analytics

## 📌 Overview

This project presents an interactive Automobile Sales Dashboard built using Python, Dash, and Plotly. It enables dynamic exploration of automobile sales data, providing insights into yearly trends, recession impacts, vehicle category performance, and economic influences such as unemployment rates.

Unlike static reports, this dashboard focuses on interactive visual analytics, allowing users to switch between different statistical views and gain deeper understanding through real-time visualizations.

---

## 🎯 Objectives

- Analyze automobile sales trends over time  
- Evaluate the impact of recession periods on sales performance  
- Compare sales across different vehicle types  
- Examine advertising expenditure distribution  
- Understand the relationship between unemployment rate and automobile sales  

---

## 🧠 Methodology

### Data Collection
The dataset is sourced from IBM Cloud and includes:
- Year and Month  
- Automobile Sales  
- Vehicle Type  
- Advertising Expenditure  
- Unemployment Rate  
- Recession Indicator  

### Data Processing
- Loaded using Pandas  
- Filtered based on user selection  
- Aggregated using groupby()  

### Dashboard Design
- Built using Dash  
- Interactive dropdowns  
- Dynamic callbacks  

### Visualization
- Line charts  
- Bar charts  
- Pie charts  

---

## 📊 Dashboard Components

### 🔹 Recession Period Analysis
- Line chart: Sales trends over years  
- Bar chart: Vehicle type comparison  
- Pie chart: Advertising expenditure  
- Bar chart: Unemployment impact  

### 🔹 Yearly Analysis
- Yearly sales trend  
- Monthly sales  
- Vehicle type performance  
- Advertisement expenditure  

---

## 🧰 Technologies Used

- Python  
- Pandas  
- Dash  
- Plotly  

---

## 📂 Project Structure

automobile-sales-dashboard/
│
├── app.py
├── requirements.txt
└── README.md

---

## ⚙️ Installation & Setup

git clone https://github.com/your-username/automobile-sales-dashboard.git  
cd automobile-sales-dashboard  
pip install -r requirements.txt  

---

## ▶️ How to Run the Project

Step 1: Check Python installation  
python --version  

Step 2: Install required libraries  
pip install dash pandas plotly  

Step 3: Run the application  
python app.py  

Step 4: Open in browser  
http://127.0.0.1:8050/  

---

## 📊 Expected Output

- Interactive dashboard with dropdown filters  
- Recession analysis charts  
- Yearly analysis charts  
- Dynamic updates  

---

## 📉 Limitations

- Limited dataset  
- No predictive modeling  
- Basic UI  

---

## 🚀 Future Improvements

- Add machine learning models  
- Improve UI/UX  
- Deploy online  
- Add more filters  

---
