-- ============================================================
-- Project  : Supply Chain Performance Analysis
-- Script   : queries.sql
-- Purpose  : Business SQL Queries for Supply Chain Data
-- Author   : Krishna S R
-- Date     : 2026
-- Tool     : MySQL Workbench
-- Database : supply_chain_db
-- Table    : supply_chain_data (180,519 rows)
-- ============================================================

USE supply_chain_db;

-- ============================================================
-- QUERY 1 — OVERALL BUSINESS KPIs
-- Returns total orders, revenue, profit, margin, shipping days
-- Expected : 65,752 orders | $36.78M revenue | 10.78% margin
-- ============================================================

SELECT
    COUNT(DISTINCT `Order Id`)                              AS total_orders,
    ROUND(SUM(`Sales`), 2)                                  AS total_revenue,
    ROUND(SUM(`Order Profit Per Order`), 2)                 AS total_profit,
    ROUND(
        SUM(`Order Profit Per Order`) * 100.0 / SUM(`Sales`), 2
    )                                                       AS profit_margin_pct,
    ROUND(AVG(`Days for shipping (real)`), 1)               AS avg_shipping_days,
    COUNT(DISTINCT `Customer Id`)                           AS total_customers,
    COUNT(DISTINCT `Product Name`)                          AS total_products,
    COUNT(DISTINCT `Market`)                                AS total_markets
FROM supply_chain_data;

-- ============================================================
-- QUERY 2 — DELIVERY STATUS BREAKDOWN
-- Returns count and percentage for each delivery status
-- Expected : Late delivery 54.83% (CRITICAL)
-- ============================================================

SELECT
    `Delivery Status`                                       AS delivery_status,
    COUNT(*)                                                AS order_count,
    ROUND(
        COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2
    )                                                       AS percentage
FROM supply_chain_data
GROUP BY `Delivery Status`
ORDER BY order_count DESC;

-- ============================================================
-- QUERY 3 — LATE DELIVERY RATE BY SHIPPING MODE
-- Identifies which shipping mode causes the most delays
-- Expected : First Class 95.32% (WORST) | Standard 38.07% (BEST)
-- ============================================================

SELECT
    `Shipping Mode`                                         AS shipping_mode,
    COUNT(*)                                                AS total_orders,
    SUM(
        CASE WHEN `Delivery Status` = 'Late delivery'
        THEN 1 ELSE 0 END
    )                                                       AS late_orders,
    ROUND(
        SUM(CASE WHEN `Delivery Status` = 'Late delivery'
            THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2
    )                                                       AS late_rate_pct,
    ROUND(
        SUM(CASE WHEN `Delivery Status` = 'Advance shipping'
            THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2
    )                                                       AS advance_rate_pct,
    ROUND(
        SUM(CASE WHEN `Delivery Status` = 'Shipping on time'
            THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2
    )                                                       AS ontime_rate_pct
FROM supply_chain_data
GROUP BY `Shipping Mode`
ORDER BY late_rate_pct DESC;

-- ============================================================
-- QUERY 4 — TOP 10 PROFITABLE CATEGORIES
-- Returns revenue, profit, margin, quantity per category
-- Expected : Fishing $756K profit (TOP)
-- ============================================================

SELECT
    `Category Name`                                         AS category_name,
    ROUND(SUM(`Sales`), 2)                                  AS total_revenue,
    ROUND(SUM(`Order Profit Per Order`), 2)                 AS total_profit,
    ROUND(
        SUM(`Order Profit Per Order`) * 100.0 / SUM(`Sales`), 2
    )                                                       AS profit_margin_pct,
    SUM(`Order Item Quantity`)                              AS total_qty_sold
FROM supply_chain_data
GROUP BY `Category Name`
ORDER BY total_profit DESC
LIMIT 10;

-- ============================================================
-- QUERY 5 — MONTHLY REVENUE TREND
-- Returns revenue and order count grouped by month
-- Expected : Peak Jan 2015 | Sharp drop late 2017
-- ============================================================

SELECT
    DATE_FORMAT(
        STR_TO_DATE(`order date (DateOrders)`, '%m/%d/%Y %H:%i'),
        '%Y-%m'
    )                                                       AS order_month,
    ROUND(SUM(`Sales`), 2)                                  AS monthly_revenue,
    COUNT(DISTINCT `Order Id`)                              AS total_orders,
    ROUND(SUM(`Order Profit Per Order`), 2)                 AS monthly_profit
FROM supply_chain_data
WHERE `order date (DateOrders)` IS NOT NULL
GROUP BY order_month
ORDER BY order_month ASC;

