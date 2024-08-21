from uuid import UUID

from pydantic import BaseModel, Field


class DemoScheme(BaseModel):
    uid: UUID
    type_: str = Field(..., alias="type")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class CreateDemoScheme(BaseModel):
    type_: str = Field(..., alias="type")
