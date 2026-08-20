from pydantic import BaseModel, Field
from datetime import datetime

class HealthCheckResponse(BaseModel):
    status: str



class ProcessFrameResponse(BaseModel):
    status: str = Field(..., json_schema_extra={"example": "success"})
    filename: str = Field(..., json_schema_extra={"example": "classroom.jpg"})
    faces_detected: int = Field(
        ...,
        ge=0,
        description="Number of faces (students) detected",
        json_schema_extra={"example": 5}
    )
    timestamp: datetime = Field(default_factory=datetime.now, description="Processing time")