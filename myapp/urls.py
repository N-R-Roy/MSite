from django.urls import path
from . import views
from django.views.generic import RedirectView


app_name = "myapp"

urlpatterns = [
    # path("", views.index, name="index"),

    path("", views.Index.as_view(), name="index"),
    path("address/<str:address>/", views.AddressCView.as_view(), name="add_c_view"),


    path("rdx/", RedirectView.as_view(url="https://www.google.com/"), name="rdx"),
    path('preload/<str:id>/and/<str:id2>/', views.PreLoadView.as_view(), name="preload"),
    path("show_page/<str:id>/value/<str:id2>/", views.ShowPageView.as_view(), name="show_page_view"),
    path('mv_page/', views.MView.as_view(), name="mv_page"),


    path('detail/<int:pk>/', views.PersonDetailView.as_view(), name="person_detail"),

    path("add_person/", views.AddPersonForm.as_view(), name="add_person"),
    path("create_person/", views.CreatePersonView.as_view(), name="create_person"),
    path("update_person/<int:pk>/", views.UpdatePersonView.as_view(), name="update_person"),
    path("delete_person/<int:pk>/", views.DeletePersonView.as_view(), name="delete_person"),


    path("song_list/", views.SongListView.as_view(), name="song_list"),
    path("create_song/", views.CreateSongView.as_view(), name="create_song"),

    path('create_emp/', views.employee_vw, name='create_emp'),
    path('emp_list/', views.EmployeeList.as_view(), name="emp_list"),

    path("my_file/", views.MyView.as_view(), name="my_file"),
    path('file_obj_list/', views.FileListView.as_view(), name="file_obj_list"),
]

