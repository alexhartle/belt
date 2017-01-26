from django.shortcuts import HttpResponse, render, redirect
from .models import Schools, Comments, User
# Create your views here.
def index(request):
    if 'id' not in request.session:
        return redirect('/login')
    context = { "schools": Schools.objects.all(),
                "comments": Comments.objects.all(),}
    print request.session['full_name']
    return render(request,'schoolCreator/index.html', context)

def add(request):
    Schools.objects.add(request.POST)
    return redirect('/schools')

def comment(request, school_id):
    school = Schools.objects.get(id=school_id)
    user = User.objects.get(id=request.session['id'])
    print user.id
    Comments.objects.create(comment=request.POST['comment'],
                            name=request.session['full_name'],
                            comment_creator=user,
                            school=school)
    return redirect('/schools')
