# Absence Management System

## Overview
The Absence Management System (AMS) is a Python-based application designed to track and manage student absences across various modules within an educational institution. The system allows users to add, delete, and view absences, as well as generating statistical insights and visualizations.

## Features

- **Add Absences Interactively:** Through a live prompt, users can enter their own absence records.
- **Print Student Absences:** Users can search for and print out a student's absent history for a certain time period.
- **Print Module Absences:** Users can search for and print out the number of absences for a certain subject on a certain date.
- **Plot Module Absences:** Users can make a bar plot that shows how many absences there were for a certain subject over a certain time period.
- **Print Unauthorised Absences:** Users can look up and print out a list of all unapproved departures for a certain date or for all dates.
- **Delete an Absence:** By giving the absence code, users can remove an absence record.

## Running the Code

### Requirements

Before running the application, ensure you have Python installed on your system. The application requires Python 3.7 or later.

### Steps to Run

1. **Navigate to the Project Directory:**
   Open a terminal and navigate to the directory where the project is located.

2. **Run the Application:**
   Execute the main script using Python. In the terminal, run:
   ```
   python main.py
   ```

3. **Interact with the System:**
   After running the script, you will be prompted to choose between adding data interactively or running predefined test cases:
   - Enter `1` to start adding absence data interactively.
   - Enter `2` to run predefined test cases.

4. **Follow the On-Screen Prompts:**
   The system will guide you through various operations based on your choice. Simply follow the on-screen prompts to interact with the system.

## Note

The application's functionality is encapsulated within the `AbsenceManagementSystem` class. For further modifications or integrations, you can import this class into your Python projects and instantiate it as needed.
