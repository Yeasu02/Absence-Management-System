from AbsenceManagementSystem import AbsenceManagementSystem

def display_menu():
    print(
        "\nAbsence Management System\n"
        "1. Add Absence\n"
        "2. Print Student Absences for a Given Time Period\n"
        "3. Print Module Absences for a Given Day\n"
        "4. Plot Absences for a Module Over a Time Period\n"
        "5. Print Unauthorised Absences for a Given Date\n"
        "6. Print All Unauthorised Absences\n"
        "7. Delete an Absence\n"
        "8. Run Predefined Test Cases\n"
        "9. Exit"
    )
    choice = input("Enter your choice (1-9): ")
    return choice

ams = AbsenceManagementSystem()

choice = input("Do you want to add data interactively (1).. or run test cases (2)? Enter 1 or 2: ")

if choice == "1":
    while True:
        user_choice = display_menu()
        
        if user_choice == "1":
            ams.add_absence_interactively()
        elif user_choice == "2":
            student_number = input("Enter student number: ")
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            ams.print_student_absences(student_number, start_date, end_date)
        elif user_choice == "3":
            module_code = input("Enter module code: ")
            date = input("Enter date (YYYY-MM-DD): ")
            ams.print_module_absences(module_code, date)
        elif user_choice == "4":
            module_code = input("Enter module code: ")
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            ams.plot_module_absences(module_code, start_date, end_date)
        elif user_choice == "5":
            date = input("Enter date (YYYY-MM-DD): ")
            ams.print_unauthorised_absences_by_date(date)
        elif user_choice == "6":
            ams.print_all_unauthorised_absences()
        elif user_choice == "7":
            absence_code = input("Enter the absence code to delete: ")
            ams.delete_absence(absence_code)
        elif user_choice == "8":
            ams.run_test_cases()
        elif user_choice == "9":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

elif choice == "2":
    ams.run_test_cases()
else:
    print("Invalid choice. Exiting.")
