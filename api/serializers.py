from rest_framework import serializers
from .models import Todos

class TodosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todos
        fields = '__all__' #lấy tất cả các trường trong csld


#công việc chính của serializer là chuyển đổi dữ liệu từ model django
#sang định dạng json để gửi cho client thông qua api
# database -> api( model django -> json ) -> client
# client -> api (json -> model django ) -> database
#serializer cũng có thể kiểm tra dữ liệu trước khi lưu vào database
#nếu dữ liệu không hợp lệ thì sẽ trả về lỗi cho client