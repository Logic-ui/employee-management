Employee Management Dashboard

A full-stack web application to manage employee records efficiently with Python Flask backend and React.js frontend. Includes interactive charts, dark/light mode, search, sorting, pagination, and export options.

Features

CRUD Operations: Add, update, delete, and view employees

Search & Sorting: Quickly filter employees and sort by columns

Pagination: Easily navigate large datasets

Total Salary Summary: Display total payroll dynamically

Export Options: Download employee data in Excel or PDF

Interactive Dashboard: Pie & Bar charts showing total salary and employee count by position

Dark/Light Mode: Toggle between themes

Responsive Design: Works on desktop and mobile

Tech Stack

Backend: Python, Flask, SQLite

Frontend: React.js, Axios, Chart.js

Export Libraries: XLSX, jsPDF, jsPDF-AutoTable

Styling: CSS

Project Structure
backend/
   ├─ app.py
   ├─ models.py
   └─ database.db (auto-created)
frontend/
   ├─ src/
   │   ├─ components/
   │   │   ├─ EmployeeForm.js
   │   │   └─ EmployeeList.js
   │   ├─ App.js
   │   └─ index.css
   ├─ package.json
   └─ package-lock.json

Installation & Setup
Backend (Flask)

Navigate to the backend folder:

cd backend


Create a virtual environment:

python -m venv venv


Activate it:

Windows: venv\Scripts\activate

Linux/Mac: source venv/bin/activate

Install dependencies:

pip install -r requirements.txt


Run the backend:

python app.py

Frontend (React)

Navigate to the frontend folder:

cd frontend


Install dependencies:

npm install


Start the frontend:

npm start


The app should now be running at http://localhost:3000

Usage

Add new employees using the form

Edit or delete existing employees

Search, sort, and paginate the table

Toggle dark/light theme

Export employee data to Excel or PDF

View dashboard charts for salary and employee count

Screenshots

(Add screenshots of your dashboard, table, and charts here for better presentation.)

Contributing

Feel free to fork the project and submit pull requests for improvements.

License

This project is open-source and free to use.
