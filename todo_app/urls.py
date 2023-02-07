from django.urls import path
from . import views

urlpatterns = [
    # 이 부부분을 채울 예정이다.
    path('',views.Todos),    #함수 불러오기(FBV)
    path('create_todo/',views.TodoCreate.as_view()),    #클래스 불러오기(CBV)
    path('update_todo/<int:pk>/',views.TodoUpdate.as_view()),
    path('delete_todo/<int:pk>/', views.DeleteTodo)

]

