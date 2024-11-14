from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView

# View for user registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Custom login view is handled by Django's LoginView, no need to create one unless customization is needed
# The default LoginView works perfectly out of the box for simple authentication
# You can customize it by specifying the template_name if needed
# class LoginView(LoginView):
#     template_name = 'relationship_app/login.html'
