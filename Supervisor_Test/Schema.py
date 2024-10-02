from Libs.libs import *

class QueryInput(BaseModel):
    query: str = Field(description="Query to be passed as an argument. Always use this")
    
    
class BookingInput(BaseModel):
    patient_id: str = Field(description="The patient id to be passed as an argument. Always use this")
    doctor_time_id: str = Field(description="Doctor appointment time to be passed as an argument. Always use this")
    patient_name: str = Field(description="patient time to be passed as an argument. Always use this")
    doctor_name: str = Field(description="doctor name to be passed as an argument. Always use this")
    time: str = Field(description="time to be passed as an argument. Always use this")
    specialization: str = Field(description="specialization to be passed as an argument. Always use this")
    
    
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