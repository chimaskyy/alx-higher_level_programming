# MORE on MYSQL

##Types of join

* Inner Join: is a type of join operation in a relational database that combines rows from two or more tables based on a related column between them. The result includes only the rows where there is a match between the specified columns in both tables.
If a row in table1 has no matching row in table2, or vice versa, that row is excluded from the result set.
Only the rows where there is a match in both tables are included in the final result.

```
SELECT *
FROM names
INNER JOIN departments ON names.id = departments.id;
```
Just like how intersection works in SET, inner join returns the intersection of rows from two tables based on a specified condition, excluding rows that don't have matching values in the specified columns.

* Left Join: is a type of join operation in a relational database that returns all the rows from the left table and the matched rows from the right table. If there is no match in the right table, NULL values are returned for columns from the right table.
Left Join prioritizes the data on left of tables(first table)

```
SELECT *
FROM names
INNER JOIN departments ON names.id = departments.id;
```
The LEFT JOIN returns all rows from the left table (names), and the matching rows from the right table (departments).
If a row in ``names`` has no matching row in ``depatments``, the result will contain NULL values for columns from ``departments``.
Rows from ``names`` without a matching row in t``departments`` are still included in the result.
LEFT JOIN is used when you want to retrieve all rows from the left table regardless of whether there are matching rows in the right table

* Right Join: is a type of join operation in a relational database that returns all the rows from the right table and the matched rows from the left table. If there is no match in the left table, NULL values are returned for columns from the left table.
Right Join prioritizes the data on right of tables(second table)

```
SELECT *
FROM names
INNER JOIN departments ON names.id = departments.id;
```
The RIGHT JOIN returns all rows from the right table (departments), and the matching rows from the left table (names).
If a row in ``departments`` has no matching row in ``names``, the result will contain NULL values for columns from ``names``.
Rows from ``departments`` without a matching row in ``names`` are still included in the result.
RIGHT JOIN is used when you want to retrieve all rows from the right table regardless of whether there are matching rows in the left table.

* Full Join: returns all rows from both tables being joined, whether or not there is a match between the columns used for the join. If there is no match for a row in one of the tables, the result set will contain NULL values for columns from the table without a match.

```
SELECT *
FROM names
INNER JOIN departments ON names.id = departments.id;
```
The FULL JOIN returns all rows from both tables (tnames and deparments).
If there is a match between the specified columns, the result will include columns from both tables for that row.
If there is no match for a row in one of the tables, the columns from the table without a match will contain NULL values in the result set.
FULL JOIN is used when you want to retrieve all rows from both tables, regardless of whether there are matching rows in either table.