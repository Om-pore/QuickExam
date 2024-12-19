from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from account.models import Profile
from exams.models import ExamSubmission, finalExam, Question
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.


def home(request):

    if request.user.is_authenticated:
        user_object = User.objects.get(username = request.user)
        user_profile = Profile.objects.get(user = user_object)
        context = {"user_profile":user_profile}
    else:
        context = {}

    return render(request, 'welcome.html', context)


def is_superuser(user):
    return user.is_superuser


@login_required(login_url='login')
@user_passes_test(is_superuser)
def dashboard_view(request):
    user_object = User.objects.get(username = request.user)
    user_profile = Profile.objects.get(user = user_object)
    
    # total numbers
    total_users = User.objects.all().count()
    total_exams = finalExam.objects.all().count()
    total_examSubmit = ExamSubmission.objects.all().count()
    total_questions = Question.objects.all().count()
    
    context = {"user_profile":user_profile, 
               "total_users":total_users, 
               "total_exams":total_exams, 
               "total_examSubmit":total_examSubmit, 
               "total_questions":total_questions}
    return render(request, 'dashboard.html', context)

def about_view(request):
    if request.user.is_authenticated:
        user_object = User.objects.get(username = request.user)
        user_profile = Profile.objects.get(user = user_object)
        context = {"user_profile":user_profile}
    else:
        context = {}
    
    return render(request, "about.html", context)


def blogs_view(request):
    if request.user.is_authenticated:
        user_object = User.objects.get(username = request.user)
        user_profile = Profile.objects.get(user = user_object)
        context = {"user_profile":user_profile}
    else:
        context = {}
    
    return render(request, "blogs.html", context)

@login_required(login_url='login')
def blog_view(request, blog_id):
    user_object = User.objects.get(username = request.user)
    user_profile = Profile.objects.get(user = user_object)
            
    
    context = {"user_profile":user_profile}
    return render(request, "blog.html", context)

@login_required(login_url='login')
def feedback_view(request):
    user_object = User.objects.get(username = request.user)
    user_profile = Profile.objects.get(user = user_object)
            
    
    context = {"user_profile":user_profile}
    return render(request, "feedback.html", context)
    
@login_required(login_url='login')
def contact_view(request):
    user_object = User.objects.get(username = request.user)
    user_profile = Profile.objects.get(user = user_object)
    context = {"user_profile":user_profile}
    
    return render(request, "contactUs.html", context)


def terms_conditions_view(request):
    if request.user.is_authenticated:
        user_object = User.objects.get(username = request.user)
        user_profile = Profile.objects.get(user = user_object)
        context = {"user_profile":user_profile}
    else:
        context = {}
    
    return render(request, "terms_condition.html", context)


@login_required(login_url='login')
def download_view(request):
    user_object = User.objects.get(username = request.user)
    user_profile = Profile.objects.get(user = user_object)
    context = {"user_profile":user_profile}
    
    return render(request, "download.html", context)