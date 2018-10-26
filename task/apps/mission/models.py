from django.db import models
from db.base_model import BaseModel

#class missionManager(models.Manager):
    #def all(self):


class mission(BaseModel):
    """任务类"""
    STATUS_CHOICE=(
        (0,'未完成'),
        (1,'已完成'),
    )
    PRIORITY_CHOICE=(
        (0,'first'),
        (1,'second'),
        (2,'third')
    )
    CATEGORY_CHOICE=(
        (1,'学习'),
        (2,'锻炼'),
        (3,'娱乐')
    )
    DURATION_CHOICE=(
        (1,'日任务'),
        (2,'周任务'),
        (3,'月任务'),
    )
    name=models.ForeignKey('user.User',verbose_name='用户',on_delete=models.CASCADE)
    status=models.SmallIntegerField(choices=STATUS_CHOICE,default=0,verbose_name='状态')
    priority=models.SmallIntegerField(choices=PRIORITY_CHOICE,default=0,verbose_name='优先级')
    category=models.SmallIntegerField(choices=CATEGORY_CHOICE,default=1,verbose_name='类型')
    content=models.TextField(verbose_name='内容')
    is_ontime=models.BooleanField(default=1,verbose_name='是否按时完成')#1代表未完成，0代表已完成
    startdate=models.DateTimeField( verbose_name="开始时间")
    enddate=models.DateTimeField( verbose_name="结束时间")
    duration=models.SmallIntegerField(choices=DURATION_CHOICE,verbose_name='时间跨度')

    #objects=missionManager() #自定义一个missionManager管理器类的对象






