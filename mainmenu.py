import os

class MainMenu:
    def __init__(self, finder, register, printAll):
        self.finder = finder
        self.register = register
        self.printAll = printAll
        self.menu_options = {
            1: self.view_personal_info,
            2: self.search_student,
            3: self.register_student,
            4: self.print_all_students,
            5: self.exit_system
        }

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def login(self):
        self.finder.data.read()
        attempts = 0
        max_attempts = 3
        while attempts < max_attempts:
            print("\n" + "-"*10, "Login - Student Info. System", "-"*10)
            verify = input("Student ID: ")
            user = self.finder.verify_login(verify)
            if user:
                self.main_menu(user)
                return
            else:
                self.clear_screen()
                attempts += 1
                print(f"\nThe student with ID number {verify} is not valid.")
                print(f"Attempts left: {max_attempts - attempts}")
        
        self.clear_screen()
        print("\n" + "-"*10, "Login Error - Student Info. System", "-"*10)
        print("You have exceeded the number of attempts allowed.")
        print("Exiting the System. Sorry, try again later.")

    def main_menu(self, user):
        while True:
            self.clear_screen()
            print(f"Hello Welcome, {user.getName()}!")
            print("-"*15, "Main Menu", "-"*15)
            print("[1] View your information")
            print("[2] View other student's information")
            print("[3] Register a new student")
            print("[4] Print all students in the system")
            print("[5] Exit")
            
            try:
                choice = int(input("Your choice: "))
                if choice in self.menu_options:
                    self.menu_options[choice](user)
                else:
                    print("Invalid option. Please try again.")
                    input("Press Enter to continue...")
            except ValueError:
                print("Invalid input. Please enter a number.")
                input("Press Enter to continue...")

    def view_personal_info(self, user):
        self.clear_screen()
        print("="*16, "YOUR INFO", "="*16)
        print(f"{user}")
        print("="*13, "END", "="*13)
        input("\nPress Enter to go back to the main menu.")

    def search_student(self, user):
        while True:
            self.clear_screen()
            print("-"*10, "Search Student Information", "-"*10)
            id = input("\nEnter student ID Number: ")
            print(self.finder.search_student(id))
            if input("\nDo you want to search again? (Y/N) ").lower() != "y":
                break

    def register_student(self, user):
        while True:
            self.clear_screen()
            self.register.input_add_student()
            if input("Do you want to add another student to the list? (Y/N) ").lower() != "y":
                break

    def print_all_students(self, user):
        self.clear_screen()
        self.printAll.printAllStudents()
        input("Press Enter to go back to the main menu.")

    def exit_system(self, user):
        self.clear_screen()
        print("-"*10, "Logging off", "-"*10)
        print("Logging out. GOODBYE")
        exit()
