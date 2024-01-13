from django.urls import path
from .views import (
    group_detail,
    add_user_to_group,
    create_group,
    user_dashboard,
    delete_group,
)

urlpatterns = [
    path("groups/<str:group_id>/", group_detail, name="group-detail"),
    path("add-user-to-group/<str:id>/", add_user_to_group, name="add-user-to-group"),
    path("create-group/", create_group, name="create-group"),
    path("dashboard/", user_dashboard, name="dashboard"),
    path("delete-group/<str:id>/", delete_group, name="delete-group"),
]
