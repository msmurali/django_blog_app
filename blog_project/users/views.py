from django.shortcuts import redirect, render
from .forms import UserRegistrationForm, UserUpdationForm, ProfileUpdationForm
from django.contrib.auth.decorators import login_required


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


@login_required
def profile(req):
    if(req.method == 'POST'):
        user_update_form = UserUpdationForm(
            req.POST,
            req.FILES,
            instance=req.user)

        profile_update_form = ProfileUpdationForm(
            req.POST,
            req.FILES,
            instance=req.user.profile)

        if (user_update_form.is_valid() and profile_update_form.is_valid()):
            user_update_form.save()
            profile_update_form.save()
        return redirect('profile')

    else:
        user_update_form = UserUpdationForm(
            instance=req.user
        )
        profile_update_form = ProfileUpdationForm(
            instance=req.user.profile
        )

        context = {
            'user_update_form': user_update_form,
            'profile_update_form': profile_update_form,
        }
        return render(req, 'users/profile.html', context)
