### QUESTION 3

SELECT 
	COUNT(*)
FROM
	green_taxi_data
WHERE
	lpep_pickup_datetime BETWEEN '2025-11-01' AND '2025-12-01' AND
	trip_distance <= 1
    
### QUESTION 4

SELECT 
	CAST(lpep_pickup_datetime AS DATE) AS "date",
	MAX(trip_distance) AS "longest"
FROM
	green_taxi_data
WHERE
	trip_distance < 100
GROUP BY
	1
ORDER BY "longest" DESC

### QUESTION 5

SELECT
    zpu."Zone",
	SUM(total_amount)
FROM
    green_taxi_data t
RIGHT JOIN
    zones zpu ON t."PULocationID" = zpu."LocationID"
JOIN
    zones zdo ON t."DOLocationID" = zdo."LocationID"
WHERE
	CAST(lpep_pickup_datetime AS DATE) = '2025-11-18'
GROUP BY
	zpu."Zone"
ORDER BY
	sum DESC