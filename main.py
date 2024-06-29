from tkinter import *
from PIL import ImageTk, Image
import customtkinter as ctk
import os

root = Tk()
root.title("Image Editor")
root.geometry('1080x720')

root.columnconfigure((0,1,2,3,4), weight = 1, uniform = 'a')
root.rowconfigure(0, weight = 1)

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
folder = f"{location}\\images\\"
icon = f"{location}\\src\\icon.ico"
root.iconbitmap(icon)

img_list = [folder + img for img in os.listdir(folder)]
leng = len(img_list) - 1
i = 0

ImageFrame = Canvas(root, background= 'black', bd=0, highlightthickness=0, relief='ridge')
ButtonFrame = Frame(root)

def img_update():
    global resized_tk

    image_original = Image.open(img_list[i])
    ImageFrame_ratio = image_original.width / image_original.height

    frame_width = ImageFrame.winfo_width()
    frame_height = ImageFrame.winfo_height()

    if frame_width / frame_height > ImageFrame_ratio:
        width = int(frame_height * ImageFrame_ratio)
        height = frame_height
    else:
        height = int(frame_width / ImageFrame_ratio)
        width = frame_width

    resized_image = image_original.resize((width, height))
    resized_tk = ImageTk.PhotoImage(resized_image)

    ImageFrame.delete("all")
    ImageFrame.create_image(frame_width//2, frame_height//2, anchor='center', image=resized_tk)

    status.config(text=f"Image {i + 1} of {leng + 1}")

def fill(img):
    global resized_tk

    image_original = Image.open(img_list[i])

    ImageFrame_ratio = img.width / img.height

    ImageFrame.delete("all")

    if ImageFrame_ratio > image_ratio:
        width = int(img.width)
        height = int(width / image_ratio)
    else:
        height = int(img.height)
        width = int(height * image_ratio)

    resized_image = image_original.resize((width, height))
    resized_tk = ImageTk.PhotoImage(resized_image)

    ImageFrame.grid(row=0, column=2, columnspan=3, sticky= NSEW)
    ButtonFrame.grid(row=0, column=0, sticky= NSEW)

    ImageFrame.create_image(int(img.width/2),
                            int(img.height/2),
                            anchor = 'center',
                            image = resized_tk
                                )

def frontF():
    global i
    global image_original
    i += 1
    
def backF():
    global i
    global image_original
    i -= 1
    
image_original = Image.open(img_list[i])
image_ratio = image_original.size[0] / image_original.size[1]

image_tk = ImageTk.PhotoImage(image_original)

ImageFrame.bind('<Configure>', lambda event: img_update())

if i == 0:
    back = ctk.CTkButton(ButtonFrame, text="<", state=DISABLED)
else:
    back = ctk.CTkButton(ButtonFrame, text="<", command=backF)
back.pack(pady=10)

if i == leng:
    front = ctk.CTkButton(ButtonFrame, text=">", state=DISABLED)
else:
    front = ctk.CTkButton(ButtonFrame, text=">", command=frontF)
front.pack(pady=10)

status = Label(ButtonFrame, text=f"image {i + 1} of {leng + 1}")
status.pack(pady=10)

leave = ctk.CTkButton(ButtonFrame, text="Close app", command=exit)
leave.pack(pady=200)

ImageFrame.grid(row=0, column=2, columnspan=3, sticky= NSEW)
ButtonFrame.grid(row=0, column=0, sticky= NSEW)

root.mainloop()