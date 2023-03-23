from django.shortcuts import redirect, render
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib import messages

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            send_mail(
                'AI Image Enhancer : Account Created',
                "Hello,\n\nWe've received your request to create an account for AI Image Enhancer. We welcome you to our site. Please feel free to contact us if you have any questions.\n\nThank You!",
                '',
                [form.cleaned_data.get('email')],
                fail_silently=False,
            )
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form, 'title':'Sign Up'})

@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)

        if u_form.is_valid():
            u_form.save()
            return redirect('users-profile')
        elif request.method == 'POST' and 'run_script' in request.POST:
            if request.user.profile.email_verified == True:
                request.user.profile.premium = True
                request.user.profile.save()
                messages.success(request, f'Your account status is now Premium')
            else:
                messages.warning(request, f'You need to verfiy your email.')
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {'u_form':u_form}
    return render(request, 'users/profile.html', context)

@login_required
def verification(request):
    if request.method == "POST":
        input_code = request.POST.get('security_code')
        if input_code == request.user.profile.security_code:
            request.user.profile.email_verified = True
            request.user.profile.save()
            messages.success(request, f'Your email is verified')
            return redirect('users-profile')
        else:
            messages.warning(request, f'Please enter valid security code')
    
    context = {'title':'Verification'}
    
    return render(request, 'users/verify.html', context)