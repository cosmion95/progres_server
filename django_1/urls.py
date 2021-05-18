"""django_1 URL Configuration

The `urlpatterns` list routes URLs to viewsa. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function viewsa
    1. Add an import:  from my_app import viewsa
    2. Add a URL to urlpatterns:  path('', viewsa.home, name='home')
Class-based viewsa
    1. Add an import:  from other_app.viewsa import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest_api/', include('progres_1.urls')),
]
