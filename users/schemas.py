from pydantic import EmailStr, BaseModel
from annotated_types import MinLen, MaxLen
from typing import Annotated

class CreateUserRequest(BaseModel):
    email: EmailStr
    login: Annotated[str, MinLen(3), MaxLen(10)]