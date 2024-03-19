from django.db import models

# Create your models here.
class CommonModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) # 생성된 시간
    updated_at = models.DateTimeField(auto_now=True) # 데이터가 업데이트된 시간 (업데이트 할 때 마다 시간 갱신)
    
    class Meta:
        abstract = True # DB에 테이블 생성을 막아줌
    