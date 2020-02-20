from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('todo.urls')),
]
# ''の中に指定しないと、最初にrunserverが読み込まれたときに表示する最初のファイルとなる。