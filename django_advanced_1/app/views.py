from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from app.models import Student

def index(request):
    student = Student.objects.all()
    return render(request, template_name='index.html', context={
        'student': student
    })

def create(request):
    if request.method == "POST":
        student = Student()
        student.name = request.POST.get('name')
        student.age = request.POST.get('age')
        student.sex = request.POST.get('sex')
        student.save()
    return redirect('/app')

def edit(request, id):
    try:
        student = Student.objects.get(id=id)

        if request.method == "POST":
            student.name = request.POST.get("name")
            student.age = request.POST.get("age")
            student.sex = request.POST.get("sex")
            student.save()
            return redirect('/app')
        else:
            return render(request, template_name="edit.html", context={"student": student})
    except Student.DoesNotExist:
        return HttpResponseNotFound("<h2>Student not found</h2>")

def delete(request, id):
    try:
        person = Student.objects.get(id=id)
        person.delete()
        return redirect('/app')
    except Student.DoesNotExist:
        return HttpResponseNotFound("<h2>Student not found</h2>")