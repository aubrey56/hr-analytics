SELECT strftime('%Y-%m', hire_date) AS hire_month,
       COUNT(CASE WHEN attrition = 'Yes' THEN 1 END) AS leavers
FROM hr_data
GROUP BY hire_month
ORDER BY hire_month;
