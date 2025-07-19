from django.urls import path
from . import views

urlpatterns = [
    path("", views.BlogPostListCreate.as_view(), name="blog-view-create"),
    path("<int:pk>/", views.BlogPostCRUD.as_view(), name="update"),
    path("", views.BlogPostList.as_view(), name="search")
]