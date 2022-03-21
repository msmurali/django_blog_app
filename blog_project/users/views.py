from django.shortcuts import redirect, render
from .forms import UserRegistrationForm

def register(req):
    if(req.method == 'POST'):
        form = UserRegistrationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('blog-home')
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(req, 'users/register.html', context)
