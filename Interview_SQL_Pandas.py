#1. Find Total Number of Employees in Each Department
#SQL:

SELECT department_id, COUNT(*) AS employee_count
FROM employees
GROUP BY department_id;

#Pandas:
employee_count_by_department = employees.groupby('department_id').size().reset_index(name='employee_count')

#2. Calculate Moving Average for Sales
#SQL:

SELECT date, sales,
AVG(sales) OVER (ORDER BY date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS moving_average
FROM sales_table;

#Pandas:

sales_table['moving_average'] = sales_table['sales'].rolling(window=7).mean()

#3. Find the Most Recent Sale for Each Product
#SQL:

SELECT product_id, MAX(sale_date) AS most_recent_sale
FROM sales
GROUP BY product_id;

#Pandas:

most_recent_sale = sales.groupby('product_id')['sale_date'].max().reset_index(name='most_recent_sale')

#4. Calculate the Difference Between Current and Previous Rows
#SQL:


SELECT id, value,
value - LAG(value) OVER (ORDER BY id) AS difference
FROM your_table;

#Pandas:

your_table['difference'] = your_table['value'].diff()


#5. Find Employees with the Lowest Salary in Each Department
#SQL:

WITH department_salaries AS (
SELECT department_id, MIN(salary) AS min_salary
FROM employees
GROUP BY department_id
)
SELECT e.*
FROM employees e
JOIN department_salaries ds ON e.department_id = ds.department_id AND e.salary = ds.min_salary;

#Pandas:

min_salary_by_department = employees.groupby('department_id')['salary'].min().reset_index()
employees_with_lowest_salary = employees.merge(min_salary_by_department, on=['department_id', 'salary'])

#6. Calculate Yearly Sales Growth
#SQL:

SELECT EXTRACT(YEAR FROM sale_date) AS year,
SUM(sales) AS total_sales,
LAG(SUM(sales)) OVER (ORDER BY EXTRACT(YEAR FROM sale_date)) AS previous_year_sales,
(SUM(sales) - LAG(SUM(sales)) OVER (ORDER BY EXTRACT(YEAR FROM sale_date))) / LAG(SUM(sales)) OVER (ORDER BY EXTRACT(YEAR FROM sale_date)) * 100 AS sales_growth
FROM sales_table
GROUP BY EXTRACT(YEAR FROM sale_date);

#Pandas:

sales_table['year'] = sales_table['sale_date'].dt.year
yearly_sales = sales_table.groupby('year')['sales'].sum()
yearly_sales_growth = (yearly_sales - yearly_sales.shift()) / yearly_sales.shift() * 100

#7. Identify the Top 5 Products by Revenue
#SQL:

SELECT product_id, SUM(revenue) AS total_revenue
FROM sales
GROUP BY product_id
ORDER BY total_revenue DESC
LIMIT 5;

#Pandas:
top_5_products = sales.groupby('product_id')['revenue'].sum().nlargest(5)
