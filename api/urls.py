from django.urls import path
from .views import get_todos, create_todo, update_todo, delete_todo

urlpatterns = [
    path('todos/', get_todos, name='get_todos'),  # Endpoint get tất cả trong csdl lên
    # gắn tên cho endpoint để sau có thể xử dụng lại vd revert('get_todos')
    path('todos/create/', create_todo, name='create_todo'),  # Endpoint tạo mới todo
    path('todos/update/<int:id>/', update_todo, name='update_todo'),  # Endpoint cập nhật todo theo id
    path('todos/delete/<int:id>/', delete_todo, name='delete_todo'),  # Endpoint xóa todo theo id
]