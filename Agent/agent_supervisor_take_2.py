from Libs.libs import llm
from langchain_core.tools import tool
from Libs.libs import *
from Tools.Schema import DateModel
from typing   import Literal
import pandas as pd

@tool
def check_availability_by_doctor(desired_date:str, doctor_name:Literal['kevin anderson','robert martinez','susan davis','daniel miller','sarah wilson','michael green','lisa brown','jane smith','emily johnson','john doe']):
    # desired_date, doctor_name:Literal['kevin anderson','Ajeet','Rajesh','Shiva','Ganesh',]):
    """
    Check the availability of the doctor with the name and date provided
    """
    # print(desired_date)
    desired_date_split = desired_date.split("T") or desired_date
    print("desired date is:",desired_date)
    df = pd.read_csv(f"./data/syntetic_data/availability.csv")
    date =  desired_date_split[0] 
    time = desired_date_split[1] if len(desired_date_split) > 1 else "" 
    # query = doctor_name+ " for " + date + " at time: " +time
    query = doctor_name+ " for " + date + "," +time

    print()
    print()
    print("Tool entered with the query", query)
    print()
    print()
    availability = df[(df['date_slot'].apply(lambda x: x.split(' ')[0]) == date) & (doctor_name == df['doctor_name'])&(df['is_available'] == True)]
    # print(availability)
    template = """
    You have to answer the user query which is about the availability of a doctor inquired by patient. You are also given a context that contains the doctors available in that day and a time slot. Analyze and return the doctor name, date and available time slot. 
        Context inside double backticks:`{context}`
        Question inside triple backticks:{question}
        Response in markdown format without any backticks and in the context phrase just answer what is asked and if the doctor is not available for a particular time slot, recomend the other time slots.

        Your response should be very much conversational in such a way that you are a receptionist talking to a patient who is here to schedule an appointment.
        """
    prompt = ChatPromptTemplate.from_template(template)
    # print("context>>>>>>>>>>>>>>>>",database.similarity_search(query,k=5))
    chain = RunnableMap({
        "context":lambda x: availability,
        "question": lambda x: x['question']
    }) | prompt | llm | string_parser
    result = chain.invoke({'question':query})
    print("------------")
    mdprint(result)
    print("------------")
    return {"messages":result} 
    
    
    # outpur = ""
    # if len(availability) == 0:
    #     outpur = "Doctor not available for the day"
    #     return llm.invoke(input=f"Your should return this text in a markdown format in a good language No doctors are available for {availability}"  )
    # else:
    #     outpur = f"Availablity for the doctor {doctor_name}is+ ""+{availability}".join(availability)
    #     return llm.invoke(input=f"Your should return this text in a markdown format in a good language No doctors are available for {outpur}"  )

    # return outpur



@tool
def check_availability_by_specialization(desired_date:str, specialization:Literal["general_dentist", "cosmetic_dentist", "prosthodontist", "pediatric_dentist","emergency_dentist","oral_surgeon","orthodontist"]):
    """
    Check the availability of the doctor with specialization and date provided.
    """
    # specialization = "orthodontist"
    # desired_date = "2024-09-03"
    desired_date_split = desired_date.split("T") or desired_date

    date =  desired_date_split[0] 
    time = desired_date_split[1] if len(desired_date_split) > 1 else "" 
    df = pd.read_csv(f"./data/syntetic_data/availability.csv")
    rows = df[(df['date_slot'].apply(lambda input: input.split(' ')[0]) == date) & (df['specialization'] == specialization) & (df['is_available'] == True)].reset_index()
    available_specialization = rows[['date_slot', 'specialization', 'doctor_name']] 
      
    query = specialization+ " for " + date + "," +time
    print()
    print()
    print("Tool entered with the query", query)
    print()
    print()

    # print(availability)
    template = """
    You have to answer the user query in which patient is searching for a doctor of a particular specialization which is given in the query. You are also given a context that contains the doctors available in that day and a time slot. Analyze and return the doctor name, date and available time slot along with the specialization. 
        Context inside double backticks:`{context}`
        Question inside triple backticks:{question}
    Response in markdown format without any backticks and in the context phrase just answer what is asked and if the doctor is not available for a particular time slot, recomend the other time slots.
    Your response should be very much conversational in such a way that you are a receptionist talking to a patient who is here to schedule an appointment.

        """
    prompt = ChatPromptTemplate.from_template(template)
    # print("context>>>>>>>>>>>>>>>>",database.similarity_search(query,k=5))
    chain = RunnableMap({
        "context":lambda x: available_specialization,
        "question": lambda x: x['question']
    }) | prompt | llm | string_parser
    result = chain.invoke({'question':query})
    mdprint(result)
    return {"messages":result} 
   
    

@tool
def book_appointment(patient_name:str,desired_date:str, doctor_name:str, specialization:str, desired_time:str):
    """
    To schedule an appointment for a particular date, time.
    """
    print("Booking appointment tool")
    app = patient_name + " " + desired_date + " "+ doctor_name + " " + specialization + " " + desired_time
    print(app)
    
    return app


@tool
def reschedule_appointment(patient_name:str,patient_id:str,desired_date:str, doctor_name:str, specialization:str, desired_time:str):
    """
    To reschedule an appointment which has already been scheduled to a new date
    """
    pass


