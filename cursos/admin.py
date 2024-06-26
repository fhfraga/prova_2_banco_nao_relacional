from django.contrib import admin

from .models import Curso


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'instrutor', 'data_inicio')
    search_fields = ('titulo', 'instrutor')