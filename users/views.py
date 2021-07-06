from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages


'''def view_profile(request):
    prof_user = request.user
    if request.method == "POST":
        pass
    else:
        if request.user.is_staff:
            return render(request=request, template_name="teacher_profile.html", context={ 'user': prof_user})
        else:
            return render(request=request, template_name="student_profile.html", context={'user': prof_user})'''




def view_register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("users:view_profile")
        else:
            print(form.errors)
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = NewUserForm(request.GET or None)
    return render(request=request, template_name="register.html", context={'register_form':form})
