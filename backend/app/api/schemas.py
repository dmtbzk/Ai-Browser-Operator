from pydantic import BaseModel

class chatResponse (BaseModel):
    answer: str

class chatRequest(BaseModel):
    message: str

