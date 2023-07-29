SELECT *from customers 
select count(distinct city) as num_cities from customer
select * from customers where country"germany"
-- ####################################################################
-- # Basic SELECT statement
-- # See https://www.ibm.com/docs/en/db2-for-zos/13?topic=statements-select for complete syntax.
-- ####################################################################
SELECT *
    FROM customer
    WHERE country in ("germany","mexico","uk")
-- ####################################################################
-- # Basic SELECT statement
-- # See https://www.ibm.com/docs/en/db2-for-zos/13?topic=statements-select for complete syntax.
-- ####################################################################
SELECT *
    FROM products
    WHERE price BETWEEN 10 And 15
       and supplier id not in (1,2)

-- ####################################################################
-- # Basic SELECT statement
-- # See https://www.ibm.com/docs/en/db2-for-zos/13?topic=statements-select for complete syntax.
-- ####################################################################
SELECT *
    FROM products
    WHERE productname
        LIKE "%an%t%"   



-- ####################################################################
-- # Basic SELECT statement
-- # See https://www.ibm.com/docs/en/db2-for-zos/13?topic=statements-select for complete syntax.
-- ####################################################################
SELECT *
    FROM products
    where price<100
    order by price
       


