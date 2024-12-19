from django.shortcuts import render, redirect
from account.models import Profile
from django.contrib.auth.models import User
from .models import finalExam, Category
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from exams.models import ExamSubmission
from django.contrib import messages

# Create your views here.
@login_required(login_url='login')
def all_exam_view(request):
    user_object = User.objects.get(username = request.user)
    user_profile = Profile.objects.get(user = user_object)

    exams = finalExam.objects.order_by('-created_at')
    categories = Category.objects.all()

    context = {"user_profile":user_profile, "exams":exams, "categories":categories}
    return render(request, 'all-quiz.html', context)


@login_required(login_url='login')
def search_view(request, category):
    user_object = User.objects.get(username = request.user)
    user_profile = Profile.objects.get(user = user_object)

    if request.GET.get('q') != None:
        q = request.GET.get('q')
        query = Q(title__icontains=q) | Q(description__icontains=q)
        exams = finalExam.objects.filter(query).distinct().order_by('-created_at')
    #search by category
    elif category != " ":
        exams = finalExam.objects.filter(category__name = category)
    #search by seachbar

    else:
        exams = finalExam.objects.order_by('-created_at')

    categories = Category.objects.all()

    context = {"user_profile":user_profile, "exams":exams, "categories":categories}
    return render(request, 'all-quiz.html', context)

@login_required(login_url='login')
def exam_view(request, exam_id):
    user_object = User.objects.get(username = request.user)
    user_profile = Profile.objects.get(user = user_object)

    exam = finalExam.objects.filter(id=exam_id).first()
    total_question = exam.question_set.all().count() 

    if request.method == "POST":

        #get the score
        score = int(request.POST.get('score',0)) 

        #Check if the user has already submitted the exam
        if ExamSubmission.objects.filter(user=request.user, exam=exam).exists():
            messages.success(request, f"This time you got {score} out of {total_question}")
            return redirect('exam', exam_id)
        
        #save the new exam submission
        submission = ExamSubmission(user=request.user,exam=exam,score=score)
        submission.save()

        #show the result in msg
        messages.success(request, f"Exam Submitted Successfully. You got {score} out of {total_question}")
        return redirect('exam', exam_id)
        
    # context = {"user_profile":user_profile, "exam":exam}
    if exam != None:
        context = {"user_profile":user_profile, "exam":exam}
    else:
        return redirect('all_exam')
    return render(request, 'quiz.html', context)