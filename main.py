import pyqrcode  
from pyqrcode import QRCode  
data = "https://www.orioninsist.org/"  
qr_code = pyqrcode.create(data)  
filename = "qr_code.png"  
qr_code.png(filename, scale=8)  
print("QR code was created and", filename, "saved to file.")