from django.db import models


class Executor(models.Model):
    name = models.CharField('Иcполнитель', max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'
    

class Task(models.Model):
    created_at = models.DateTimeField('Дата создания')
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE)
    priority = models.IntegerField('Приоритет', choices=[(x, str(x)) for x in range(1, 4)])
    title = models.CharField('Заголовок', max_length=255)
    comment = models.TextField('Комментарий', blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        
