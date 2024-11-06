from collections import defaultdict
from datetime import datetime
import matplotlib.pyplot as plt

class AbsenceManagementSystem:
    def __init__(self):
        self.absences_db = {}
        self.student_absences = defaultdict(list)
        self.module_absences = defaultdict(list)
        self.date_absences = defaultdict(list)
        self.unauthorised_absences = []

    def _validate_date(self, date_str):
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")

    def insert_absence(self, absence_code, date, student_name, gender, student_number, authorised, module_code):
        if absence_code in self.absences_db:
            raise ValueError(f"Absence code {absence_code} already exists.")
        
        formatted_date = self._validate_date(date)
        
        self.absences_db[absence_code] = {
            'date': formatted_date,
            'student_name': student_name,
            'gender': gender,
            'student_number': student_number,
            'authorised': authorised,
            'module_code': module_code
        }
        
        self.student_absences[student_number].append(absence_code)
        self.module_absences[module_code].append(absence_code)
        self.date_absences[formatted_date.date()].append(absence_code)
        if not authorised:
            self.unauthorised_absences.append(absence_code)
    
    def add_absence_interactively(self):
        print("Enter the details of the absence:")
        absence_code = input("Absence Code: ")
        date = input("Date (YYYY-MM-DD): ")
        student_name = input("Student's Full Name: ")
        gender = input("Gender (M/F/NB/O): ")
        student_number = input("Student Number (e.g., DSA123): ")
        authorised_input = input("Authorised? (yes/no): ")
        authorised = authorised_input.strip().lower() == 'yes'
        module_code = input("Module Code (e.g., ABC123): ")
        
        try:
            self.insert_absence(absence_code, date, student_name, gender, student_number, authorised, module_code)
            print(f"Absence {absence_code} added successfully.")
        except Exception as e:
            print(f"Error: {e}")

    def print_student_absences(self, student_number, start_date, end_date):
        start = self._validate_date(start_date)
        end = self._validate_date(end_date)
        
        absences = [
            code for code in self.student_absences[student_number]
            if start <= self.absences_db[code]['date'] <= end
        ]
        print(f"Student {student_number} has {len(absences)} absences between {start_date} and {end_date}.")
    
    def print_student_absences(self, student_number, start_date, end_date):
        start = self._validate_date(start_date)
        end = self._validate_date(end_date)
        
        absences = [
            code for code in self.student_absences.get(student_number, [])
            if start <= self.absences_db[code]['date'] <= end
        ]
        if absences:
            print(f"Student {student_number} has {len(absences)} absences between {start_date} and {end_date}.")
        else:
            print(f"No absences found for student {student_number} between {start_date} and {end_date}.")

    def print_module_absences(self, module_code, date):
        formatted_date = self._validate_date(date).date()
        absences = [
            code for code in self.module_absences.get(module_code, [])
            if self.absences_db[code]['date'].date() == formatted_date
        ]
        if absences:
            print(f"Module {module_code} has {len(absences)} absences on {date}.")
        else:
            print(f"No absences found for module {module_code} on {date}.")

    def plot_module_absences(self, module_code, start_date, end_date):
        start = self._validate_date(start_date)
        end = self._validate_date(end_date)
        
        absences_per_day = defaultdict(int)
        for code in self.module_absences.get(module_code, []):
            absence_date = self.absences_db[code]['date']
            if start <= absence_date <= end:
                absences_per_day[absence_date.date()] += 1
        
        if absences_per_day:
            dates = list(absences_per_day.keys())
            counts = list(absences_per_day.values())
            plt.figure(figsize=(10, 6))
            plt.bar(dates, counts, color='skyblue')
            plt.xlabel('Date')
            plt.ylabel('Number of Absences')
            plt.title(f'Absences for module {module_code} from {start_date} to {end_date}')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        else:
            print(f"No absences found for module {module_code} between {start_date} and {end_date}.")

    def print_unauthorised_absences_by_date(self, date):
        formatted_date = self._validate_date(date).date()
        absences = [
            code for code in self.date_absences.get(formatted_date, [])
            if not self.absences_db[code]['authorised']
        ]
        if absences:
            print(f"Unauthorised absences on {date}:")
            for code in absences:
                print(f"- {self.absences_db[code]['student_name']} ({code})")
        else:
            print(f"No unauthorised absences found on {date}.")

    def print_all_unauthorised_absences(self):
        if self.unauthorised_absences:
            print("All unauthorised absences:")
            for code in self.unauthorised_absences:
                absence = self.absences_db[code]
                print(f"- {absence['student_name']} ({code}) on {absence['date'].strftime('%Y-%m-%d')}")
        else:
            print("No unauthorised absences found.")

    def delete_absence(self, absence_code):
        if absence_code not in self.absences_db:
            print(f"No absence found with code {absence_code}.")
            return
        
        absence = self.absences_db.pop(absence_code)
        self.student_absences[absence['student_number']].remove(absence_code)
        self.module_absences[absence['module_code']].remove(absence_code)
        self.date_absences[absence['date'].date()].remove(absence_code)
        if not absence['authorised']:
            self.unauthorised_absences.remove(absence_code)
        print(f"Absence {absence_code} successfully deleted.")

    def run_test_cases(self):

        test_data = [
            ("000001", "2024-01-01", "Alice Smith", "F", "DSA123", False, "ABC123"),
            ("000002", "2024-01-02", "Bob Jones", "M", "DSA124", True, "ABC124"),
            ("000003", "2024-01-03", "Charlie Brown", "NB", "DSA125", True, "ABC123"),
            ("000004", "2024-01-04", "Diana Prince", "F", "DSA126", False, "ABC125"),
            ("000005", "2024-01-05", "Ethan Hunt", "M", "DSA127", True, "ABC124"),
            ("000006", "2024-01-06", "Fiona Gallagher", "F", "DSA128", False, "ABC126"),
            ("000007", "2024-01-07", "George King", "M", "DSA129", True, "ABC123"),
            ("000008", "2024-01-08", "Hannah Abbott", "F", "DSA130", False, "ABC125"),
            ("000009", "2024-01-09", "Ian Somerhalder", "M", "DSA131", True, "ABC126"),
            ("000010", "2024-01-10", "Julia Roberts", "F", "DSA132", False, "ABC124"),
            ("000011", "2024-01-11", "Kurt Hummel", "NB", "DSA133", True, "ABC123"),
            ("000012", "2024-01-12", "Luna Lovegood", "F", "DSA134", False, "ABC125"),
            ("000013", "2024-01-13", "Mason Grey", "M", "DSA135", True, "ABC126"),
            ("000014", "2024-01-14", "Nina Dobrev", "F", "DSA136", False, "ABC124"),
            ("000015", "2024-01-15", "Oliver Queen", "M", "DSA137", True, "ABC123"),
            ("000016", "2024-01-16", "Pam Beesly", "F", "DSA138", False, "ABC125"),
            ("000017", "2024-01-17", "Quentin Lance", "M", "DSA139", True, "ABC126"),
            ("000018", "2024-01-18", "Rachel Green", "F", "DSA140", False, "ABC124"),
            ("000019", "2024-01-19", "Steve Rogers", "M", "DSA141", True, "ABC123"),
            ("000020", "2024-01-20", "Tina Cohen", "NB", "DSA142", False, "ABC125"),
            ("000021", "2024-01-21", "Ulysses Grant", "M", "DSA143", True, "ABC126"),
            ("000022", "2024-01-22", "Victoria Chase", "F", "DSA144", False, "ABC124"),
            ("000023", "2024-01-23", "Walter White", "M", "DSA145", True, "ABC123"),
            ("000024", "2024-01-24", "Xena Warrior", "F", "DSA146", False, "ABC125"),
            ("000025", "2024-01-25", "Yvonne Strahovski", "F", "DSA147", True, "ABC126"),
            ("000026", "2024-01-26", "Zachary Levi", "M", "DSA148", False, "ABC124"),
            ("000027", "2024-01-27", "Amanda Rollins", "F", "DSA149", True, "ABC123"),
            ("000028", "2024-01-28", "Barry Allen", "M", "DSA150", False, "ABC125"),
            ("000029", "2024-01-29", "Carrie Mathison", "F", "DSA151", True, "ABC126"),
            ("000030", "2024-01-30", "Dominic Toretto", "M", "DSA152", False, "ABC124"),
        ]
        for data in test_data:
            self.insert_absence(*data)

        self.print_student_absences("DSA123", "2024-01-01", "2024-01-31")
        self.print_module_absences("ABC123", "2024-01-01")
        self.plot_module_absences("ABC123", "2024-01-01", "2024-01-31")
        self.print_unauthorised_absences_by_date("2024-01-01")
        self.print_all_unauthorised_absences()
        self.delete_absence("000001")
        self.print_student_absences("DSA123", "2024-01-01", "2024-01-31")
