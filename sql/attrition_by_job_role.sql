SELECT job_role,
       COUNT(CASE WHEN attrition = 'Yes' THEN 1 END) * 100.0 / COUNT(*) AS attrition_rate
FROM hr_data
GROUP BY job_role
ORDER BY attrition_rate DESC;
