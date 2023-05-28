class Patient:
    def __init__(self, name, age, gender, phone):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.appointments = []

    def add_appointment(self, appointment):
        self.appointments.append(appointment)


class Appointment:
    def __init__(self, patient, doctor, date):
        self.patient = patient
        self.doctor = doctor
        self.date = date


class Hospital:
    def __init__(self):
        self.patients = []
        self.doctors = []

    def register_patient(self, name, age, gender, phone):
        patient = Patient(name, age, gender, phone)
        self.patients.append(patient)
        return patient

    def schedule_appointment(self, patient, doctor, date):
        appointment = Appointment(patient, doctor, date)
        patient.add_appointment(appointment)
        return appointment

    def display_patient_appointments(self, patient):
        print(f"Appointments for {patient.name}:")
        for appointment in patient.appointments:
            print(f"Doctor: {appointment.doctor}, Date: {appointment.date}")


if __name__ == '__main__':
    hospital = Hospital()

    # Patient registration
    patient1 = hospital.register_patient("John Doe", 30, "Male", "1234567890")
    patient2 = hospital.register_patient("Jane Smith", 25, "Female", "9876543210")

    # Schedule appointments
    appointment1 = hospital.schedule_appointment(patient1, "Dr. Johnson", "2023-06-01")
    appointment2 = hospital.schedule_appointment(patient1, "Dr. Smith", "2023-06-05")
    appointment3 = hospital.schedule_appointment(patient2, "Dr. Anderson", "2023-06-03")

    # Display patient appointments
    hospital.display_patient_appointments(patient1)
    hospital.display_patient_appointments(patient2)
