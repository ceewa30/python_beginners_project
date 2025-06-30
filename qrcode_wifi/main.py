from wifi_qrcode_generator.generator import wifi_qrcode
from PIL import Image

ssid = "Your WiFi Network"
password = "Your WiFi Password"
security = "WPA"
# Generate a QR code for Wi-Fi credentials
# ssid='Home WiFi', hidden=False, authentication_type='WPA', password='very complicated password'
qr = wifi_qrcode(ssid, False, security, password)
qr_image = qr.make_image(fill_color="black", back_color="white")
qr_image.save("wifi_qr_code.png")
# Display the QR code image
qr_image.show()
# The above code generates a QR code for Wi-Fi credentials and saves it as an image file.
# The QR code can be scanned by devices to connect to the Wi-Fi network without manually entering the credentials.