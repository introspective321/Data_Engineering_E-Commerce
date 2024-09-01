# Data_Engineering_E-Commerce
**Assignment-1**

## Overview
This project involves designing and implementing a database for an e-commerce platform focused on artworks. The project includes various tasks such as creating ER diagrams, implementing custom hash functions, indexing, and executing SQL queries for data manipulation.

## Tasks and Files

### Task 1: ER Diagram
- **Description:** Design the Entity-Relationship Diagram (ERD) for the e-commerce platform.
- **File Reference:** ER_Diagram.pdf

### Task 2: Table Creation and Insertion of Dummy Values
- **Description:** Create tables and insert dummy values into the database.
- **File Reference:** [tables_creat_insert.py](db/tables_creat_insert.py)
- **Additional Values:** Additional dummy values were inserted.
- **File Reference:** [add_insert.py](db/add_insert.py)

### Task 3: Normalization
- **Description:** Ensure that all tables are in 3NF (Third Normal Form).
- **File Reference:** LabReport.pdf

### Task 4 & 5: Custom Hash Function
- **Description:** Implement a custom hash function for hashing passwords and artwork names.
- **File Reference:** [hash.py](db/hash.py)

### Task 6 & 7: Indexing
- **Description:** Implement clustering indexing and secondary indexing on the database tables.
- **File Reference:** [secon_idx.py](db/secon_idx.py)

### Task 8: Comparison Between Indexing Schemes
- **Description:** Compare clustering indexing and secondary indexing in terms of performance and storage.
- **File Reference:** [compare.py](db/compare.py)

### Task 9: Adding Information About Contemporary Artists
- **Description:** Add information about 5 contemporary artists to the database.
- **File Reference:** [contemporary_artists.py](db/contemporary_artists.py)

### Task 10: Report on Artwork Listings
- **Description:** Generate a report of all artwork listings made in August 2024.
- **File Reference:** [report.py](db/report.py)

### Task 11: Remove Artwork Purchases
- **Description:** Remove all artwork purchases made after 7PM on August 15, 2024.
- **File Reference:** [remove.py](db/report.py)

## Getting Started

To get started with this project, clone the repository and install the necessary dependencies. Make sure you have a MySQL server running and create a database before executing the scripts.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Data_Engineering_E-Commerce.git
