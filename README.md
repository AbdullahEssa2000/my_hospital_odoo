# Hospital Management System – Odoo 18

A Hospital Management System developed using Odoo 18 ERP to manage hospital operations, patient records, appointments, prescriptions, and medical products.

## Project Overview

This project aims to provide an integrated hospital management solution using Odoo's modular architecture and built-in business applications.

## Features

### 1. Patient Management
- Create and manage patient records.
- Store patient information.
- View and track patient details.

### 2. Appointment Management
- Schedule patient appointments.
- Manage appointment records.
- Link appointments with patients and doctors.

### 3. Prescription Management
- Create medical prescriptions.
- Add multiple prescription lines.
- Link prescribed medicines with Odoo products.

### 4. Medical Products
- Extend Odoo product functionality.
- Identify and manage medical products.
- Integrate medicines with inventory operations.

### 5. Doctor and Employee Management
- Manage doctor and employee records.
- Organize hospital staff information.

## Odoo Integration

The module integrates with standard Odoo applications:

- Inventory
- Sales
- Purchase
- Accounting
- Employees
- Point of Sale
- CRM

## Technologies Used

- Odoo 18
- Python
- PostgreSQL
- Odoo ORM
- XML
- SCSS
- Git & GitHub

## Project Structure

```text
my_hospital/
│
├── controllers/
├── data/
├── demo/
├── models/
├── security/
├── static/
│   └── src/
│       └── scss/
├── views/
├── wizards/
│
├── __init__.py
├── __manifest__.py
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

2. Copy the module into your Odoo custom addons directory.

3. Restart the Odoo server.

4. Update the Apps List from the Odoo interface.

5. Search for `Hospital Management System`.

6. Install the module.

## Development

This project is developed as a practical application of Odoo 18 development concepts, including:

- Custom Models and Fields.
- ORM Operations.
- Model Inheritance.
- XML Views and Actions.
- Access Rights and Security Rules.
- Wizards.
- Integration with Standard Odoo Modules.

## License

LGPL-3

## Author

Abdullah Eissa

Odoo Developer | Python Developer
