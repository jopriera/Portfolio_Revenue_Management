# Portfolio Revenue Management
**Josep Riera Querol** – Revenue Analyst | Power BI Specialist | MBA BI & Big Data

> This repository showcases six end-to-end revenue management BI projects using real and synthetic hotel data. Each folder contains raw data, scripts, queries, dashboards, and documentation.

---

## Table of Contents
1. [Folder Structure](#folder-structure)
2. [Projects Overview](#projects-overview)
3. [Prerequisites](#prerequisites)
4. [Installation & Reproduction](#installation--reproduction)
5. [Testing & Coverage](#testing--coverage)
6. [Skills Demonstrated](#skills-demonstrated)
7. [Contact & Links](#contact--links)

---

## Folder Structure

```Portfolio_Revenue_Management/
├── 01_Raw_Data/             # Raw and synthetic datasets
├── 02_Python_Scripts/       # Data generation, cleaning, analysis, forecasting scripts
├── 03_SQL_Queries/          # Schema creation & analysis queries
├── 04_PowerBI_Files/        # .pbix dashboards
├── 05_Tableau_Public/       # .twb workbooks for competitive analysis
└── 06_Documentation/        # Screenshots, methodology, summaries
```

---

## Projects Overview
1. **Dashboard Revenue Management**  - Visualize ADR, length of stay, cancellation rate, segment filters
2. **Forecasting Estacional**       - Predict occupancy and ADR trends with time-series models
3. **Channel Management**           - Compare booking channels (OTA vs direct) performance
4. **F&B Revenue Analysis**         - Analyze restaurant and event revenues
5. **Competitive Benchmarking**     - Benchmark against industry peers using STR data
6. **Customer Analytics**           - Perform RFM and loyalty profiling

Each project folder contains a detailed `README.md` with goals, data sources, usage steps, and key insights.

---

## Prerequisites
- **Power BI Desktop** (Windows)
- **Python 3.10+** (Anaconda distribution recommended)
- **SQLite** (or SQL Server Express on Windows)
- **Git** & **GitHub CLI**

```bash
conda create -n rm_portfolio python=3.10 -y
conda activate rm_portfolio
``` 

---

## Installation & Reproduction
1. Clone repository
```bash
git clone https://github.com/jopriera/Portfolio_Revenue_Management.git
cd Portfolio_Revenue_Management
```

2. Install libraries
```bash
pip install -r common/requirements.txt
```

3. Run Forecasting Estacional example
```bash
pytest --cov=Projects/02_Forecasting_Estacional/02_Python_Scripts -v
coverage html -d htmlcov
open htmlcov/index.html
```

---

## Testing & Coverage
Run all tests with coverage:
```bash
pytest --cov=Projects/02_Forecasting_Estacional/02_Python_Scripts -v
```

Generate HTML coverage report:
```bash
coverage html -d htmlcov
open htmlcov/index.html
```

Install testing dependencies:
```bash
pip install pytest pytest-mock pytest-cov
```

---

## 🛠 Skills Demonstrated
- **Python**: pandas, scikit-learn, prophet, data cleaning, forecasting  
- **SQL**: database schema design, complex queries  
- **Power BI**: data modeling, DAX measures, interactive dashboards  
- **Data Visualization**: matplotlib, seaborn, plotly, Tableau Public

---

## 📬 Contact & Links
- LinkedIn: [linkedin.com/in/jrieraq](https://linkedin.com/in/jrieraq)  
- Email: joseprieraq@gmail.com  
- IBM Coursera Certificates: [coursera.org/learner/josep-riera](https://coursera.org/learner/josep-riera)