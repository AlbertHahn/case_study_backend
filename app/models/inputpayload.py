from pydantic import BaseModel, PositiveInt
from typing import List


class InputPayload(BaseModel):
    list_a: List[PositiveInt]
    list_b: List[PositiveInt]
    target: PositiveInt

    class Config:
        from_attributes = True
