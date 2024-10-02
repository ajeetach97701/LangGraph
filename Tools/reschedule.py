from Tools.availability_by_doctor import *
from Tools.availability_by_specialization import *


@tool
def reschedule_appointment(
    patient_name: str,
    desired_date: str,
    doctor_name: str,
    specialization: str,
    desired_time: str,
):
    """
    To reschedule an appointment which has already been scheduled to a new date


    """
    # pass
    patient_id = "adss"
    print("reschedule tool activated", desired_date, " ", desired_time)
    print("patient_id", patient_id)
    availability = pd.DataFrame()
    appointments_df = pd.read_excel("./Appointment/doctor_appointments.xlsx")
    appointment_to_reschedule = appointments_df[
        (appointments_df["patient_id"] == patient_id)
    ]
    if appointment_to_reschedule.empty:
        return f"Error: No appointment found for patient {patient_id}."
    original_date = f"{appointment_to_reschedule["appointment date time"].iloc[0]} {appointment_to_reschedule['appointment time'].iloc[0]}"
    print("original date", original_date)
    # doctor_name = appointment_to_reschedule["doctor_name"].iloc[0]
    # if specialization =="":
    desired_date_time = f"{desired_date}T{desired_time}"
    _, availability = availabilityy(
        desired_date=desired_date_time, doctor_name=doctor_name
    )
    availability_new = availability[["date_slot", "specialization", "doctor_name"]]
    print("availability", availability)
    print("availability_new--->", availability_new)
    if not availability.empty:
        appointments_df.loc[
            appointments_df["patient_id"] == patient_id,
            ["appointment time", "appointment date time"],
        ] = [desired_time, desired_date]

        # Write the updated appointment back to Excel
        appointments_df.to_excel("./Appointment/doctor_appointments.xlsx", index=False)

        message = update_availability_csv(
            original_date=original_date,
            desired_date=desired_date,
            desired_time=desired_time,
            patient_id=patient_id,
        )

        return f"Appointment rescheduled successfully for {desired_date} at {desired_time}.\n{message}"
    else:
        return f"Error: The time slot {desired_time} is not available for {doctor_name}. Please choose another slot."


def update_availability_csv(
    original_date, desired_date, desired_time,patient_id
):

    availability_csv_path = r"data/syntetic_data/availability.csv"
    df = pd.read_csv(availability_csv_path)
    desired_date_time = f"{desired_date} {desired_time}"

    df.loc[ df["date_slot"].str.contains(original_date),
        ["is_available", "patient_to_attend"]
    ] = [True, ""]

    # Update the new time slot to be unavailable (False) and assign the patient to attend
    df.loc[df["date_slot"].str.contains(desired_date_time),
        ["is_available", "patient_to_attend"],
    ] = [False, patient_id]

    # Write the updated DataFrame back to the CSV file
    df.to_csv(availability_csv_path, index=False)

    return "Doctor's availability updated successfully."
