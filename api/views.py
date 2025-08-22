# đay là nơi sẻ xử lý logic và các điểm cuối của api
from rest_framework.decorators import api_view #decorators dùng để biến 1 hàm bình thường thành 1 api endpoint
from .models import Todos
from .serializers import TodosSerializer  # import serializer để chuyển đổi dữ liệu từ model sang định dạng JSON
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

@api_view(['GET']) # đánh dấu cho django rest framework biết đây là 1 api endpoint và phương thức là GET
def get_todos(request):
    todos = Todos.objects.all()  # Lấy tất cả dữ liệu từ cơ sở dữ liệu
    serializer = TodosSerializer(todos, many=True) # Chuyển đổi dữ liệu sang định dạng JSON, many=true để báo cho 
    # serializer biết rằng đây là 1 list chứ k phải chỉ 1 object
    return Response(serializer.data, status=status.HTTP_200_OK) 


# POST /todos/create/
@swagger_auto_schema(
    method='post',
    request_body=TodosSerializer,# <-- báo cho Swagger biết schema body
    responses={201: TodosSerializer, 400: 'Bad Request'},
    tags=['todos']
)

@api_view(['POST'])
def create_todo(request):
    serializer = TodosSerializer(data=request.data)  # Lấy dữ liệu từ request và chuyển đổi sang định dạng JSON
    if serializer.is_valid():  # Kiểm tra dữ liệu có hợp lệ không
        serializer.save()  # Lưu dữ liệu vào cơ sở dữ liệu
        return Response(serializer.data, status=status.HTTP_201_CREATED)  # Trả về dữ liệu đã lưu với mã trạng thái 201
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Trả về lỗi nếu dữ liệu không hợp lệ



# PUT /todos/update/{id}/
@swagger_auto_schema(
    method='put',
    request_body=TodosSerializer,
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description='Todo ID',
                          type=openapi.TYPE_INTEGER, required=True),
    ],
    responses={200: TodosSerializer, 404: 'Not found'},
    tags=['todos']
)

@api_view(['PUT'])
def update_todo(request, id):
    try:
        todo = Todos.objects.get(id=id)  # Lấy todo theo id
    except Todos.DoesNotExist:
        return Response({'error': 'Todo not found'}, status=status.HTTP_404_NOT_FOUND)  # Trả về lỗi nếu không tìm thấy

    serializer = TodosSerializer(todo, data=request.data)  # Chuyển đổi dữ liệu từ request sang định dạng JSON
    if serializer.is_valid():  # Kiểm tra tính hợp lệ của dữ liệu
        serializer.save()  # Lưu dữ liệu đã cập nhật
        return Response(serializer.data, status=status.HTTP_200_OK)  # Trả về dữ liệu đã cập nhật
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Trả về lỗi nếu dữ liệu không hợp lệ

@api_view(['DELETE'])
def delete_todo(request,id):
    try:
        todo = Todos.objects.get(id=id)  # Lấy todo theo id
    except Todos.DoesNotExist:
        return Response({'error': 'Todo not found'}, status=status.HTTP_404_NOT_FOUND)  # Trả về lỗi nếu không tìm thấy
    todo.delete()  # Xóa todo
    return Response(status=status.HTTP_204_NO_CONTENT)