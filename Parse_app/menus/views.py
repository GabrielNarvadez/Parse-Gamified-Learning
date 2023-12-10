import logging
from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .forms import AccountForm, UserLoginForm
from django.contrib import messages
from .models import *
import random
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='signup')

def homepage(request):
    template = loader.get_template('Homepage.html')
    return HttpResponse(template.render())
    

# Create your views here.

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not the same!!")
        else:
            my_user = CustomUser.objects.create_user(uname, email, pass1)  # Use the custom manager
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html')


def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')






def courses(request):
    context = {'categories': Category.objects.all()}

    if request.GET.get('category'):
        return redirect(f"/quizzes/?category={request.GET.get('category')}")

    return render(request, 'Courses.html', context)

def quiz_instance(request):

    context = {'category' : request.GET.get('category')}
    return render(request, 'quiz.html', context)

def account(request):
    acc = loader.get_template('Account.html')
    return HttpResponse(acc.render())

def successfulAccount(request):
    acc = loader.get_template('account_success.html')
    return render(request, 'account_success.html')

def about(request):
    # Logic for the about page
    return render(request, 'about.html')

def blank(request):
    # Logic for the blank page
    return render(request, 'blank.html')

def error(request):
    # Logic for the error page
    return HttpResponse("This is an error page.")

def finished(request):
    # Logic for the finished courses page
    return render(request, 'finished.html')

def help(request):
    # Logic for the help page
    return render(request, 'help.html')
from django.http import JsonResponse, HttpResponse

def get_quiz(request):
    try:
        question_objs = Question.objects.all()

        if request.GET.get('category'):
            question_objs = question_objs.filter(category__category_name__icontains=request.GET.get('category'))

        question_objs = list(question_objs)
        data = []

        random.shuffle(question_objs)

        for question_obj in question_objs:
            data.append({
                "uid": question_obj.uid,
                "category": question_obj.category.category_name,
                "question": question_obj.question,
                "marks": question_obj.marks,
                "answers": question_obj.get_answers()
            })
            
        payload = {'status': True, 'data': data}
        return JsonResponse(payload)

    except Exception as e:
        print(e)
        # Return an HttpResponse even in case of exception
        return HttpResponse("Something went wrong", status=500)

