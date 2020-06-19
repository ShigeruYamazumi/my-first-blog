from django.urls import path 
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), # リスト表示
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'), # 新規
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'), # 編集
    path('drafts/', views.post_draft_list, name='post_draft_list'), # 草稿ページ
    path('post/<pk>/publish/', views.post_publish, name='post_publish'), # 公開
    path('post/<pk>/remove/', views.post_remove, name='post_remove'), # 削除
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]
