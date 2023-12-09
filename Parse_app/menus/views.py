import logging
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .forms import AccountForm, UserLoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import *
import random
# Create your views here.



def homepage(request):
    template = loader.get_template('Homepage.html')
    return HttpResponse(template.render())
    
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


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'courses.html')  # Redirect to a success page
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})




def createAccount(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('successful/')  # Redirect to a success page
        else:
            # The form is not valid. Print errors to console or pass them back to the template
            print(form.errors)  # This line is for debugging purposes
            return render(request, 'Account_Creation.html', {'form': form})
    else:
        form = AccountForm()
        return render(request, 'Account_Creation.html', {'form': form})

def question_list(request):
    questions = Question.objects.all()
    return render(request, 'question_list.html', {'questions': questions})

