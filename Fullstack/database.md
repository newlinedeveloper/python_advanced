Here is the complete set of **PostgreSQL SQL queries** to:

1. Create the tables (`Vehicle`, `Component`, `Configuration`, `Simulation`, `User`)
2. Insert sample data
3. Set up foreign key relationships
4. Prepare the schema for **future expansion** (`TestCase`, `ResultLog`)

---

### ✅ **1. Schema Creation Queries**

```sql
-- Table: Vehicle
CREATE TABLE Vehicle (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    model_year INT NOT NULL,
    variant TEXT
);

-- Table: Component
CREATE TABLE Component (
    id SERIAL PRIMARY KEY,
    vehicle_id INT REFERENCES Vehicle(id) ON DELETE CASCADE,
    name TEXT NOT NULL,
    type TEXT CHECK (type IN ('ECU', 'Sensor', 'Controller')) NOT NULL
);

-- Table: Configuration
CREATE TABLE Configuration (
    id SERIAL PRIMARY KEY,
    component_id INT REFERENCES Component(id) ON DELETE CASCADE,
    key TEXT NOT NULL,
    value TEXT NOT NULL
);

-- Table: Simulation
CREATE TABLE Simulation (
    id SERIAL PRIMARY KEY,
    vehicle_id INT REFERENCES Vehicle(id) ON DELETE CASCADE,
    status TEXT CHECK (status IN ('Pending', 'Running', 'Success', 'Failed')) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table: User (optional)
CREATE TABLE AppUser (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    role TEXT CHECK (role IN ('Engineer', 'Admin', 'Viewer')) NOT NULL,
    password_hash TEXT NOT NULL
);

-- Future Table: TestCase
CREATE TABLE TestCase (
    id SERIAL PRIMARY KEY,
    simulation_id INT REFERENCES Simulation(id) ON DELETE CASCADE,
    name TEXT NOT NULL,
    description TEXT
);

-- Future Table: ResultLog
CREATE TABLE ResultLog (
    id SERIAL PRIMARY KEY,
    test_case_id INT REFERENCES TestCase(id) ON DELETE CASCADE,
    log TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

### ✅ **2. Sample Data Insertion**

```sql
-- Insert Vehicle
INSERT INTO Vehicle (name, model_year, variant)
VALUES 
('EV-Concept-X', 2025, 'Luxury'),
('EV-Concept-Y', 2024, 'Sport');

-- Insert Components
INSERT INTO Component (vehicle_id, name, type)
VALUES 
(1, 'Battery Management System', 'ECU'),
(1, 'Thermal Sensor', 'Sensor'),
(2, 'Drive Controller', 'Controller');

-- Insert Configuration
INSERT INTO Configuration (component_id, key, value)
VALUES 
(1, 'CAN ID', '0x101'),
(1, 'Voltage Range', '300-400V'),
(2, 'CAN ID', '0x202');

-- Insert Simulations
INSERT INTO Simulation (vehicle_id, status)
VALUES 
(1, 'Pending'),
(1, 'Running'),
(2, 'Success');

-- Insert Users
INSERT INTO AppUser (username, role, password_hash)
VALUES 
('alice', 'Engineer', 'hashed_pw_1'),
('bob', 'Admin', 'hashed_pw_2'),
('carol', 'Viewer', 'hashed_pw_3');
```

---

### ✅ **3. Example Queries**

```sql
-- List all components of a specific vehicle
SELECT v.name AS vehicle, c.name AS component, c.type
FROM Vehicle v
JOIN Component c ON c.vehicle_id = v.id
WHERE v.name = 'EV-Concept-X';

-- Get all configurations for a given component
SELECT c.name, cfg.key, cfg.value
FROM Component c
JOIN Configuration cfg ON cfg.component_id = c.id
WHERE c.name = 'Battery Management System';

-- List all simulations for a vehicle
SELECT v.name, s.status, s.created_at
FROM Vehicle v
JOIN Simulation s ON s.vehicle_id = v.id
WHERE v.name = 'EV-Concept-X';

-- Count simulations by status
SELECT status, COUNT(*) FROM Simulation GROUP BY status;

-- List users and their roles
SELECT username, role FROM AppUser;
```

---

Would you like a graphical ER diagram or a setup script for a PostgreSQL container (e.g., with Docker)?
