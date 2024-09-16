from django.shortcuts import get_object_or_404, render
from .models import Blogs

# Create your views here.

def blogs(request, *args, **kwargs):
    blogs = Blogs.objects.all()

    return render(request, "blog/blogs.html", {"blogs": blogs})

def blog(request, blog_id):
    blog = get_object_or_404(Blogs, id=blog_id)
    
    return render(request, "blog/blog.html", {"blog": blog})