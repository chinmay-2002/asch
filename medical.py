# Hospital Management Expert System - Medical Facilities

# Initialize variables
medical_facilities = {
    "Cardiology": {
        "Available Doctors": ["Dr. Smith", "Dr. Johnson"],
        "Available Equipment": ["ECG machine", "Echocardiogram machine"],
        "Special Procedures": ["Angiography", "Cardiac catheterization"]
    },
    "Radiology": {
        "Available Doctors": ["Dr. Brown", "Dr. Davis"],
        "Available Equipment": ["X-ray machine", "MRI machine"],
        "Special Procedures": ["CT scan", "Ultrasound"]
    },
    "Laboratory": {
        "Available Technicians": ["John", "Sarah"],
        "Available Equipment": ["Microscope", "Centrifuge"]
    }
}

# Function to display available medical facilities
def display_medical_facilities():
    print("Available Medical Facilities:")
    for facility, details in medical_facilities.items():
        print("Facility:", facility)
        print("Available Doctors/Technicians:", ", ".join(details["Available Doctors"]) if "Available Doctors" in details else "N/A")
        print("Available Equipment:", ", ".join(details["Available Equipment"]) if "Available Equipment" in details else "N/A")
        print("Special Procedures:", ", ".join(details["Special Procedures"]) if "Special Procedures" in details else "N/A")
        print("-------------------------")

# Function to search for available medical facilities by name
def search_medical_facilities():
    facility_name = input("Enter medical facility name to search: ")

    if facility_name in medical_facilities:
        details = medical_facilities[facility_name]
        print("Facility:", facility_name)
        print("Available Doctors/Technicians:", ", ".join(details["Available Doctors"]) if "Available Doctors" in details else "N/A")
        print("Available Equipment:", ", ".join(details["Available Equipment"]) if "Available Equipment" in details else "N/A")
        print("Special Procedures:", ", ".join(details["Special Procedures"]) if "Special Procedures" in details else "N/A")
        print("-------------------------")
    else:
        print("Medical facility not found.")

# Main menu function
def main_menu():
    print("Hospital Management Expert System - Medical Facilities")
    print("--------------------------------")
    print("1. Display Available Medical Facilities")
    print("2. Search Medical Facilities")
    print("3. Exit")
    choice = int(input("Enter your choice (1-3): "))

    if choice == 1:
        display_medical_facilities()
    elif choice == 2:
        search_medical_facilities()
    elif choice == 3:
        print("Exiting the program...")
        return
    else:
        print("Invalid choice. Please try again.")

    print()  # Add a line break
    main_menu()

# Start the program
main_menu()
