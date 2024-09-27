from Libs.libs import *

class QueryInput(BaseModel):
    query: str = Field(description="Query to be passed as an argument. Always use this")
    organization_name:str = Field(description="organization name to be passed as an argument. Always use this")
    