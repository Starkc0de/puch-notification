from django.urls import reverse
from django.views import generic
from django.http import HttpResponseRedirect, JsonResponse
from push_notifications.models import WebPushDevice


class NotificationView(generic.TemplateView):
    template_name = "notifications.html"

    def post(self, request):
        web_device=WebPushDevice.objects.get(auth  = "bACc8ksBniO7Fy/UnCpidw==")
        web_device.send_message("Bob wants to play poker")
        return HttpResponseRedirect(reverse('push-notification:notification'))

class WebNotificationSaveUserRegisterIdView(generic.View):
    
    def post(self,request):
        browser = request.POST.get("browser")
        p256dh = request.POST.get("p256dh")
        auth = request.POST.get("auth")
        registration_id = request.POST.get("registration_id")
        if WebPushDevice.objects.filter(registration_id = registration_id).first():
            pass
        else:
             WebPushDevice.objects.create(p256dh=p256dh,auth=auth,browser=browser,registration_id=registration_id)

        return JsonResponse({'status':1})

     