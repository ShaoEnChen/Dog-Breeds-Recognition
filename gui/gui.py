# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import numpy as np
import json
from keras.models import load_model

img_size = 224
text_wrap_length = 840

model_file = 'model.h5'
uploaded_img = None
breeds = {}

# Load dictionary of dog breed introductions
with open('breed_classes.json') as f:
    classes = json.load(f)

for key, val in classes.items():
    breeds[val] = key

def rescaleImg(img):
    # Scale and center image to fit canvas (longer side has length 300)
    w, h = img.size
    if w > h:
        scale = 300 / w
        x_shift = 0
        y_shift = int(150 - h * scale / 2)
    else:
        scale = 300 / h
        x_shift = int(150 - w * scale / 2)
        y_shift = 0

    rescaled_img = img.resize((int(w * scale), int(h * scale)))

    return rescaled_img, x_shift, y_shift

def uploadImg():
    global uploaded_img

    # Upload the image, and show it on screen
    try:
        f = askopenfilename(filetypes = [("jpeg files", "*.jpg")])
        img = Image.open(f)
        uploaded_img = img
    except:
        return

    imgfile, x_shift, y_shift = rescaleImg(img)
    imgfile = ImageTk.PhotoImage(imgfile)
    image_canvas.image = imgfile
    image_canvas.create_image(x_shift, y_shift, anchor = 'nw', image = imgfile)

def predict():
    global uploaded_img
    input_img = uploaded_img.resize((224, 224))
    img_array = np.asarray(input_img)

    shape = img_array.shape
    img_array = img_array.reshape(1, shape[0], shape[1], shape[2])
    img_array = img_array.astype('float32')
    img_array /= 255.0

    model = load_model(model_file)
    breed_idx = model.predict_classes(img_array)[0]

    introduction.configure(text = "This is a %s !" %(breeds[breed_idx]))

# Initiate the window
window = tk.Tk()
window.title('Dog Breed Classification')
window.geometry('960x540')

# ROW 1
# Set title in the window content
main_title = tk.Label(window, text = 'Dog Breeds Recognizer', font = ('', 30), pady = 20)
main_title.pack()

# ROW 2
# Set image display areas
images_frame = tk.Frame(window)
images_frame.pack()

image_canvas = tk.Canvas(images_frame, width = img_size, height = img_size, bd = 0)
image_canvas.create_text(150, 150, text = 'Your image will be displayed here.')
image_canvas.pack()

# ROW 3
# Set two functional buttons
buttons_frame = tk.Frame(window)
buttons_frame.pack()

upload_image_button = tk.Button(buttons_frame, text = 'Open', pady = 20, command = uploadImg)
upload_image_button.pack(side = 'left')

predict_button = tk.Button(buttons_frame, text = 'Predict', pady = 20, command = predict)
predict_button.pack(side = 'right')

# ROW 4
# Set introductions
introduction = tk.Label(window, wraplength = text_wrap_length, text = 'Please upload an image to classify.')
introduction.pack()

window.mainloop()
