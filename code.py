from asyncio import constants
from turtle import back, fillcolor
import qrcode

def qrCodeGen(txt):

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    qr.add_data(txt)
    qr.make(fit=True)
    img = qr.make_image(fillcolor="black", back_color = "white")
    img.save("code.png")

url = input("Enter URL: ")

qrCodeGen(url)

print("Code Generated Successfully!")

