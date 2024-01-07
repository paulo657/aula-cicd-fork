from django.urls import include, path
from .views import SongCreate, SongList, SongDetail, SongUpdate, SongDelete


urlpatterns = [
    path('create/', SongCreate.as_view(), name='create-song'),
    path('list/', SongList.as_view()),
    path('<int:pk>/', SongDetail.as_view(), name='retrieve-song'),
    path('update/<int:pk>/', SongUpdate.as_view(), name='update-song'),
    # path('delete/<int:pk>/', SongDelete.as_view(), name='delete-song')
]