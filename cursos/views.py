from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import CursoForm
from .models import Curso


def home(request):
    return render(request, 'cursos/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'cursos/register.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('/login')

def curso_list(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/curso_list.html', {'cursos': cursos})

class CursoCreate(LoginRequiredMixin, CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'cursos/curso_form.html'
    success_url = reverse_lazy('curso_list')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class CursoUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'cursos/curso_form.html'
    success_url = reverse_lazy('curso_list')

    def test_func(self):
        curso = self.get_object()
        return self.request.user == curso.autor or self.request.user.is_superuser

class CursoDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Curso
    template_name = 'cursos/curso_confirm_delete.html'
    success_url = reverse_lazy('curso_list')

    def test_func(self):
        curso = self.get_object()
        return self.request.user == curso.autor or self.request.user.is_superuser

def chat_view(request):
    return render(request, 'cursos/chat.html')