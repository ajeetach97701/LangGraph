from Libs.libs import *

class QueryInput(BaseModel):
    query: str = Field(description="Query to be passed as an argument. Always use this")
    senderId:str = Field(description="Query to be passed as an argument. Always use this")
    
class RagInput(BaseModel):
    query: str = Field(description="Query to be passed as an argument. Always use this")
   
    
    
class BookingInput(BaseModel):
    patient_id: str = Field(description="The patient id to be passed as an argument. Always use this")
    doctor_time_id: str = Field(description="Doctor appointment time to be passed as an argument. Always use this")
    patient_name: str = Field(description="patient time to be passed as an argument. Always use this")
    doctor_name: str = Field(description="doctor name to be passed as an argument. Always use this")
    time: str = Field(description="time to be passed as an argument. Always use this")
    specialization: str = Field(description="specialization to be passed as an argument. Always use this")
    
class DoctorSchema(BaseModel):
    desired_date:str = Field(description="The date in which the patients inquires about. The date format should always be YYYY-MM-DDTHH:MM to be passed as arguement")
    doctor_name:str = Field(description= "The name of the doctor to be passed as an arguement. Always use this")
    
class SpecializationSchema(BaseModel):
    desired_date:str = Field(description="The date in which the patients inquires about. The date format should always be YYYY-MM-DDTHH:MM to be passed as arguement")
    specialization:str = Field(description= "The Specialization of a doctor to be passed as an arguement. Always use this")
    
class bookingSchema(BaseModel):
    desired_date:str = Field(description="The date in which the patients inquires about. The date format should always be YYYY-MM-DD to be passed as arguement")
    desired_time:str = Field(description="The date in which the patients inquires about. The date format should always be HH:MM to be passed as arguement")
    doctor_name:str = Field(description= "The name of the doctor to be passed as an arguement. Always use this")
    
    

class AgentState(TypedDict):
    # The annotation tells the graph that new messages will always
    # be added to the current states
    messages: Annotated[Sequence[BaseMessage], operator.add]
    # The 'next' field indicates where to route to next
    next: str