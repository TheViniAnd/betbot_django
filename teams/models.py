from django.db import models
from django.utils import timezone

class Team(models.Model):
    name = models.TextField(verbose_name='Название команды:', default='')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команда"

class Time_Kill(models.Model):
    team = models.ForeignKey(Team, models.SET_NULL, blank=True, null=True, related_name='team',
                             verbose_name='Команда:')
    time_map = models.IntegerField(verbose_name='Время игры:')
    kill_map = models.IntegerField(verbose_name='Убийств:')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        template = '{0.team} Время:{0.time_map} Килл:{0.kill_map}'
        return template.format(self)

    class Meta:
        verbose_name = "Totals"
        verbose_name_plural = "totals"


class Totals(models.Model):
    one_team = models.ForeignKey(Team, models.SET_NULL, blank=True, null=True,related_name='OneTeam', verbose_name='Первая команда')
    two_team = models.ForeignKey(Team, models.SET_NULL, blank=True, null=True,related_name='TwoTeam', verbose_name='Вторая команда')
    names = one_team,'|',two_team
    def __str__(self):
        return self.names
    class Meta:
        verbose_name = "Тотал"
        verbose_name_plural = "Тотал"