from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from .forms import ServiceRequestForm

# Create your views here.


def signup(request):

    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['pass1']
        conform_password = request.POST['pass2']
        if password != conform_password:
            messages.warning(request,"Password is not matching")
            return render(request,'signup.html')

        try:
            if User.objects.get(username=email):
                messages.info(request,"User already exists")
                return render(request,"signup.html")
        except Exception as identifier:
            pass

        user = User.objects.create_user(email,email,password)
        user.save()
        # return HttpResponse("User created successfully")
        messages.info(request,"User created successfully!")
        return render(request,"login.html")


    return render(request,'signup.html')

def handlelogin(request):
    if request.method == "POST":
        username = request.POST['email']
        userpassword = request.POST['password']
        myuser = authenticate(username=username,password=userpassword)

        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Successfully")
            return redirect('track_request')

        else:
            messages.warning(request,'Invalid creditials...Try Again!!')
            return render(request,'login.html')

    return render(request,'login.html')


def handlelogout(request):
    logout(request)
    messages.info(request,"log out successfully")
    return redirect('/')


# @login_required
def track_request(request):
    user = request.user
    requests = ServiceRequest.objects.filter(customer=user).order_by('-submission_timestamp')
    return render(request, 'index.html', {'requests': requests})

def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            new_request = form.save(commit=False)
            new_request.customer = request.user
            new_request.save()
            messages.success(request, 'Service request submitted successfully.')
            return redirect('track_request')
        else:
            messages.error(request, 'Failed to submit service request. Please check the form.')
    else:
        form = ServiceRequestForm()

    return render(request, 'submit.html', {'form': form})
#

# def track_request(request):
#     user = request.user
#     requests = ServiceRequest.objects.filter(customer=user)
#     return render(request, 'index.html', {'requests': requests})