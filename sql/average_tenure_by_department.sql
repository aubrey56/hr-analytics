SELECT department, ROUND(AVG(YearsAtCompany), 2) AS avg_tenure
FROM hr_data
GROUP BY department
ORDER BY avg_tenure DESC;

