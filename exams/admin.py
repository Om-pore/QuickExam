from django.contrib import admin
from .models import finalExam, Category, Question, Choice, ExamSubmission

# Register your models here.
admin.site.register(Category)
admin.site.register(finalExam)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(ExamSubmission)
