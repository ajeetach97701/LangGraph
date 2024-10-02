from Tools.availability_by_doctor import *
from Tools.availability_by_specialization import *


@tool
def book_appointment(
    desired_date: str,
    desired_time: str,
    patient_name: str,
    doctor_name: str,
    patient_id: str,
):
    """
    When the user wants to book an appointment for a doctor at a specified time.

    """
    # patient_id = "abcded"
    # patient_id = "adss"
    # patient_name = "Ajeet Acharya"
    print("book tool activated", desired_date, " ", desired_time)
    print("patient_id", patient_id)
    availability = pd.DataFrame()
    specializations = pd.DataFrame()
    # if specialization =="":
    desired_date_time = f"{desired_date}T{desired_time}"
    _, availability = availabilityy(
        desired_date=desired_date_time, doctor_name=doctor_name
    )
    availability_new = availability[["date_slot", "specialization", "doctor_name"]]
    print("availability_new", availability_new)
    if len(availability) == 1:
        date_id_booking = availability.index[0]
        date_slot_booking = availability["date_slot"].iloc[0]
        time, date = date_slot_booking.split(" ")[0], date_slot_booking.split(" ")[1]
        time = desired_time.split(":")
        final_time = f"{time[0]}:{time[1]}"
        if final_time == desired_time:
            doctor_name_booking = availability["doctor_name"].iloc[0]
            specialization_booking = availability["specialization"].iloc[0]
            data = pd.DataFrame(
                {
                    "patient_id": [patient_id],
                    "doctor_time_id": [date_id_booking],
                    "patient_name": [patient_name],
                    "doctor_name": [doctor_name_booking],
                    "appointment date time": [desired_date],
                    "appointment time": [final_time],
                    "specialization": [specialization_booking],
                }
            )

            message = write_to_excel(
                data=data, date_id_booking=date_id_booking, patient_id=patient_id
            )
            print("Data written to Excel successfully!")
            return message
    else:
        return f"The time slot {desired_time} is not available for {doctor_name}. Please select one of the.\n {availability_new}"


def write_to_excel(data, date_id_booking, patient_id):
    data.to_excel(
        "./Appointment/doctor_appointments.xlsx"
    )  # 'index=False' prevents writing row numbers
    book_appointment_path = r"data/syntetic_data/availability.csv"
    df = pd.read_csv(book_appointment_path)
    column_no = date_id_booking - 2
    df.loc[column_no, "is_available"] = False
    df.loc[column_no, "patient_to_attend"] = patient_id
    df.to_csv(book_appointment_path, index=False)

    return "Booking has been made sucessfully"
