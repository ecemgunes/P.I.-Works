UPDATE table_name
SET daily_vaccinations = (
  SELECT COALESCE(MEDIAN(daily_vaccinations), 0) AS median_vaccinations
  FROM table_name AS t2
  WHERE t2.country = table_name.country
  GROUP BY t2.country
)
WHERE daily_vaccinations IS NULL;