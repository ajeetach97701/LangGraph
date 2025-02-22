DELETE_HISTORY_QUERYS = ['lead', "clear", "restart", "reset"]

from pydantic import BaseModel, Field
from typing import Literal, Union

class GreetingResponse(BaseModel):
    type: Literal["handle_greetings", "assistant"]
