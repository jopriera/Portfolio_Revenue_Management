# Portfolio Revenue Management  
**Josep Riera Querol** – Revenue Analyst | Power BI Specialist | MBA BI & Big Data  

> This repository showcases six end-to-end revenue management BI projects using real and synthetic hotel data. Each folder contains raw data, scripts, queries, dashboards, and documentation.  

---  

## 🚀 Table of Contents  
1. [Folder Structure](#folder-structure)  
2. [Projects Overview](#projects-overview)  
3. [Prerequisites](#prerequisites)  
4. [Installation & Reproduction](#installation--reproduction)  
5. [Skills Demonstrated](#skills-demonstrated)  
6. [Contact & Links](#contact--links)  

---  

## 📁 Folder Structure  

Portfolio_Revenue_Management/
├── 01_Raw_Data/ # Raw and synthetic datasets
├── 02_Python_Scripts/ # Data generation, cleaning, analysis
├── 03_SQL_Queries/ # Schema creation & analysis queries
├── 04_PowerBI_Files/ # .pbix dashboards
├── 05_Tableau_Public/ # .twb workbooks for competitive analysis
└── 06_Documentation/ # Screenshots, methodology, summaries


---  

## 📊 Projects Overview  
1. **Dashboard Revenue Management**  
   - Visualize ADR, length of stay, cancellation rate, segment filters  
2. **Forecasting Estacional**  
   - Predict occupancy and ADR trends with time-series models  
3. **Channel Management**  
   - Compare booking channels (OTA vs direct) performance  
4. **F&B Revenue Analysis**  
   - Analyze restaurant and event revenues  
5. **Competitive Benchmarking**  
   - Benchmark against industry peers using STR data  
6. **Customer Analytics**  
   - Perform RFM and loyalty profiling  

Each project folder contains a detailed `README.md` with goals, data sources, usage steps, and key insights.  

---  

## ⚙️ Prerequisites  
- **Power BI Desktop** (Windows)  
- **Python 3.10+** (Anaconda distribution recommended)  
- **SQLite** (or SQL Server Express on Windows)  
- **Git** & **GitHub CLI**  

Create Python environment
conda create -n rm_portfolio python=3.10 -y
conda activate rm_portfolio

Install libraries
pip install pandas numpy sdv faker matplotlib seaborn plotly scikit-learn sqlalchemy jupyter

---  

## 🚩 Installation & Reproduction  

1. Clone repository
git clone https://github.com/jopriera/Portfolio_Revenue_Management.git
cd Portfolio_Revenue_Management

2. Place raw datasets in 01_Raw_Data/ (download from Kaggle or generate synthetic)
3. (Optional) Generate synthetic data
python 02_Python_Scripts/data_generation.py

4. Clean and prepare data
python 02_Python_Scripts/data_cleaning.py

5. Load into SQLite
python 02_Python_Scripts/load_to_sqlite.py

6. Run exploratory analysis
python 02_Python_Scripts/analysis.py

7. Open Power BI dashboard
04_PowerBI_Files/Portfolio_Hotel_Revenue_Management_Dashboard_JosepRiera.pbix


---  

## 🛠 Skills Demonstrated  
- **Python**: pandas, SDV synthetic data, data cleaning, forecasting  
- **SQL**: database schema design, complex queries (SQLite)  
- **Power BI**: data modeling, DAX measures, interactive dashboards  
- **Data Visualization**: matplotlib, seaborn, plotly, Tableau Public  

---  

## 📬 Contact & Links  
- LinkedIn: https://www.linkedin.com/in/jrieraq/  
- Email: joseprieraq@gmail.com 
- IBM Coursera Certificates: https://www.coursera.org/jopriera  

---  
