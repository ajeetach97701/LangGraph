# from Libs.libs import llm
# from langchain_core.tools import tool
# from Libs.libs import *
# from models.Schema import DateModel
# from typing   import Literal
# import pandas as pd


# def availability_by_specialization(desired_date:str, specialization:str):
#     desired_date_split = desired_date.split("T") or desired_date

#     date =  desired_date_split[0] 
#     time = desired_date_split[1] if len(desired_date_split) > 1 else "" 
#     df = pd.read_csv(f"./data/syntetic_data/availability.csv")
#     rows = df[(df['date_slot'].apply(lambda input: input.split(' ')[0]) == date) & (df['specialization'] == specialization) & (df['is_available'] == True)].reset_index()
#     available_specialization = rows[['date_slot', 'specialization', 'doctor_name']] 
      
#     query = specialization+ " for " + date + "," +time
#     print()
#     print()
#     print("Tool entered with the query", query)
#     print()
#     print()
#     return query, available_specialization
    

# @tool
# def check_availability_by_specialization(desired_date:str, specialization:Literal["general_dentist", "cosmetic_dentist", "prosthodontist", "pediatric_dentist","emergency_dentist","oral_surgeon","orthodontist"]):
#     """
#     Check the availability of the doctor with specialization and date provided.
#     """
#     print("from check availability by doctor tool")
#     # specialization = "orthodontist"
#     # desired_date = "2024-09-03"
    
#     query, available_specialization = availability_by_specialization(desired_date=desired_date, specialization=specialization)
#     # print(availability)
#     template = """
#     You have to answer the user query in which patient is searching for a doctor of a particular specialization which is given in the query. You are also given a context that contains the doctors available in that day and a time slot. Analyze and return the doctor name, date and available time slot along with the specialization. 
#         Context inside double backticks:`{context}`
#         Question inside triple backticks:{question}
#     Response in markdown format without any backticks and in the context phrase just answer what is asked and if the doctor is not available for a particular time slot, recomend the other time slots.
#     Your response should be very much conversational in such a way that you are a receptionist talking to a patient who is here to schedule an appointment.

#         """
#     prompt = ChatPromptTemplate.from_template(template)
#     # print("context>>>>>>>>>>>>>>>>",database.similarity_search(query,k=5))
#     chain = RunnableMap({
#         "context":lambda x: available_specialization,
#         "question": lambda x: x['question']
#     }) | prompt | llm | string_parser
#     result = chain.invoke({'question':query})
#     mdprint(result)
#     return {"messages":result} 
   
    


