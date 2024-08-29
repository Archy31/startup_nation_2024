from pydantic import BaseModel, ValidationError, EmailStr, Field
from pprint import pprint


class User(BaseModel):
    username: str
    email: EmailStr | None = Field(default=None)
    password: str


inp = """{
    "username": "Kairat",
    "email": "kubanychbekukairat",
    "password": "Kairat123"
    }"""

try:
    val = User.model_validate_json(inp)

except ValidationError as e:
    pprint(e.json(indent=2))

else:
    print(type(val.password))