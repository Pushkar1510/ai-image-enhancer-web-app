#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import glob
import numpy as  np
from PIL import Image
from tensorflow.keras import models
import matplotlib.pyplot as plt
from skimage.io import imsave
from skimage.color import rgb2lab, lab2rgb
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
import cv2


# In[2]:


def loadImagesToArray(dir_path):
    images = []
    try:
        for filename in os.listdir(dir_path):
            images.append(img_to_array(load_img(dir_path+os.sep+filename)))
    except:
        pass
    return np.array(images,dtype=float)/255.0

def RGB2GRAY(img,add_channel_dim=False):
    conv_matrix = np.array([0.212671 ,0.715160,0.072169])
    gray_img = np.matmul(img,conv_matrix)
    if add_channel_dim==True:
        return gray_img.reshape(np.array([*gray_img.shape,1]))
    else:
        return gray_img

def Lab2RGB(gray,ab):
    ab = ab*255.0 -127
    gray = gray*100
    Lab =np.concatenate([x[..., np.newaxis] for x in [gray[...,0], ab[...,0],ab[...,1]]], axis=-1)
    return lab2rgb(Lab)
    

        
def save_result(img_out,save_as="media/converted/"):
    fig, (ax) = plt.subplots(1, 1)
    ax.imshow(img_out)
    ax.set_title('Output')
    ax.set_xticks([])
    ax.set_yticks([])
    path = save_as+'conv.jpg'
    fig.savefig(path,dpi=1000)


# In[3]:


def preprocessing():
    path = 'media/processed/'
    for filename in glob.glob('media/profile_pics/*'): 
        img = Image.open(filename).resize((128,128))
        img.save('{}{}{}'.format(path,'/',os.path.split(filename)[1]))
        color_me = loadImagesToArray(path)
        gray = RGB2GRAY(color_me,True)
        gray2 = RGB2GRAY(color_me)
    return color_me, gray, gray2


# In[4]:


model = models.load_model('model/v1')


# In[14]:


files = glob.glob('media/processed/*')
for f in files:
    os.remove(f)


# In[15]:


files = glob.glob('media/converted/*')
for f in files:
    os.remove(f)


# In[16]:


func_return = preprocessing()


# In[17]:


color_me = np.array(func_return[0])
gray = np.array(func_return[1])
gray2 = np.array(func_return[2])


# In[18]:


output = model.predict(gray)


# In[19]:


for i in range(1):
    pred = Lab2RGB(gray[i],output[i])
    pred = pred.reshape(color_me[i].shape)
   


# In[20]:


save_result(pred)


# In[21]:


files = glob.glob('media/profile_pics/*')
for f in files:
    os.remove(f)


# In[ ]:





# In[ ]:




