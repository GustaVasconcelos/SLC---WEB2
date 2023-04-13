from django.contrib import admin
from .models import Itens, Lista
models = [Itens, Lista]

for model in models:
    admin.site.register(model)