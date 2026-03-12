-- total flights
SELECT COUNT(*) FROM flights;

-- number of airlines
SELECT DISTINCT uniquecarrier FROM flights;

-- flights per airline
SELECT uniquecarrier, COUNT(*)
FROM flights
GROUP BY uniquecarrier
ORDER BY COUNT(*) DESC;

-- average delay per airline
SELECT uniquecarrier, AVG(arrdelay)
FROM flights
GROUP BY uniquecarrier
ORDER BY AVG(arrdelay) DESC;

-- delay by month
SELECT month, COUNT(*), AVG(arrdelay)
FROM flights
GROUP BY month
ORDER BY AVG(arrdelay) DESC;

-- delay causes
SELECT
AVG(carrierdelay),
AVG(weatherdelay),
AVG(nasdelay),
AVG(securitydelay),
AVG(lateaircraftdelay)
FROM flights;