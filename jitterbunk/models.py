from django.db import models

class User(models.Model):
    username = models.CharField(max_length=200)
    photo = models.CharField(max_length=200)

    def __str__(self):
        return self.username


class Bunk(models.Model):
    from_user = models.ForeignKey("User", on_delete=models.CASCADE, related_name='from_user')
    to_user = models.ForeignKey("User", on_delete=models.CASCADE, related_name='to_user')
    time = models.TimeField()

    def __str__(self):
        string = str(self.from_user) + " bunked " + str(self.to_user)
        return string

