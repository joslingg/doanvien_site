from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

class Member(models.Model):
    name = models.CharField(max_length=180)
    gender = models.CharField(max_length=10, choices=[('Nam','Nam'),('Nữ','Nữ')])
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    status = models.CharField(
        max_length=50,
        choices=[
            ('Còn hoạt động','Còn hoạt động'),
            ('Hưu','Hưu'),
            ('Ngưng hoạt động','Ngưng hoạt động'),
        ],
        null=True,
        blank=True
    )
    note = models.CharField(
        max_length=50,
        choices=[
            ('Chủ tịch BCH CĐCS','Chủ tịch BCH CĐCS'),
            ('Phó chủ tịch BCH CĐCS','Phó chủ tịch BCH CĐCS'),
            ('Uỷ viên BCH CĐCS','Uỷ viên BCH CĐCS'),
            ('Tổ trưởng', 'Tổ trưởng'),
            ('Tổ phó', 'Tổ phó'),
            ('Người lao động', 'Người lao động'),
        ],
        null=True,
        blank=True
    )
    
    def __str__(self):
        return self.name