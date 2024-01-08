from django.shortcuts import render

def homepage(request):
    return render(request, template_name='home/homepage.html', context={"is_logged_in": False})
