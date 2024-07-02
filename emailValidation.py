from pydantic import BaseModel, EmailStr

class Kisi(BaseModel):
    adi: str
    yasi: int
    email: EmailStr

print("Email Validation")
kisi_bilgi4 = {"adi": "Mustafa", "yasi": 21, "email": "mustafa@gmail"}
kisi_4 = Kisi(**kisi_bilgi4)
print(kisi_4.adi)
print(kisi_4.yasi)
print(kisi_4.email)