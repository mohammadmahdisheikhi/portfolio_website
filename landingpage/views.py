from django.shortcuts import get_object_or_404, render
from blog.models import Blogs
from works.models import Works
from .models import Owner, Skill

def index(request, work_id=None, blog_id=None, *args, **kwargs):
    works = Works.objects.all()
    owner = Owner.objects.first()  # Retrieve the first Owner instance
    skills = Skill.objects.all()

    # Handle blog retrieval
    if blog_id:
        blog = get_object_or_404(Blogs, id=blog_id)
    else:
        blog = Blogs.objects.first()  # You can modify this to select a default blog or set to None
    
    # Fetch all blogs
    blogs = Blogs.objects.all()
    testimonials = owner.testimonials.all() if owner else None

    # Handle work retrieval
    if work_id:
        work = get_object_or_404(Works, id=work_id)
    else:
        work = works.first() if works.exists() else None  # Modify this as per your preference

    return render(request, "landingpage/index.html", {
        "works": works,
        "work": work,
        "owner": owner,
        "blog": blog,
        "blogs": blogs,
        "testimonials": testimonials,
        "skills": skills
    })


