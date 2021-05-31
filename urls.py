from django.urls import path
from .views import home,BookList,BookDetail,OrderListCreateAPIView
# from .router import router

urlpatterns = [
    path('/',home),
    path('/BookList/',BookList.as_view()),
    # path('/BookDetail/',BookDetail.as_view()),
    path('Test_app/Books/<int:pk>',BookDetail.as_view()),
    # path('',router()),
    path('/OrderListCreateAPIView',OrderListCreateAPIView),

]