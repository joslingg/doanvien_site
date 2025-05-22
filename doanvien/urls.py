from django.urls import path
from . import views

urlpatterns = [
    path('', views.member_list, name='member-list'),  # Trang chủ
    path("them-doan-vien/", views.add_member, name="add-member"),
    path("chinh-sua/<int:pk>", views.edit_member, name="edit-member"),
    path("xoa/<int:pk>", views.delete_member, name="delete-member"),
    path("thong-ke/", views.member_stats, name="member-stats"),
    path('xuat-excel/', views.export_member_list, name='export-member-list'),
    path('import-members/', views.import_member_from_excel, name='import-members'),
    path('download-template/', views.download_template, name='download_template'),
]
