SELECT employee_id, job_role, performance_rating, monthly_income
FROM hr_data
WHERE performance_rating = 'High'
ORDER BY monthly_income DESC
LIMIT 10;
