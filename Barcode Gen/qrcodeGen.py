import qrcode as qc
import tkinter
import random, string
import csv
import array
import cv2


password = input("Enter the Password: ")
authenticate = qc.make(password)
authenticate.save("password.jpeg")


d = cv2.QRCodeDetector()
val, points, straight_qrcode = d.detectAndDecode(cv2.imread("password.jpeg"))
print(val)
