"""mi_primer_mvt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hola_mundo.views import (mostrar_mis_tareas, crear_tareas, BuscarTareas, crear_compra, mostrar_compras, BuscarCompras, BuscarPersonas, mostrar_personas, crear_persona, BuscarPersonas)
from SocialTravel.views import (index, PostList,PostDetail, PostCreate, PostUpdate, PostDelete)

urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls),

    path('tareas', mostrar_mis_tareas, name="tareas"),
    path('tareas/create', crear_tareas, name="tareas-create"),
    path('tareas/list', BuscarTareas.as_view(), name="tareas-list"),

    path('compras', mostrar_compras, name="compras"),
    path('compras/create', crear_compra, name="compras-create"),
    path('compras/list', BuscarCompras.as_view(), name="compras-list"),

    path('personas', mostrar_personas, name="personas"),
    path('personas/create', crear_persona, name="personas-create"),
    path('personas/list', BuscarPersonas.as_view(), name="personas-list"),

    path('post/list', PostList.as_view(), name="post-list"),
    path('post/<pk>/detail', PostDetail.as_view(), name="post-detail"),
    path('post/create', PostCreate.as_view(), name="post-create"),
    path('post/<pk>/update', PostUpdate.as_view(), name="post-update"),
    path('post/<pk>/delete', PostDelete.as_view(), name="post-delete"),
]
