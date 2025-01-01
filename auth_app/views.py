from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request=request, template_name="base/index.html", context=
                  {})
