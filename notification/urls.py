from django.urls import path
from notification.views import WebNotificationSaveUserRegisterIdView, NotificationView

urlpatterns = [

    path("user", WebNotificationSaveUserRegisterIdView.as_view(), name="save-user"),
    path("", NotificationView.as_view(), name="notification")

]
