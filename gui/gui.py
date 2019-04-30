# -*- coding: utf-8 -*-
import os
import tkinter as tk
import numpy as np
import json
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from keras.models import load_model

img_size = 224

# https://drive.google.com/file/d/1RasU0buZ00D6BpYia8IFlMaf0jWnwRSJ/view?usp=sharing
model_file = 'CSCE636_final_model.h5'
uploaded_img = None
breeds = {}

# Load dictionary of dog breed introductions
with open('breed_classes.json') as f:
    classes = json.load(f)

for key, val in classes.items():
    breeds[val] = key

def rescaleImg(img):
    # Scale and center image to fit canvas (longer side has length img_size(300))
    global img_size
    w, h = img.size
    scaled_w = img_size
    if w > h:
        scale = scaled_w / w
        x_shift = 0
        y_shift = int(scaled_w / 2 - h * scale / 2)
    else:
        scale = scaled_w / h
        x_shift = int(scaled_w / 2 - w * scale / 2)
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
    image_canvas.delete(img_display_instruction)

def updateSampleImg(breed):
    sample_dir = os.path.join('./', breed)
    try:
        img = Image.open(os.path.join(sample_dir, 'sample.jpg'))
    except:
        return

    imgfile, x_shift, y_shift = rescaleImg(img)
    imgfile = ImageTk.PhotoImage(imgfile)
    intro_canvas.image = imgfile
    intro_canvas.create_image(x_shift, y_shift, anchor = 'nw', image = imgfile)

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

    intro.configure(text = "This is a %s ! A dog of this type looks like:" %(breeds[breed_idx]), pady = 20)
    updateSampleImg(breeds[breed_idx])

# Initiate the window
window = tk.Tk()
window.title('Dog Breed Classification')
window.geometry('768x700')

# ROW 1
# Set title in the window content
main_title = tk.Label(window, text = 'Dog Breeds Recognizer', font = ('', 30), pady = 20)
main_title.pack()

# ROW 2
# Set image display areas
images_frame = tk.Frame(window)
images_frame.pack()

image_canvas = tk.Canvas(images_frame, width = img_size, height = img_size, bd = 0)
img_display_instruction = image_canvas.create_text(int(img_size / 2), int(img_size / 2), text = 'Your image will be displayed here.')
image_canvas.pack()

# ROW 3
# Set two functional buttons
buttons_frame = tk.Frame(window)
buttons_frame.pack()

upload_image_button = tk.Button(buttons_frame, text = 'Upload', pady = 20, command = uploadImg)
upload_image_button.pack(side = 'left')

predict_button = tk.Button(buttons_frame, text = 'Predict', pady = 20, command = predict)
predict_button.pack(side = 'right')

# ROW 4
# Set introductions
intro_frame = tk.Frame(window)
intro_frame.pack()

intro = tk.Label(intro_frame, wraplength = 840, text = 'Please upload an image of A DOG to classify.')
intro.pack()

intro_canvas = tk.Canvas(intro_frame, width = img_size, height = img_size, bd = 0)
intro_canvas.pack()

window.mainloop()
