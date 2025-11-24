# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError

class Game(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def delete(self):
        if self.score_set.exists():
            raise ValidationError(
                "Cannot delete game with existing scores. Tournament has active games."
            )
        super().delete()