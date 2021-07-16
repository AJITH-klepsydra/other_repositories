import datetime
from django.core.cache import cache
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from todoapp.models import User
class ActiveUserMiddleware:
    def __init__(self, get_response):
            self.get_response = get_response

    def __call__(self, request):
        current_user = request.user
        now = datetime.datetime.now()
        try:
            u = User.objects.all().get(username=str(request.user))
            u.last_scene=now
            u.save()
        except:
            pass
        #print(request.user.last_scene)
        #print(request.user.username)
        #print(datetime.datetime.now())
        return self.get_response(request)


    def process_exception(self, request, exception):
        return HttpResponse("in exception")
