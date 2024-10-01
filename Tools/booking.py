from Tools.availability_by_doctor import *
from Tools.availability_by_specialization import *

@tool
def book_appointment(patient_name:str, patient_id:str, desired_date:str,  doctor_name):
    """
    used to book appointment with 
    """
    print("book tool activated")
    availability = pd.DataFrame()
    specializations = pd.DataFrame()
    # if specialization =="":
    print("from if")
    _, availability = availability_by_doctor(desired_date=desired_date, doctor_name=doctor_name)
    # print(availability)
    availability_new = availability[["date_slot","specialization","doctor_name"]]
    
    date_id_booking = availability.index[0]
    date_slot_booking = availability['date_slot'].iloc[0]
    time, date = date_slot_booking.split(" ")[0],  date_slot_booking.split(" ")[1]
    if time == desired_date.split('T')[1]:
        doctor_name_booking = availability['doctor_name'].iloc[0]
        specialization_booking = availability['specialization'].iloc[0]
        data = pd.DataFrame({
            "patient_id":[patient_id],
            "doctor_time_id":[date_id_booking],
            "patient_name":[patient_name],
            "doctor_name":[doctor_name_booking],
            "appointment date time":[time],
            "appointment time":[date],
            "specialization":[specialization_booking]
        })
        data.to_excel("./Appointment/doctor_appointments.xlsx")  # 'index=False' prevents writing row numbers
        print("Data written to Excel successfully!")
        return "Booking has been made sucessfully"
        # else:
        #     return f"No available slots for booking at time{desired_date}. Here are some of the available slots. Which would you like to choose?.\n {availability_new}"
    # elif doctor_name == "":
    #     print("from else if")
    #     _, specializations= availability_by_specialization(desired_date=desired_date, specialization=specialization)
    #     print(specializations)
    #     return specializations
    # else:
    #     print("from else")
    #     _, availability = availability_by_doctor(desired_date=desired_date, doctor_name=doctor_name)
    #     _, specializations= availability_by_specialization(desired_date=desired_date, specialization=specialization)
        
        # return availability, specializations
    # app = patient_name + " " + desired_date + " "+ doctor_name + " " + specialization + " " + desired_time
    # print("app")
    
    # return "Booked "
