# middleware.py
from django.http import HttpResponseForbidden
from django.urls import reverse
from django.shortcuts import redirect

class AdminAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith(reverse('admin:index')):
            if not request.user.is_superuser:
                if request.user.is_authenticated:
                    return HttpResponseForbidden("You are not authorized to access this page.")
                else:
                    return redirect('%s?next=%s' % (reverse('login'), request.path))
        return self.get_response(request)



