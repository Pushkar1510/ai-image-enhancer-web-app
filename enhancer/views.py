from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from users.forms import InputImageForm
from django.contrib import messages
from PIL import Image, ImageEnhance
import os
import cv2
from cv2 import dnn_superres

def home(request):
    if request.method == "POST":
        im_form = InputImageForm(request.POST,request.FILES, instance=request.user.profile)
        if im_form.is_valid():
            current_user = request.user
            if current_user.profile.premium == True or current_user.profile.trials != 0:
                current_user.profile.trials = current_user.profile.trials - 1
                im_form.save()
                return redirect('enhancer-ai_app')
            else:
                messages.warning(request, f'Your free membership is expired. Please purchase to continue using AI Image Enhancer')
                return redirect('enhancer-home')
    im_form = InputImageForm()
    context = {
        'title':'Home',
        'im_form':im_form,
    }
    return render(request, 'enhancer/home.html', context)

def ai_app(request):
    if request.method == 'POST' and 'to_black' in request.POST:
        img_path = os.getcwd()+request.user.profile.image.url
        img_path = img_path.replace('\\', '/')
        img = Image.open(img_path)
        conv_to_black(img, request)
        print(request.user.profile.image.url)
        request.user.profile.save()
        return redirect('enhancer-result')
    elif request.method == 'POST' and 'to_color' in request.POST:
        os.system('python main.py')
        save_path = os.getcwd()+'/media/converted/conv.jpg'
        save_path = save_path.replace('\\', '/')
        request.user.profile.image = save_path
        request.user.profile.save()
        print('Inside to_color if loop')
        print(request.user.profile.image.url)
        return redirect('enhancer-result')
    elif request.method == 'POST' and 'to_upscale' in request.POST:
        img_path = os.getcwd()+request.user.profile.image.url
        img_path = img_path.replace('\\', '/')
        img = Image.open(img_path)
        my_scale(img, request)
        request.user.profile.save()
        return redirect('enhancer-result')
    return render(request, 'enhancer/ai_app.html', {'title':'Workspace'})

def result(request):
    if request.method == 'POST':
        save_path = os.getcwd()+'/media/converted/conv.jpg'
        save_path = save_path.replace('\\', '/')
        filename = 'conv.jpg'
        im = Image.open(save_path)
        response = HttpResponse(mimetype='image/jpg')
        response['Content-Disposition'] = 'attachment; filename=%s.png' % filename
        im.save(response, 'jpg')
    return render(request, 'enhancer/result.html', {'title':'Result'})


def aboutus(request):
    return render(request, 'enhancer/aboutus.html', {'title':'About Us'})

def first(request):
    return render(request, 'enhancer/first.html', {'title':'Welcome'})

def conv_to_black(img, request):
    img_data = img.getdata()

    lst=[]
    for i in img_data:
        lst.append(i[0]*0.2125+i[1]*0.7174+i[2]*0.0721)

    new_img = Image.new("L", img.size)
    new_img.putdata(lst)

    new_img = new_img.convert('RGB')
    save_path = os.getcwd()+'/media/converted/conv.jpg'
    save_path = save_path.replace('\\', '/')
    thefile = new_img.save(save_path)
    request.user.profile.image = save_path

def my_scale(img, request):
    sr = dnn_superres.DnnSuperResImpl_create()
    temp_path = os.getcwd()+ request.user.profile.image.url
    temp_path = temp_path.replace('\\', '/')
   
    


    image = cv2.imread(temp_path)
    print(temp_path)


    path = "model/EDSR_x3.pb"
    sr.readModel(path)

    sr.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
    sr.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)


    sr.setModel("edsr", 8)

    
    result = sr.upsample(image)
    save_path = os.getcwd()+'/media/converted/conv.jpg'
    save_path = save_path.replace('\\', '/')
    
    cv2.imwrite("media/converted/conv.jpg", result)
    request.user.profile.image = save_path