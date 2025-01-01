from django.shortcuts import render

# Create your views here.

def login_view(request, *args, **kwargs):
    return render(request=request, template_name="auth_app/login.html", context=
                  {})
