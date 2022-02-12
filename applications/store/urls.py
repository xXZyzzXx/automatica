from django.urls import path

from applications.store.views import StoresListView, GetVisitView


urlpatterns = [
    path('stores_list/', StoresListView.as_view()),
    path('get_visit/', GetVisitView.as_view()),
]
