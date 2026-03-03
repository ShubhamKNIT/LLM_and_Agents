from pydantic import BaseModel, Field
from typing import Dict, List

class TOCSchema(BaseModel):
    toc: Dict[str, List[int]] = Field(
        description="A dictionary mapping chapter/unit names to a list [start_page, end_page]"
    )