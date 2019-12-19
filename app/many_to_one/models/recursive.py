from django.db import models


class WPSUser(models.Model):
    name = models.CharField(max_length=20)
    instructor = models.ForeignKey('self', on_delete=models.SET_NULL,
                                   null=True, # SET_NULL 을 하는 것은 null이 참인것을 허용한다는 뜻이다
                                   related_name='student_set')

    def __str__(self):
        return self.name
