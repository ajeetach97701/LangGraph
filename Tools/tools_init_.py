from Tools.Schema import *
from Libs.libs import *
from Tools.booking import *
from Tools.reschedule import *
from Tools.availability_by_doctor  import *
from Tools.availability_by_specialization import *

class GetCustomTools():
    tools = []
    def __init__(self, params=None):
        self.params = params
        self.initialize_tools()

    def initialize_tools(self):
    
        booking_tool = StructuredTool.from_function(name='bookingTool',
                                                      func=book_appointment(self.params),
                                                      description="A tool that is used to book an appointment with the Doctor.",
                                                      args_schema=bookingSchema)
        
        check_doctor =  StructuredTool.from_function(name='checkDoctorAvailabilityTool',
                                                      func=check_availability_by_doctor(self.params),
                                                      description="A tool that is used check the availability of a doctor at a particular date and time, given the  doctor's name.",
                                                      args_schema=DoctorSchema)
        check_spec =  StructuredTool.from_function(name='CheckSpecializationTool',
                                                      func=check_availability_by_specialization(self.params),
                                                      description="A tool that is used check the availability of a doctor at a particular date and time given the specialization ",
                                                      args_schema=SpecializationSchema)
        
        reschedule_tool =  StructuredTool.from_function(name='rescheduleTime',
                                                      func=reschedule(self.params),
                                                      description="A tool that is used check the availability of a doctor at a particular date and time given the specialization ",
                                                      args_schema=bookingSchema)
        
        self.tools = [
            booking_tool, 
            check_doctor,
            reschedule_tool,
            check_spec]

    def get_tools(self):
        return self.tools

    def get_tools_names(self):
        return [tool.name for tool in self.tools]

        