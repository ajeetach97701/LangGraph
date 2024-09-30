from langchain_core.tools import tool

from Tools.Schema import DateModel
from typing   import Literal
import pandas as pd

@tool
def check_availability_by_doctor():
    # desired_date, doctor_name:Literal['kevin anderson','Ajeet','Rajesh','Shiva','Ganesh',]):
    """
    Check the availability of the doctor with the name and date provided
    """
    doctor_name = "kevun anderson"
    desired_date = "2024-09-03"
    print("Tool entered")
    df = pd.read_csv(f"./data/syntetic_data/availability.csv")
    availability = df[(df['date_slot'].apply(lambda x: x.split(' ')[0]) == desired_date.date) & (doctor_name == df['doctor_name'])&(df['is_available'] == True)]["date_slot"]
    if len(availability) == 0:
        return "Doctor not available for the day"
    else:
        outpur = f"Availablity for the doctor{doctor_name}is+ ""+{availability}".join(availability)
        return outpur

from Libs.libs import llm

@tool
def mercedes_tool(text:str):
    """
    A tool that is used to answer all the queries related to mercedes.
    """
    # df = pd.read_csv(f"./data/syntetic_data/availability.csv")
    # rows = df[(df['date_slot'].apply(lambda input: input.split(' ')[0]) == desired_date.date) & (df['specialization'] == specialization) & (df['is_available'] == True)].reset_index()
    # available_specialization = rows[['date_slot', 'specialization', 'doctor_name']]    
    # if len(available_specialization) == 0:
    #     return f"No doctors are available for {available_specialization}"    
    # else:
    #     output = "availability for the doctor"
    #     for index, row in available_specialization.iterrows():
    #         output += f"\n{row['date_slot']}"
    
    return llm.invoke(text)


@tool
def check_availability_by_specialization(desired_date:DateModel, specialization:Literal['General', "ENT","Dentist","orthodontist"]):
    """
    Check the availability of the doctor with specialization and date provided.
    """
    df = pd.read_csv(f"./data/syntetic_data/availability.csv")
    rows = df[(df['date_slot'].apply(lambda input: input.split(' ')[0]) == desired_date.date) & (df['specialization'] == specialization) & (df['is_available'] == True)].reset_index()
    available_specialization = rows[['date_slot', 'specialization', 'doctor_name']]    
    if len(available_specialization) == 0:
        return f"No doctors are available for {available_specialization}"    
    else:
        output = "availability for the doctor"
        for index, row in available_specialization.iterrows():
            output += f"\n{row['date_slot']}"
        
        return output
    

