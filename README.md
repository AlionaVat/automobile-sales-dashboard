# 📊 Automobile Sales Dashboard with Interactive Analytics

## 📌 Overview

This project presents an interactive **Automobile Sales Dashboard** built using **Python, Dash, and Plotly**. It enables dynamic exploration of automobile sales data, providing insights into **yearly trends, recession impacts, vehicle category performance, and economic influences** such as unemployment rates.

Unlike static reports, this dashboard focuses on **interactive visual analytics**, allowing users to switch between different statistical views and gain deeper understanding through real-time visualizations.

---

## 🎯 Objectives

* Analyze automobile sales trends over time  
* Evaluate the impact of recession periods on sales performance  
* Compare sales across different vehicle types  
* Examine advertising expenditure distribution  
* Understand the relationship between unemployment rate and automobile sales  

---

## 🧠 Methodology

### 1. Data Collection

The dataset is sourced from IBM Cloud and includes:

* Year and Month  
* Automobile Sales  
* Vehicle Type  
* Advertising Expenditure  
* Unemployment Rate  
* Recession Indicator  

---

### 2. Data Processing

* Data is loaded using **Pandas**
* Filtered based on:
  * Selected year
  * Recession periods
* Aggregated using `groupby()` operations for visualization

---

### 3. Dashboard Design

The dashboard is built using **Dash**, enabling:

* Interactive dropdown selections  
* Dynamic updates using callbacks  
* Real-time chart rendering  

---

### 4. Visualization

Multiple visualizations are created using **Plotly Express**, including:

* Line charts  
* Bar charts  
* Pie charts  

---

## 📊 Dashboard Components

### 🔹 Recession Period Analysis

* **Line Chart:** Average automobile sales over recession years  
* **Bar Chart:** Average sales by vehicle type  
* **Pie Chart:** Advertising expenditure distribution  
* **Bar Chart:** Impact of unemployment rate on sales  

---

### 🔹 Yearly Analysis

* **Line Chart:** Year-wise automobile sales trend  
* **Line Chart:** Monthly automobile sales  
* **Bar Chart:** Vehicle type performance for selected year  
* **Pie Chart:** Advertisement expenditure by vehicle type  

---

## 📈 Why Interactive Dashboards?

Traditional static analysis provides limited insight, whereas this dashboard allows users to:

* Explore data dynamically  
* Identify trends and anomalies  
* Compare multiple dimensions in real-time  
* Gain better decision-making insights  

---

## 🧰 Technologies Used

* **Python 3**  
* **Pandas** – data manipulation  
* **Dash** – interactive web framework  
* **Plotly Express** – visualization  
* **HTML/CSS (via Dash)** – layout design  

---
