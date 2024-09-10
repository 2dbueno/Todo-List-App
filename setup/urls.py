from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from todos.views import (
    TodoListView,
    TodoCreateView,
    TodoUpdateView,
    TodoDeleteView,
    TodoCompleteView,
    RegisterUserView,
    LoginView,
    HomePageView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomePageView.as_view(), name="home"),
    path("todos/", TodoListView.as_view(), name="todo_list"),
    path("create/", TodoCreateView.as_view(), name="todo_create"),
    path("update/<int:pk>", TodoUpdateView.as_view(), name="todo_update"),
    path("delete/<int:pk>", TodoDeleteView.as_view(), name="todo_delete"),
    path("complete/<int:pk>", TodoCompleteView.as_view(), name="todo_complete"),
    path("register_user/", RegisterUserView.as_view(), name="register_user"),
    path("login_user/", LoginView.as_view(), name="login_user"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
