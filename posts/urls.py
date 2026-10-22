from django.urls import path

from posts.views import about_website, create_post, home_page, list_posts, read_post, delete_post, update_post


urlpatterns = [
    path('', home_page, name='home-page'), 
    path('posts/create/', create_post, name='create-post'),
    path('posts/list/',list_posts, name = 'list-posts' ),
    path('posts/<int:post_id>/',read_post , name='read-post'),
    path('post/<int:post_id>/delete/', delete_post, name = 'delete-post'),
    path('post/<int:post_id>/update/', update_post, name= 'update-post'),
    path('post/about', about_website, name='about-website')
]

