import qrcode

# Text to encode in QR code
data = input('azeqsd:')

# Create QR code instance
qr = qrcode.QRCode(version=1, box_size=15, border=4)

# Add data to QR code instance
qr.add_data(data)

# Generate QR code image
qr.make(fit=True)

# Get QR code image
img = qr.make_image(fill_color="black", back_color="white")

# Save QR code image
img.save("qrcode.png")
