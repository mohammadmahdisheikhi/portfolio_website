from django.shortcuts import get_object_or_404, render
from works.models import Works

# Create your views here.

def works(request, *args, **kwargs):
    works = Works.objects.all()

    return render(request, "works/works.html", {"works": works})

def work(request, work_id):
    work = get_object_or_404(Works, id=work_id)
    
    return render(request, "works/work.html", {"work": work})