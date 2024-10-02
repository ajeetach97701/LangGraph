from Libs.libs import *

class QueryInput(BaseModel):
    query: str = Field(description="Query to be passed as an argument. Always use this")
    senderId:str = Field(description="Query to be passed as an argument. Always use this")
    
    
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
    
    
   
    
    

class DateModel(BaseModel):
    """
    The way the date should be structured and formatted
    """
    date: str = Field(..., description="Propertly formatted date", pattern=r'^\d{4}-\d{2}-\d{2}$')

    @field_validator("date")
    def check_format_date(cls, v):
        if not re.match(r'^\d{4}-\d{2}-\d{2}$', v):
            raise ValueError("The date must be in the format 'YYYY-MM-DD'")
        return v