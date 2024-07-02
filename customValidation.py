from pydantic import BaseModel, EmailStr, validator

class Kisi(BaseModel):
    adi: str
    yasi: int
    email: EmailStr

    @validator("yasi")
    def check_age(cls, v):
        if v < 0:
            raise ValueError("Age must be a positive number")
        return v

kisi_bilgi = {"adi": "Musa", "yasi": -12, "email": "musa@gmail.com"}
kisi_bilgi = Kisi(**kisi_bilgi)
print(kisi_bilgi)