from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    View,
)
from crispy_forms.helper import FormHelper
from .forms import TodoForm, CustomUserCreationForm, CustomAuthenticationForm
from .models import Todo, CustomUser


class HomePageView(TemplateView):
    template_name = "home/home.html"


class TodoListView(LoginRequiredMixin, ListView):
    model = Todo
    template_name = "todo/todo_list.html"

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy("todo_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["title", "deadline", "priority"]
    success_url = reverse_lazy("todo_list")

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")

class TodoCompleteView(View):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.mark_has_complete()
        return redirect("todo_list")

class RegisterUserView(View):
    template_name = "registration/register_user.html"
    form_class = CustomUserCreationForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.instance.password = make_password(form.cleaned_data["password1"])
            user = form.save()

            return redirect(reverse("todo_list"))

        return render(request, self.template_name, {"form": form})

class LoginView(View):
    template_name = "registration/login_user.html"

    def get(self, request, *args, **kwargs):
        form = CustomAuthenticationForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_user = authenticate(
                request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )

            if auth_user is not None:
                login(request, auth_user)
                return redirect("todo_list")

        return render(request, self.template_name, {"form": form})