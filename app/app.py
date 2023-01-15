# AUTOGENERATED! DO NOT EDIT! File to edit: ../dogvcats.ipynb.

# %% auto 0
__all__ = ['learn', 'categories', 'image', 'label', 'examples', 'intf', 'is_cat', 'classify_image']

# %% ../dogvcats.ipynb 2
from fastai.vision.all import *
import gradio as gr

def is_cat(x): return x[0].isupper()

# %% ../dogvcats.ipynb 4
learn = load_learner('model.pkl')

# %% ../dogvcats.ipynb 6
categories = ('Dog', 'Cat')

def classify_image(img):
    pred,idx,probs = learn.predict(img)
    return dict(zip(categories, map(float, probs)))

# %% ../dogvcats.ipynb 8
image = gr.inputs.Image(shape=(192,192))
label = gr.outputs.Label()
examples = ['dog.jpg', 'cat.jpg', 'meowth.jpg']

intf = gr.Interface(fn=classify_image, inputs=image, outputs=label, examples=examples)
intf.launch(inline=False)
