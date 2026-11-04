# Train Reservation System

A modern train ticket reservation application built with Spring Boot, Java 17, Spring Security, JPA, and a single-page web interface. The system allows users to register, log in, search trains, book tickets, view reservations, and cancel bookings with secure JWT-based authentication.

## Overview

This project was designed to address common issues in traditional reservation systems, including weak security, session-based state management, limited booking flows, and concurrency problems during seat allocation. The application uses a stateless authentication model and optimistic locking to improve reliability under concurrent booking attempts.

## Features

- User registration and login
- Secure JWT authentication
- Role-based access control
- Search for trains by source and destination
- Booking multiple passengers in a single reservation
- Generate unique PNR numbers
- View reservation details
- Cancel bookings and restore seat availability
- Optimistic locking to prevent double booking
- Responsive web UI using HTML, CSS, JavaScript, and Bootstrap
- MySQL for production and H2 for local/test use

## Tech Stack

- Java 17
- Spring Boot 3.2.5
- Spring Web
- Spring Data JPA
- Spring Security
- Thymeleaf
- Maven
- MySQL
- H2 Database
- JWT (jjwt)
- Lombok

## Project Structure

```text
.
├── pom.xml
├── .classpath
├── .project
├── Project_Report.md
├── Project_Report.docx
├── Project_Report.pptx
├── Train Ticket Reservation System.pdf
├── OJT - Internship Company Letter.pdf
├── capture_screenshots.py
├── generate_docx.py
├── generate_report_assets.py
└── README.md
```

## Prerequisites

Before running the project, make sure you have the following installed:

- JDK 17+
- Maven 3.8+
- MySQL 8.x (optional if using H2 for local testing)
- IDE such as IntelliJ IDEA or Eclipse

## Configuration

The project uses Spring Boot and can be configured through application properties. If you are using MySQL, configure the datasource in your application configuration file.

Example configuration:

```properties
spring.datasource.url=jdbc:mysql://localhost:3306/train_reservation
spring.datasource.username=root
spring.datasource.password=yourpassword
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true
```

If you want to use the embedded H2 database for testing, ensure the H2 dependency is enabled and configure the relevant properties accordingly.

## Run the Project

1. Clone the repository:

```bash
git clone https://github.com/Riyaj2700/Train-Reservation-System.git
cd Train-Reservation-System
```

2. Build the project:

```bash
mvn clean install
```

3. Run the application:

```bash
mvn spring-boot:run
```

4. Open the application in your browser:

```text
http://localhost:8080
```

## Main Functionality Flow

1. Register a new user or log in.
2. Search for available trains by route.
3. Select a train and enter passenger details.
4. Complete a simulated payment step.
5. Receive a booking confirmation with a unique PNR.
6. View or cancel the ticket from the reservation dashboard.

## Security

The application uses Spring Security with JWT-based authentication. This ensures stateless session management and improved security over traditional cookie-based session systems.

## Documentation

Additional project documentation is included in:

- `Project_Report.md`
- `Project_Report.docx`
- `Project_Report.pptx`
- `Train Ticket Reservation System.pdf`

These files provide project analysis, architecture details, requirements, and system overview.

## License

This repository does not currently include an explicit license file. If you plan to distribute or publish this project, add an appropriate open-source license before doing so.

## Contributing

Contributions are welcome. You can fork the repository, create a feature branch, make your changes, and submit a pull request.

## Contact

Project repository: https://github.com/Riyaj2700/Train-Reservation-System

