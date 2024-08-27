# Odoo Educational Center

## Overview
The Odoo Educational Center is a comprehensive application designed to automate the payment system of an educational center. It allows administrators to manage courses, teachers, students, and payments, while providing different user roles and access levels.

## Features
- **Course Management**: Administrators can create and manage courses, including assigning teachers to courses.
- **Teacher Management**: Teachers can be created and assigned to courses.
- **Student Management**: Students can be enrolled in one or more groups, and their payment information can be tracked.
- **Payment Management**: Administrators can view, accept, and edit payments made by students. Teachers can also view and accept payments for their assigned groups.
- **Reporting**: Administrators can view detailed reports on payments, including charts and filters for better analysis.

## Installation

### Docker
1. Ensure you have Docker installed on your system.
2. Clone the repository to your local machine:
`git clone https://github.com/ulugkhujaev/educational_center.git`
3. Navigate to the project directory:
`cd educational_center`
4. Build and run the Docker image:
`docker compose up --build`
6. Access the application in your web browser at `http://localhost:8069`.


## Usage
1. Log in to the Odoo application using the admin credentials.
2. Navigate to the "Educational Center" module.
3. Manage courses, teachers, students, and payments according to your user role and permissions.
4. Administrators can view the payment reports and charts.
5. Teachers can view and accept payments for their assigned groups.


## Testing
    Run tests:
`docker-compose run --rm web odoo -c /etc/odoo/odoo.conf -d postgres --test-enable --stop-after-init -i educational_center`     