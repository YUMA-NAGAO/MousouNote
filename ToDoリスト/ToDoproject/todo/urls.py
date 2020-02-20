from django.urls import path,re_path
from django.views.generic import RedirectView
from .views import ToDoList, ToDoDetail, ToDoCreate, ToDoDelete, ToDoUpdate

urlpatterns = [
    path('', ToDoList.as_view(), name='list'),
    path('list/', ToDoList.as_view(), name='list'),
    path('detail/<int:pk>', ToDoDetail.as_view(), name='detail'),
    path('create/', ToDoCreate.as_view(), name='create'),
    path('delete/<int:pk>', ToDoDelete.as_view(), name='delete'),
    path('update/<int:pk>', ToDoUpdate.as_view(), name='update'),
]
# ''の中に指定しないと、最初にrunserverが読み込まれたときに表示する最初のファイルとなる。
urlpatterns += [re_path(r'^.*$', RedirectView.as_view(url='/')), ]
