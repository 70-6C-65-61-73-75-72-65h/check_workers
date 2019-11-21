from django.db import models

# Create your models here.
class Simulation(models.Model):
    # changed every simul day
    created_date = models.DateField(auto_now_add=True)
    today = models.DateField(auto_now=False, auto_now_add=False)
    status = models.BooleanField(default=False)
    daemon_active = models.BooleanField(default=False)
    info = models.TextField()

    def get_simulation_day(self):
        """Сколько дней прошло с начала симуляции"""
        return (self.today - self.created_date).days

def get_simulation():
    return Simulation.objects.all().last()
