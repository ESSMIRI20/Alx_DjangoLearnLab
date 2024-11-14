from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login  # Import login function

# View for user registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Save the new user
            user = form.save()
            
            # Automatically log in the user after registration
            login(request, user)
            
            # Redirect to home or some other page after login
            return redirect('home')  # Replace 'home' with your desired redirect target
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
