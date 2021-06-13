CREATE TABLE large_countries_2015 (
    country VARCHAR(255),
    population NUMERIC,
    fertility NUMERIC,
    continent VARCHAR(255)
);


COPY large_countries_2015 FROM '/Users/FelixAir/Desktop/SPICED/bootcamp/class_material/week_05/data/large_countries_2015.csv' DELIMITER ';' CSV HEADER NULL 'NULL'; 


encounter=# SELECT *
encounter-# FROM countries;


encounter=# SELECT * 
encounter-# FROM countries
encounter-# WHERE continent = 'Asia'
encounter-# ORDER BY fertility;

encounter=# SELECT *
encounter-# FROM countries
encounter-# WHERE country <> 'Asia' AND fertility > 2
encounter-# ;


encounter=# SELECT *
encounter-# FROM countries
encounter-# WHERE continent <> 'Asia' AND fertility > 2;


encounter=# SELECT *
encounter-# FROM countries
encounter-# WHERE fertility BETWEEN 1.4 AND 2;

encounter=# SELECT AVG(fertility), MIN(population)
encounter-# FROM countries;


encounter=# SELECT AVG(fertility) AS AVG_fertility, AVG(population) AS AVG_population
encounter-# FROM countries;


encounter=# SELECT continent, MIN(fertility), MAX(fertility), AVG(population)
encounter-# FROM countries
encounter-# GROUP BY continent;



encounter=# SELECT continent, AVG(fertility), COUNT(country)
encounter-# FROM countries
encounter-# GROUP BY continent;





SELECT continent, AVG(fertility), COUNT(countries)
FROM countries
GROUP BY continent 
HAVING AVG(fertility) > 1.7;


SELECT continent, AVG(fertility)
FROM countries
WHERE continent IN ('Asia', 'Africa', 'Europe')
GROUP BY continent
HAVING AVG(fertility) > 1.7;

SELECT continent, AVG(fertility)
FROM countries
WHERE AVG(fertility) > 1.7
GROUP BY continent;
!!! Throws an error because aggregate functions cannot be used in WHERE


!!! WHERE has to be before GROUP BY

!!! HAVING comes after GROUP BY

We want the average fertility, minimum and maximum population 
per continent
 with two conditions: 1
1. Continent name starts with ‘A
2. Average fertility < 2

SELECT continent, AVG(fertility), MIN(population), MAX(population)
FROM countries
WHERE continent LIKE 'A%'
GROUP BY continent
HAVING AVG(fertility) < 2;

SELECT continent, AVG(fertility), MIN(population), MAX(population)
FROM countries
GROUP BY continent;