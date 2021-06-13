JOINING TABLES 

SELECT singer.name AS singer_name, song.name AS song_name
FROM singer
JOIN song
ON singer.id = song.singer_id;

 singer_name |  song_name  
-------------+-------------
 Nicky Minaj | Anaconda
 Lady Gaga   | Paparazzi
 Lady Gaga   | Bad Romance
 Tom Jones   | Sex Bomb
(4 rows)


SAVING A VIEW

CREATE VIEW sales_by_customer_temp AS SELECT
orders."customerID", sum(order_details."unitPrice") AS sales_by_customer
FROM orders
JOIN order_details ON
orders."orderID" = order_details."orderID"
GROUP BY orders."customerID"
ORDER BY sales_by_customer DESC;

TO CALL THE VIEW:

northwind=# SELECT * FROM sales_by_customer_temp;
 customerID | sales_by_customer 
------------+-------------------
 QUICK      |           2739.95
 SAVEA      |           2679.66
 ERNSH      |           2666.67
 RATTC      |           2182.90
 HUNGO      |           1719.86
 BERGS      |           1425.65
 HANAR      |           1396.10
 WHITC      |           1278.33
 KOENE      |           1229.24




SHORTEN YOUR STATEMENTS

SELECT o."customerID", sum(od."unitPrice") AS sales_by_customer
FROM orders AS o
JOIN order_details as od
ON od."orderID" = od."orderID"
GROUP BY o."customerID"
ORDER BY sales_by_customer DESC
LIMIT 50;

customerID | sales_by_customer 
------------+-------------------
 SAVEA      |        1751528.21
 ERNSH      |        1695027.30
 QUICK      |        1582025.48
 HUNGO      |        1073517.29
 FOLKO      |        1073517.29
 BERGS      |        1017016.38
 HILAA      |        1017016.38
 RATTC      |        1017016.38
 BONAP      |         960515.47








CREATE VIEW test AS SELECT orders."customerID", order_details.unitPrice
FROM orders
LEFT JOIN order_details ON
orders."orderID" = "orderDetails".orderID
ORDER BY orderDetails."orderID" DESC;
