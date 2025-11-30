from pydantic import BaseModel
from typing import List, Optional

class UserRequest(BaseModel):
    user_id: str
    message: str

class UserResponse(BaseModel):
    response_id: str
    message: str
    timestamp: str

class Rule(BaseModel):
    rule_id: str
    description: str
    applicable_conditions: List[str]

class MemoryEntry(BaseModel):
    entry_id: str
    user_id: str
    data: dict
    timestamp: str

class ErrorResponse(BaseModel):
    error_code: int
    error_message: str

class SuccessResponse(BaseModel):
    success: bool
    data: Optional[dict] = None
    message: Optional[str] = None