from pydantic import BaseModel, validator, Field

class UserModel(BaseModel):
    name: str
    email: str
    password: str
    confirmPassword: str = Field(exclude=True)  # Add confirmPassword field

    @validator('confirmPassword')
    def passwords_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError('Passwords do not match')
        return v

class TokenModel(BaseModel):
    user_id: str
    token: str
    created_at: str

class LoginModel(BaseModel):
    email: str
    password: str

