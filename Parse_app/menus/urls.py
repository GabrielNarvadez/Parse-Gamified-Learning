from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name = "Home Page"),
    path('account/', views.homepage, name = 'empty link brah'),
    path('account/successful/', views.successfulAccount, name = 'Account Successful'),
    path('courses/', views.courses, name = 'Courses'),

#Added
    path('about/', views.about, name = 'About Page'),
    path('blank/', views.blank, name = 'Blank Page'),
    path('error/', views.error, name = 'Error Page'),
    path('courses/finished', views.finished, name = 'Course Finished'),
    path('help/', views.help, name= 'Help Page'),
    path('quizzes/', views.quiz_instance, name='Quiz Instance'),


#Second batch
    path('quizzes/questions/', views.finished, name = 'addQuestion'),
    path('quizzes/choices/', views.help, name= 'addChoices'),
    path('quizzes/choices/edit/', views.quiz_instance, name='addEditChoices'),

#Third Batch
    path('api/get-quiz/', views.get_quiz, name='get_quiz'),

#Login
    path('signup/', views.SignupPage, name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),


]
