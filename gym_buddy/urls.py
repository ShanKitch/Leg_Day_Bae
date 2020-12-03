from django.urls import path
from . import views
from .models import Profile


urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('create', views.create),
    path('create_profile', views.create_profile),
    path('home', views.home),
    path('view/<int:id>', views.view_user),
    path ('logout', views.logout),
    path('inbox', views.inbox),
    path('mark_as_read/<int:message_id>', views.mark_as_read),
    path('mark_as_unread/<int:message_id>', views.mark_as_unread),
    path('send_message', views.send_message),
    path('reply_message', views.reply_message),
    path('delete_message/<int:message_id>', views.delete_message),
    path('update/<int:id>', views.update),
    path('update_profile', views.update_profile),
    path('forum', views.forum),
    path ('forum_post', views.forum_post),
    path('post_comment/<int:id>',views.post_comment),
    path('delete_comment/<int:id>', views.delete_comment),
    path('delete_post/<int:id>', views.delete_post),
    path('reply_comment/<int:id>', views.reply_comment),
    path('delete_reply/<int:id>', views.delete_reply)
  


   
]