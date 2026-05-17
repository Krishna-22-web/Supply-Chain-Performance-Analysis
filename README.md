\# 🚚 Supply Chain Performance Analysis



<div align="center">



!\[Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge\&logo=powerbi\&logoColor=black)

!\[Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)

!\[MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge\&logo=mysql\&logoColor=white)

!\[VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge\&logo=visualstudiocode\&logoColor=white)



\*\*A comprehensive end-to-end data analytics project analyzing 180,519 supply chain transactions\*\*

\*\*from the DataCo SMART Supply Chain dataset · January 2015 – January 2018\*\*



\[📊 Dashboard Pages](#6--dashboard-pages) · \[🔑 Key Findings](#7--key-findings) · \[💡 Recommendations](#9--business-recommendations) · \[👤 Author](#10--author--data-source)



</div>



\---



\## 📋 Table of Contents



1\. \[Project Overview](#1--project-overview)

2\. \[Tools \& Technologies](#2-️-tools--technologies)

3\. \[Dataset Details](#3--dataset-details)

4\. \[Project Workflow](#4--project-workflow)

5\. \[Dashboard Screenshots](#5--dashboard-screenshots)

6\. \[Dashboard Pages](#6--dashboard-pages)

7\. \[Key Findings](#7--key-findings)

8\. \[Confusions Clarified](#8--confusions-clarified)

9\. \[Business Recommendations](#9--business-recommendations)

10\. \[Author \& Data Source](#10--author--data-source)



\---



\## 1. 📌 Project Overview



This project is a \*\*complete end-to-end data analytics solution\*\* built to uncover critical supply chain performance issues in a global company's operations.



\### What Was Built

A \*\*5-page interactive Power BI dashboard\*\* that analyzes delivery performance, product profitability, and regional revenue trends — powered by Python data cleaning, MySQL SQL analysis, and 21 custom DAX measures.



\### Why It Was Built

> Over \*\*54% of orders are delivered late\*\*. This project identifies where the problem is, how severe it is, which shipping modes are responsible, and what business actions should be taken.



\### What It Demonstrates

\- ✅ End-to-end data analytics workflow

\- ✅ Data cleaning \& normalization with Python

\- ✅ SQL business query writing with MySQL

\- ✅ Advanced Power BI dashboard development

\- ✅ DAX measure creation (21 measures)

\- ✅ Business insight generation \& recommendations



\---



\## 2. 🛠️ Tools \& Technologies



| Tool | Purpose |

|------|---------|

| \*\*Python\*\* | Data cleaning, EDA, chart generation |

| \*\*MySQL Workbench\*\* | Database storage + 5 SQL business queries |

| \*\*Power BI Desktop\*\* | Interactive 5-page dashboard \& 21 DAX measures |

| \*\*VS Code\*\* | Python development environment |



\### Python Libraries Used

```

pandas · matplotlib · seaborn · sqlalchemy

```



\---



\## 3. 📦 Dataset Details



| Detail | Value |

|--------|-------|

| \*\*Name\*\* | DataCo SMART Supply Chain Dataset |

| \*\*Source\*\* | Kaggle |

| \*\*File\*\* | `supply\_chain\_data.csv` |

| \*\*Total Rows\*\* | 180,519 |

| \*\*Unique Orders\*\* | 65,752 |

| \*\*Columns\*\* | 53 |

| \*\*Period\*\* | January 2015 – January 2018 |

| \*\*Markets\*\* | 5 (Africa, Europe, LATAM, Pacific Asia, USCA) |

| \*\*Countries\*\* | 164 |

| \*\*Unique Products\*\* | 118 |

| \*\*Unique Customers\*\* | 20,652 |



\---



\## 4. 🔄 Project Workflow



```

┌─────────────────────────────────────────────────────┐

│         DataCo SMART Supply Chain CSV (Kaggle)       │

│                   180,519 rows                       │

└──────────────────────┬──────────────────────────────┘

&#x20;                      │

&#x20;                      ▼

┌─────────────────────────────────────────────────────┐

│                Python Data Cleaning                  │

│  • Removed: Email, Password, Description, Image     │

│  • Fixed date column formats                        │

│  • Filled missing zipcode values                    │

│  • Removed duplicate rows                           │

│  • Generated 5 EDA charts                           │

│  • Saved cleaned CSV for Power BI                   │

└──────────────────────┬──────────────────────────────┘

&#x20;                      │

&#x20;         ┌────────────┴────────────┐

&#x20;         ▼                         ▼

┌──────────────────┐    ┌──────────────────────────┐

│  MySQL Workbench │    │     Cleaned CSV           │

│  5 SQL Queries   │    │   → Power BI Import       │

└──────────────────┘    └──────────────────────────┘

&#x20;                              │

&#x20;                              ▼

┌─────────────────────────────────────────────────────┐

│               Power BI Dashboard                     │

│         5 Pages · 21 DAX Measures                   │

│   Home · Executive · Delivery · Product · Regional  │

└─────────────────────────────────────────────────────┘

```



\### 📁 Project Folder Structure



```

Supply-Chain-Performance-Analysis/

│

├── data/

│   └── supply\_chain\_cleaned.csv       ← Python cleaned dataset

│

├── python/

│   ├── load\_data.py                   ← Loads CSV to MySQL

│   └── eda\_analysis.py                ← EDA + 5 chart generation

│

├── sql/

│   └── queries.sql                    ← 5 business SQL queries

│

├── Outputs/

│   ├── chart1\_delivery\_status.png

│   ├── chart2\_late\_shipping.png

│   ├── chart3\_top\_categories.png

│   ├── chart4\_monthly\_trend.png

│   └── chart5\_regional.png

│

├── powerbi/

│   └── supply\_chain\_dashboard.pbix    ← Power BI dashboard file

│

├── screenshots/

│   ├── home.png

│   ├── executive\_summary.png

│   ├── delivery\_analysis.png

│   ├── product\_performance.png

│   └── regional\_analysis.png

│

└── README.md

```



\---



\## 5. 📸 Dashboard Screenshots



\### 🏠 Home Page

!\[Home Page](screenshots/home.png)



\---



\### 📊 Executive Summary

!\[Executive Summary](screenshots/executive\_summary.png)



\---



\### 🚚 Delivery Analysis

!\[Delivery Analysis](screenshots/delivery\_analysis.png)



\---



\### 📦 Product Performance

!\[Product Performance](screenshots/product\_performance.png)



\---



\### 🌍 Regional Analysis

!\[Regional Analysis](screenshots/regional\_analysis.png)



\---



\## 6. 📊 Dashboard Pages



\### 🏠 Page 0 — Home Navigation



| Section | Content |

|---------|---------|

| \*\*Header\*\* | SUPPLY CHAIN PERFORMANCE ANALYSIS |

| \*\*Info Boxes\*\* | Dataset · Tools Used · Analysis · Author |

| \*\*Navigation\*\* | 4 clickable arrow buttons → each dashboard page |

| \*\*Key Findings\*\* | 6 critical business insights |

| \*\*Footer\*\* | Author + Tools + Dataset credits |



\---



\### 📊 Page 1 — Executive Summary



\*\*KPI Cards\*\*



| Metric | Value |

|--------|-------|

| Total Orders | \*\*66K\*\* |

| Total Revenue | \*\*$36.78M\*\* |

| Total Profit | \*\*$3.97M\*\* |

| Late Delivery % | \*\*54.83%\*\* 🔴 |



\*\*Charts\*\*



| Chart | Type | Insight |

|-------|------|---------|

| Delivery Status Distribution | Donut | 4 delivery status categories |

| Late Delivery % by Shipping Mode | Horizontal Bar | First Class = 95.32% late |

| Revenue by Region | Treemap | Western Europe leads at $5.89M |

| Monthly Revenue Trend | Line | Revenue peaks Jan, dips Nov-Dec |



\---



\### 🚚 Page 2 — Delivery Analysis



\*\*KPI Cards\*\*



| Metric | Value |

|--------|-------|

| On Time Rate % | \*\*40.88%\*\* |

| Total Late Orders | \*\*99K\*\* |

| Avg Shipping Days | \*\*3.50\*\* |

| Early Delivery % | \*\*23.04%\*\* |



\*\*Charts\*\*



| Chart | Type | Insight |

|-------|------|---------|

| Orders by Shipping Mode + Status | Stacked Bar | Standard Class = most orders |

| Monthly Orders by Delivery Status | Stacked Column | Consistent late trend monthly |

| Shipping Mode vs Delivery Status | Matrix Table | First Class: 0 on-time/early rows |

| Avg Shipping Delay Days | Waterfall | Advance shipping saves 1.5 days |



\---



\### 📦 Page 3 — Product Performance



\*\*KPI Cards\*\*



| Metric | Value |

|--------|-------|

| Total Products | \*\*118\*\* |

| Avg Profit Per Item | \*\*$21.97\*\* |

| Profit Margin % | \*\*10.78%\*\* |

| Total Quantity Sold | \*\*384K\*\* |



\*\*Charts\*\*



| Chart | Type | Insight |

|-------|------|---------|

| Revenue Trend — Top 5 Categories | Area | Fishing leads 2015–2017 |

| Top 5 Categories by Total Profit | Horizontal Bar | Fishing = $760K profit |

| Product Category Performance | Table | Full detail + conditional formatting |

| Profit Margin % by Category | Column | Consistent \~10–11% across all |



\---



\### 🌍 Page 4 — Regional Analysis



\*\*KPI Cards\*\*



| Metric | Value |

|--------|-------|

| Total Markets | \*\*5\*\* |

| Total Countries | \*\*164\*\* |

| Revenue per Customer | \*\*$1.78K\*\* |

| Total Customers | \*\*21K\*\* |



\*\*Interactive Slicer:\*\* Filter by Market — Africa · Europe · LATAM · Pacific Asia · USCA



\*\*Charts\*\*



| Chart | Type | Insight |

|-------|------|---------|

| Revenue by Country | World Map | Dense in Europe + LATAM |

| Revenue Trend by Market | Line | Europe + LATAM dominate |

| Top 5 Regions by Revenue | Horizontal Bar | W. Europe $5.89M · C. America $5.67M |



\---



\### 📐 DAX Measures (21 Total)



<details>

<summary><strong>Click to expand — Basic KPI Measures (1–5)</strong></summary>



```dax

\-- 1. Total Orders

Total Orders = DISTINCTCOUNT('supply\_chain\_cleaned'\[Order Id])



\-- 2. Total Revenue

Total Revenue = SUM('supply\_chain\_cleaned'\[Sales])



\-- 3. Total Profit

Total Profit = SUM('supply\_chain\_cleaned'\[Order Profit Per Order])



\-- 4. Total Customers

Total Customers = DISTINCTCOUNT('supply\_chain\_cleaned'\[Customer Id])



\-- 5. Total Products

Total Products = DISTINCTCOUNT('supply\_chain\_cleaned'\[Product Name])

```

</details>



<details>

<summary><strong>Click to expand — Delivery Measures (6–12)</strong></summary>



```dax

\-- 6. Late Delivery %

Late Delivery % =

DIVIDE(

&#x20;   CALCULATE(COUNTROWS('supply\_chain\_cleaned'),

&#x20;       'supply\_chain\_cleaned'\[Delivery Status] = "Late delivery"),

&#x20;   COUNTROWS('supply\_chain\_cleaned')

) \* 100



\-- 7. On Time Rate % (Shipping on time + Advance shipping)

On Time Rate % =

DIVIDE(

&#x20;   CALCULATE(COUNTROWS('supply\_chain\_cleaned'),

&#x20;       'supply\_chain\_cleaned'\[Delivery Status] IN

&#x20;       {"Shipping on time", "Advance shipping"}),

&#x20;   COUNTROWS('supply\_chain\_cleaned')

) \* 100



\-- 8. Early Delivery %

Early Delivery % =

DIVIDE(

&#x20;   CALCULATE(COUNTROWS('supply\_chain\_cleaned'),

&#x20;       'supply\_chain\_cleaned'\[Delivery Status] = "Advance shipping"),

&#x20;   COUNTROWS('supply\_chain\_cleaned')

) \* 100



\-- 9. Total Late Orders

Total Late Orders =

CALCULATE(COUNTROWS('supply\_chain\_cleaned'),

&#x20;   'supply\_chain\_cleaned'\[Delivery Status] = "Late delivery")



\-- 10. Avg Shipping Days

Avg Shipping Days = AVERAGE('supply\_chain\_cleaned'\[Days for shipping (real)])



\-- 11. Shipping Delay Days

Shipping Delay Days =

AVERAGEX('supply\_chain\_cleaned',

&#x20;   'supply\_chain\_cleaned'\[Days for shipping (real)] -

&#x20;   'supply\_chain\_cleaned'\[Days for shipment (scheduled)])



\-- 12. Early Delivery Count

Early Delivery Count =

CALCULATE(COUNTROWS('supply\_chain\_cleaned'),

&#x20;   'supply\_chain\_cleaned'\[Delivery Status] = "Advance shipping")

```

</details>



<details>

<summary><strong>Click to expand — Product Measures (13–15)</strong></summary>



```dax

\-- 13. Profit Margin %

Profit Margin % =

DIVIDE(SUM('supply\_chain\_cleaned'\[Order Profit Per Order]),

&#x20;      SUM('supply\_chain\_cleaned'\[Sales])) \* 100



\-- 14. Avg Profit Per Item

Avg Profit Per Item = AVERAGE('supply\_chain\_cleaned'\[Order Profit Per Order])



\-- 15. Total Quantity Sold

Total Qty Sold = SUM('supply\_chain\_cleaned'\[Order Item Quantity])

```

</details>



<details>

<summary><strong>Click to expand — Regional \& Utility Measures (16–21)</strong></summary>



```dax

\-- 16. Revenue per Customer

Revenue per Customer =

DIVIDE(SUM('supply\_chain\_cleaned'\[Sales]),

&#x20;      DISTINCTCOUNT('supply\_chain\_cleaned'\[Customer Id]))



\-- 17. Total Markets

Total Markets = DISTINCTCOUNT('supply\_chain\_cleaned'\[Market])



\-- 18. Total Countries

Total Countries = DISTINCTCOUNT('supply\_chain\_cleaned'\[Order Country])



\-- 19. Order Row Count

Order Row Count = COUNTROWS('supply\_chain\_cleaned')



\-- 20. Revenue in Millions

Revenue M = DIVIDE(SUM('supply\_chain\_cleaned'\[Sales]), 1000000)



\-- 21. Profit in Millions

Profit M = DIVIDE(SUM('supply\_chain\_cleaned'\[Order Profit Per Order]), 1000000)

```

</details>



\---



\## 7. 🔑 Key Findings



| # | Finding | Value | Status |

|---|---------|-------|--------|

| 1 | Overall late delivery rate | \*\*54.83%\*\* | 🔴 Critical |

| 2 | First Class late delivery rate | \*\*95.32%\*\* | 🔴 Worst performer |

| 3 | Standard Class late delivery rate | \*\*38.07%\*\* | 🟢 Best performer |

| 4 | Combined on time rate (on time + early) | \*\*40.88%\*\* | 🟡 Note |

| 5 | Most profitable product category | \*\*Fishing — $760K\*\* | 🟡 Insight |

| 6 | Highest revenue region | \*\*Western Europe — $5.89M\*\* | 🟡 Insight |

| 7 | First Class on-time or early orders | \*\*0%\*\* | 🔴 Critical |

| 8 | Only Standard Class has advance shipping | \*\*Unique to Standard\*\* | 🟡 Insight |

| 9 | Profit margin consistency | \*\*\~10.78% all categories\*\* | ✅ Stable |

| 10 | Global operational reach | \*\*5 markets · 164 countries\*\* | ✅ Scale |



\### Delivery Status Breakdown



| Status | Row Count | Percentage |

|--------|-----------|-----------|

| Late delivery | \~99,000 | \*\*54.83%\*\* |

| Advance shipping | \~42,000 | \*\*23.04%\*\* |

| Shipping on time | \~32,000 | \*\*17.84%\*\* |

| Shipping canceled | \~8,000 | \*\*4.34%\*\* |

| \*\*Total\*\* | \*\*180,519\*\* | \*\*100%\*\* |



\---



\## 8. 🤔 Confusions Clarified



<details>

<summary><strong>❓ Why does the matrix table show 49,170 but KPI shows 66K orders?</strong></summary>



The matrix table shows unique orders per delivery status combination. Since one order can contain items with different delivery statuses, DISTINCTCOUNT removes cross-status duplicates giving 49,170. The KPI card shows 66K total unique Order IDs across all statuses.



> ✅ This is not an error — it reflects multi-item order complexity in the data.



</details>



<details>

<summary><strong>❓ On Time Rate shows 40.88% but delivery status shows only 17.84% "Shipping on time" — why?</strong></summary>



On Time Rate % includes TWO delivery status categories:

\- `Shipping on time` = 17.84%

\- `Advance shipping` (early delivery) = 23.04%

\- \*\*Combined On Time Rate = 40.88%\*\*



> ✅ Early delivery IS successful on-time delivery. The combined rate of 40.88% is the correct business KPI.



</details>



<details>

<summary><strong>❓ Late Delivery shows 54.83% but Total Late Orders shows 99K — aren't these contradicting?</strong></summary>



These measure different things:

\- \*\*54.83%\*\* = Late rows ÷ Total rows × 100 (percentage)

\- \*\*99K\*\* = Total late order rows counted by COUNTROWS



> ✅ Both values are correct — they answer different analytical questions. Percentages use row-level calculation for accuracy.



</details>



<details>

<summary><strong>❓ Why use COUNTROWS for delivery % but DISTINCTCOUNT for Total Orders?</strong></summary>



| Measure | Method | Value | Reason |

|---------|--------|-------|--------|

| Total Orders | DISTINCTCOUNT | 66K | Count unique order IDs |

| Late Delivery % | COUNTROWS | 54.83% | Item-level row accuracy |

| On Time Rate % | COUNTROWS | 40.88% | Item-level row accuracy |

| Total Late Orders | COUNTROWS | 99K | Count all late rows |

| Total Revenue | SUM | $36.78M | Sum all sales values |



> ✅ One order contains multiple product rows. COUNTROWS gives item-level accuracy for delivery percentages, while DISTINCTCOUNT gives unique order counts.



</details>



<details>

<summary><strong>❓ Why does First Class show blank for Advance and On Time in the matrix table?</strong></summary>



This is real data — First Class shipping mode genuinely has:

\- \*\*0\*\* advance shipping orders

\- \*\*0\*\* on-time orders

\- Only Late delivery and Shipping canceled statuses



> ✅ Blank cells mean those combinations do not exist in the dataset. This confirms First Class is the worst performing shipping mode.



</details>



\---



\## 9. 💡 Business Recommendations



| # | Priority | Recommendation | Action |

|---|----------|---------------|--------|

| 1 | 🔴 HIGH | \*\*Fix First Class Shipping\*\* | Investigate 95.32% late rate. Switch high-value orders to Standard Class immediately. |

| 2 | 🔴 HIGH | \*\*Scale Standard Class\*\* | Only mode with advance shipping and lowest late rate (38.07%). Prioritize and expand capacity. |

| 3 | 🟡 MED | \*\*Expand Fishing Category\*\* | Highest profit at $760K with only 17,325 orders. Significant untapped growth potential. |

| 4 | 🟡 MED | \*\*Focus on Top Markets\*\* | Western Europe ($5.89M) + Central America ($5.67M) = $11.56M combined. Increase investment. |

| 5 | 🟡 MED | \*\*Investigate 2017 Revenue Drop\*\* | Nov: $2.70M → Dec: $2.60M sharp decline. Identify if seasonal or operational issue. |

| 6 | 🟢 LOW | \*\*Build Delivery Monitoring System\*\* | Real-time tracking to reduce 54.83% late rate. Target: below 30% within 12 months. |



\---



\## 10. 👤 Author \& Data Source



\### Author



\*\*Krishna S R\*\*

Data Analyst · 2026



> \*Built to demonstrate end-to-end data analytics skills — from raw data to actionable business insights.\*



\---



\### Data Source



\*\*DataCo SMART Supply Chain for Big Data Analysis\*\*



| Detail | Info |

|--------|------|

| \*\*Platform\*\* | Kaggle |

| \*\*Original Authors\*\* | Fabian Constante, Francisco Miranda, Antonios Antoniadis |

| \*\*Description\*\* | Real supply chain transactions from a global company |



\---



\### 📄 License



This project is for \*\*educational and portfolio purposes only.\*\*

Dataset used under Kaggle's open dataset terms.



\---



<div align="center">



\*\*⭐ If you found this project useful, please consider starring the repository!\*\*



\*Built with ❤️ using Python · MySQL · Power BI · VS Code\*



</div>

