from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from projectapp.models import Project


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='subscription', null=False)  # cascade 종속된, 우저가 삭제되면 구독정보도 사라짐
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='subscription', null=False)

    # 메타클래스, 필드를 제외한 메타데이터를 말함. 이미지를 예로들면 이미지 자체가 아닌 이미지 사이즈, 생성시간 등을 말함
    class Meta:
        # db에서 user, project가 유니크하게 설정됨
        unique_together = ['user', 'project']

