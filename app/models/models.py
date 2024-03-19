from pydantic import BaseModel, PositiveInt
from typing import List


class TwoListTarget(BaseModel):
    list_a: List[PositiveInt]
    list_b: List[PositiveInt]
    target: PositiveInt
