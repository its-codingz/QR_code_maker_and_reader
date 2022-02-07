import qrcode
import cv2

value = input("Enter the value for which QR code is to be made: ")
img = qrcode.make(value)
img.save("Output.png")

d = cv2.QRCodeDetector()
val , points , staright_qrcode = d.detectAndDecode(cv2.imread("Output.png"))
print("Value obtained from QR code: ",val)