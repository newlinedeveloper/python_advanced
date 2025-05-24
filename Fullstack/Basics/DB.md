### What is a Relational Database?

A Relational Database Management System (RDBMS) stores data in the form of tables, which are organized as rows and columns. Relationships between tables are maintained through keys (primary and foreign keys).

RDBMS examples: PostgreSQL, MySQL, Oracle, SQL Server

Each table is like a spreadsheet:

* Columns → represent attributes (e.g. name, age)
* Rows → represent individual records

Example Table: Vehicle

| id | name    | model\_year |
| -- | ------- | ----------- |
| 1  | EVX-100 | 2023        |
| 2  | EVX-200 | 2025        |

---

✅ Key Concepts

1. Tables

* A table is a collection of related data.
* Think of it like a sheet in Excel: rows are entries, columns are attributes.

2. Columns

* Each column has a data type (e.g., INTEGER, TEXT, DATE).
* Columns define the structure and type of data.

3. Rows (Records)

* Each row is a unique data entry (e.g., a single vehicle).
* Rows contain values for each column defined in the table.

4. Primary Key

* A column (or set of columns) that uniquely identifies each row in a table.
* Must be unique and not NULL.

Example:
```
CREATE TABLE vehicle (
id SERIAL PRIMARY KEY,
name VARCHAR(100),
model_year INTEGER
);
```
5. Foreign Key

* A foreign key is a reference to a primary key in another table.
* It establishes a relationship between two tables.

Example:
```
CREATE TABLE component (
id SERIAL PRIMARY KEY,
name VARCHAR(100),
vehicle_id INTEGER REFERENCES vehicle(id)
);
```

Here, vehicle_id in the component table is a foreign key that links each component to a vehicle.

---

✅ Relationships Between Tables

1. One-to-One

* One row in Table A corresponds to one row in Table B.

Example:
One Driver has one License.

2. One-to-Many

* One row in Table A maps to many rows in Table B.
* Most common relationship in relational databases.

Example:
One Vehicle has many Components.

3. Many-to-Many

* Many rows in Table A relate to many rows in Table B.
* Requires a junction (association) table.

Example:
Vehicles and Features (a vehicle can have many features, and a feature can belong to many vehicles).

```
CREATE TABLE vehicle_feature (
vehicle_id INTEGER REFERENCES vehicle(id),
feature_id INTEGER REFERENCES feature(id),
PRIMARY KEY (vehicle_id, feature_id)
);
```
---

✅ RDBMS vs NoSQL (basic comparison)

| Feature       | RDBMS (PostgreSQL)         | NoSQL (MongoDB)              |
| ------------- | -------------------------- | ---------------------------- |
| Structure     | Tables with rows & columns | Documents (JSON-like)        |
| Schema        | Fixed schema               | Flexible schema              |
| Relationships | Strong via foreign keys    | Weak or embedded             |
| Use Cases     | Transactions, reporting    | Real-time analytics, agility |
| Examples      | PostgreSQL, MySQL, Oracle  | MongoDB, Firebase, Cassandra |

---


### 2. Learn Basic SQL – Examples

📌 Let's assume we have two tables:

vehicles

| id | name    | model\_year |
| -- | ------- | ----------- |
| 1  | EVX-100 | 2023        |
| 2  | EVX-200 | 2024        |

components

| id | name         | type   | vehicle\_id |
| -- | ------------ | ------ | ----------- |
| 1  | Battery Pack | Power  | 1           |
| 2  | Brake System | Safety | 1           |
| 3  | Infotainment | UI     | 2           |

---

🛠 1. CREATE TABLE

Define a new table:

```sql
CREATE TABLE vehicles (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  model_year INTEGER
);
```

```sql
CREATE TABLE components (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  type VARCHAR(50),
  vehicle_id INTEGER REFERENCES vehicles(id)
);
```

---

🛠 2. INSERT INTO

Add rows into a table:

```sql
INSERT INTO vehicles (name, model_year)
VALUES ('EVX-100', 2023),
       ('EVX-200', 2024);
```

```sql
INSERT INTO components (name, type, vehicle_id)
VALUES ('Battery Pack', 'Power', 1),
       ('Brake System', 'Safety', 1),
       ('Infotainment', 'UI', 2);
```

---

🛠 3. SELECT

Query data:

```sql
SELECT * FROM vehicles;
```

```sql
SELECT name, model_year FROM vehicles WHERE model_year > 2023;
```

---

🛠 4. UPDATE

Change data:

```sql
UPDATE vehicles
SET name = 'EVX-100 Pro'
WHERE id = 1;
```

---

🛠 5. DELETE

Remove rows:

```sql
DELETE FROM components
WHERE type = 'UI';
```

---

🛠 6. WHERE, ORDER BY, LIMIT, OFFSET

Filter and sort data:

```sql
SELECT * FROM vehicles
WHERE model_year >= 2023
ORDER BY model_year DESC
LIMIT 1 OFFSET 0;
```

---

🛠 7. JOIN (INNER, LEFT, RIGHT, FULL)

Combine data from multiple tables:

🔹 INNER JOIN (only matching rows)

```sql
SELECT v.name AS vehicle, c.name AS component
FROM vehicles v
INNER JOIN components c ON v.id = c.vehicle_id;
```

🔹 LEFT JOIN (all from left + matches from right)

```sql
SELECT v.name, c.name
FROM vehicles v
LEFT JOIN components c ON v.id = c.vehicle_id;
```

🔹 RIGHT JOIN

```sql
SELECT v.name, c.name
FROM vehicles v
RIGHT JOIN components c ON v.id = c.vehicle_id;
```

🔹 FULL OUTER JOIN

```sql
SELECT v.name, c.name
FROM vehicles v
FULL OUTER JOIN components c ON v.id = c.vehicle_id;
```

---

🛠 8. GROUP BY + Aggregate Functions

🔹 COUNT: How many components per vehicle

```sql
SELECT vehicle_id, COUNT(*) AS total_components
FROM components
GROUP BY vehicle_id;
```

🔹 SUM, AVG: (Assume a numeric column e.g., weight or cost)

```sql
-- Total model years summed (not realistic, just for syntax)
SELECT SUM(model_year) FROM vehicles;
```

---



