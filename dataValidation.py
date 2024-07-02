from pydantic import BaseModel

class Kisi(BaseModel):
    adi: str
    yasi: int
    email: str

# ornek olusturma
kisi = Kisi(adi = "Mehmet", yasi = 21, email = "mehmet@gmail.com")

print(kisi)
print(kisi.dict())
print(kisi.adi)
print(kisi.yasi)
print(kisi.email)

print("")
print("Unpacking Dictionary")
print("")

kisi_bilgi = {"adi": "Mustafa", "yasi": 21, "email": "mustafa@gmail.com"}
kisi_2 = Kisi(**kisi_bilgi)

print(kisi_2.adi)
print(kisi_2.yasi)
print(kisi_2.email)


print("Data Validation")
#hatayi göstermek amacli yas string olarak girildi
kisi3 = Kisi(adi = "Mehmet", yasi = "12y", email = "mehmet@gmail.com")
print(kisi3.yasi)