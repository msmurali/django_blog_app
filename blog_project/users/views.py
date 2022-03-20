from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm

def register(req):
    if(req.method == 'POST'):
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('blog-home')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(req, 'users/register.html', context)
