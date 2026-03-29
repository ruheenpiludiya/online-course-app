from django.shortcuts import render
from .models import Course, Submission

def submit(request):
    score = 80  # dummy score
    Submission.objects.create(course_id=1, score=score)
    return render(request, 'result.html', {'score': score})

def show_exam_result(request):
    submission = Submission.objects.last()
    return render(request, 'result.html', {'score': submission.score})