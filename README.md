# SQL Beginner Challenge #6: Group and Summarize Data with GROUP BY

**Difficulty:** Beginner  
**Estimated time:** 10–15 minutes  
**Concepts:** `GROUP BY`, aggregation, summarizing data  

This challenge introduces how to group rows and calculate summary values using the `GROUP BY` clause—one of the most important ideas in SQL.

---

## 🧠 The Problem

A product manager asks:

> “How many products do we have per category?”

Instead of counting all products together, you need to **group products by category** and calculate how many products belong to each group.

---

## 📊 Table Schema

### `products`

| Column Name | Type      | Description |
|------------|-----------|-------------|
| product_id | INTEGER   | Unique product ID |
| name       | TEXT      | Product name |
| category   | TEXT      | Product category |
| price      | DECIMAL   | Product price |
| stock_qty | INTEGER   | Units in stock |
| created_at | TIMESTAMP | Creation timestamp |

---

## 🧪 Sample Data

| product_id | name                 | category     | price  |
|-----------:|----------------------|--------------|-------:|
| 101 | Wireless Mouse      | Accessories | 24.99 |
| 102 | Mechanical Keyboard | Accessories | 89.00 |
| 103 | 27-inch Monitor     | Displays    | 229.99 |
| 104 | USB-C Hub           | Accessories | 34.50 |
| 105 | Laptop Stand        | Workspace   | 39.99 |

---

## ✅ Requirements

Your query must:

- Return one row per `category`
- Count how many products belong to each category
- Use `GROUP BY`
- Use `COUNT()` for the aggregation
- Return exactly two columns:
  - `category`
  - `total_products`

---

## ✍️ Your Task

Write a SQL query that fulfills the requirements.

```sql
-- Write your query here

