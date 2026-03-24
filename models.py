from pydantic import BaseModel
from typing import List, Optional


class Project(BaseModel):
    id: str
    title: str
    deleted: Optional[bool] = None


class ProjectsList(BaseModel):
    content: List[Project]
