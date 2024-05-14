import pyqrcode
from PIL import Image, ImageTk
import tkinter as tk

window = tk.Tk()
window.geometry('300x400')
window.title('QR Code Generator')

label = tk.Label(window, text='Let’s Create QR Code', font='arial 15')
label.pack()

entry = tk.Entry(window, font='arial 15')
entry.pack()


def create_qrcode():
    qr_data = entry.get()
    qr = pyqrcode.create(qr_data)
    qr.png('myqr.png', scale=6)

    # Load the generated QR code image using PIL
    qr_image = Image.open('myqr.png')
    qr_image = qr_image.resize((200, 200), Image.ANTIALIAS)  # Resize the image
    qr_photo = ImageTk.PhotoImage(qr_image)

    # Display the QR code image using a Label widget
    qr_label = tk.Label(window, image=qr_photo)
    qr_label.image = qr_photo  # Keep a reference to prevent garbage collection
    qr_label.pack()

    result_label = tk.Label(window, text='QR Code is created and displayed successfully')
    result_label.pack()


create_button = tk.Button(window, text='Create', bg='pink', command=create_qrcode)
create_button.pack()

window.mainloop()
