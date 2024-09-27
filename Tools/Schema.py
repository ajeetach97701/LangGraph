from Libs.libs import *

class QueryInput(BaseModel):
    query: str = Field(description="Query to be passed as an argument. Always use this")
    