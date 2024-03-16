from pydantic import BaseModel
from typing import List

class InputPayload(BaseModel):
    list_a : List[int]
    list_b : List[int]
    target: int