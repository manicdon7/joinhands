from django.shortcuts import render,redirect
from .models import Res,Sign
from django.http import HttpResponse



def index(request):
    if request.method == 'POST':
        name = request.POST['Name']
        Desc = request.POST['Description']
        Image = request.FILES.get('file')
        Stat = 'Not Claimed'
        
        obj = Res()
        obj.name = name
        obj.desc = Desc
        obj.image = Image
        obj.status = Stat
        obj.save()
    return render(request,"index.html")
def view(request):
    obj = Res.objects.all()
    return render(request, 'view.html', {'obj':obj})
def NGO(request):
    obj = Res.objects.all()
    return render(request, 'NGO.html', {'obj':obj})
def change_status(request, res_id):
    obj = Res.objects.get(pk=res_id)
    if obj.status == 'Not Claimed':
        obj.status = 'Claimed'
    else:
        obj.status = 'Not Claimed'
    obj.save()
    return render(request, 'NGO.html', {'obj':obj})
def SignUp(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        designation = request.POST['designation']
        signup_instance = Sign()
        signup_instance.user=username
        signup_instance.password=password
        signup_instance.designation = designation
        signup_instance.save()
        redirect('Login')
    return render(request, 'SignUp.html')
def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        obj = Sign.objects.all()
        try:
            user_obj = Sign.objects.get(user=username, password=password)
            if user_obj.designation == 'NGO':
                return redirect('NGO')  # Make sure you have a valid URL name for the NGO view
            elif user_obj.designation == 'Restaurant':
                return redirect('index')
        except Sign.DoesNotExist:
            return HttpResponse("Invalid Login Credentials.")
    return render(request,'Login.html')