from django.db import models

class Todos(models.Model):
    title = models.CharField(max_length=255)  # tiêu đề hay tên công việc
    description = models.TextField(blank=True, null=True) # mô tả công việc
    is_completed = models.IntegerField(blank=True, null=True) #trạng thái công việc đã hoàng thành hay chưa
    created_at = models.DateTimeField(blank=True, null=True) #ngày tạo công việc
    updated_at = models.DateTimeField(blank=True, null=True) #ngày cập nhật lại công việc

    class Meta:
        managed = False #db này không quản lý bở django
        db_table = 'todos'  
