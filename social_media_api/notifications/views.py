from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Notification
from django.contrib.auth.decorators import login_required

@login_required
def get_notifications(request):
    notifications = Notification.objects.filter(recipient=request.user, is_read=False)
    notifications_list = [
        {
            'actor': n.actor.username,
            'verb': n.verb,
            'timestamp': n.timestamp,
            'target': str(n.target),
        } for n in notifications
    ]
    return JsonResponse({'notifications': notifications_list})
