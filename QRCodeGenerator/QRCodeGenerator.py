import qrcode

# Make Instance Of QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add Some Data To Our QR Code (You Can Add Any Stuff)
data = "https://www.isamirmmd.ir"
qr.add_data(data)
qr.make(fit=True)

# Make An Image From The QR Code
image = qr.make_image(fill_color="black", back_color="white")

# Save The QR Code Image
imageSaveAs = "QRCode_Output.png"
image.save(imageSaveAs)

# Display The Image OF That QR Code
image.show()