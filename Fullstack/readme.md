🚗 Project: Vehicle Configuration and Simulation Platform

📌 Description:
Led the development of a fullstack platform for configuring, integrating, simulating, and testing virtual vehicle architectures. The platform enables automotive engineers to define a vehicle model, assign individual components (e.g., ECUs, sensors, actuators), configure parameters, simulate interactions, and validate functionality through test cases—entirely through a web interface.

✅ Key Features:

1. Vehicle Modeling and Configuration

* Engineers can create a digital twin of a vehicle by defining high-level vehicle attributes (e.g., model, variant, year).
* Component hierarchy (Engine ECU, Brake Controller, BMS, etc.) is mapped and stored using relational and document-based structures.
* Each component supports customizable configuration data, such as communication interfaces, software versions, calibration values, etc.

2. Component Integration Workflow

* Components can be virtually wired to one another to simulate real-world signal/data flows.
* Dependency validation logic ensures compatibility between integrated components.
* Integration logic supports dynamic component replacement and interface updates.

3. Simulation and Testing Environment

* Allows simulation of system behavior with configurable input signals.
* Engineers can define and execute test cases to verify expected behavior (e.g., signal propagation, error state transitions).
* Provides runtime logs, status reports, and test result dashboards.

4. Access Control and Collaboration

* Role-based access for architects, developers, and testers.
* Audit trail and versioning support for tracking configuration changes and test results.

🛠 Tech Stack:

* Frontend: React.js, Redux, Tailwind CSS
* Backend: Python (FastAPI), PostgreSQL (component data), MongoDB (config snapshots)
* DevOps: Docker, GitHub Actions, AWS (EC2, S3, CloudWatch)
* Simulation Engine: Python modules for signal simulation and data injection
* API Documentation: Swagger/OpenAPI

📈 Impact:

* Streamlined vehicle configuration and test workflows, reducing setup time by 60%
* Enabled faster prototyping and validation cycles for new vehicle architectures
* Improved cross-team collaboration by centralizing vehicle knowledge and test history
* Reduced physical test rig dependency by enabling virtual testing environments

------

🚧 High-Level Design (HLD)

🔹 1. Database Design (Entities and Relationships)

Here are the primary entities and their relationships:

Entity: Vehicle

* id (PK)
* name (e.g., "EV-Concept-X")
* model\_year (e.g., 2025)
* variant (e.g., "Luxury" or "Sport")

Entity: Component

* id (PK)
* vehicle\_id (FK → Vehicle.id)
* name (e.g., “Battery Management System”)
* type (e.g., ECU, Sensor, Controller)

Entity: Configuration

* id (PK)
* component\_id (FK → Component.id)
* key (e.g., “CAN ID”)
* value (e.g., “0x101”)

Entity: Simulation

* id (PK)
* vehicle\_id (FK → Vehicle.id)
* status (Pending, Running, Success, Failed)
* created\_at
* updated\_at

Entity: User (optional for access control)

* id (PK)
* username
* role (Engineer, Admin, Viewer)
* password\_hash

Optional Entities for future expansion:

* TestCase: Linked to Simulation
* ResultLog: Linked to TestCase

ER Diagram (simplified):

Vehicle
└───▶ Component
└───▶ Configuration

Vehicle
└───▶ Simulation

---

🔹 2. API Design (REST Endpoints using Django + DRF)

🟢 Vehicle Endpoints:

* GET /api/vehicles/ → List all vehicles
* POST /api/vehicles/ → Create new vehicle
* GET /api/vehicles/{id}/ → Get vehicle details
* PUT /api/vehicles/{id}/ → Update vehicle
* DELETE /api/vehicles/{id}/ → Delete vehicle

🟢 Component Endpoints:

* GET /api/components/?vehicle={vehicle\_id} → List components for a vehicle
* POST /api/components/ → Create a new component
* PUT /api/components/{id}/ → Update a component
* DELETE /api/components/{id}/ → Delete a component

🟢 Configuration Endpoints:

* GET /api/configurations/?component={component\_id}
* POST /api/configurations/
* PUT /api/configurations/{id}/
* DELETE /api/configurations/{id}/

🟢 Simulation Endpoints:

* POST /api/simulations/ → Trigger a simulation for a vehicle
* GET /api/simulations/?vehicle={vehicle\_id} → View simulations for a vehicle
* GET /api/simulations/{id}/ → Get simulation status
* PATCH /api/simulations/{id}/status → Update simulation status (if handled manually or externally)

🟢 Optional: Authentication

* POST /api/auth/login
* GET /api/auth/profile

---



