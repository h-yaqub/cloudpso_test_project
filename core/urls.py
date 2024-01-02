from django.urls import path

from . import views

urlpatterns = [
    path("accounts/register/", views.RegisterView.as_view(), name="register"),
    path("accounts/<int:pk>/edit/", views.UpdateUserView.as_view(), name="update_user"),
    path("", views.HomeView.as_view(), name="home"),
    path("notes", views.NoteListView.as_view(), name="notes_list"),
    path("notes/create/", views.CreateNoteView.as_view(), name="notes_create"),
    path("notes/<int:pk>/edit/", views.EditNoteView.as_view(), name="notes_edit"),
    path("notes/<int:pk>/delete/", views.DeleteNoteView.as_view(), name="notes_delete"),
    path(
        "notes/<int:pk>/details/", views.DetailNoteView.as_view(), name="notes_detail"
    ),
]
