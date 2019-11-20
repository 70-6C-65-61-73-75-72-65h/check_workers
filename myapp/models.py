from django.db import models


# from django.db.models.signals import post_save, pre_save
# from django.dispatch import receiver

# import myapp.tasks as tasks


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
        # sim = Simulation.objects.all().last()
        return (self.today - self.created_date).days

def get_simulation():
    return Simulation.objects.all().last()


# @receiver(post_save, sender=Simulation)
# def simulation_daemon(sender, instance, signal, *args, **kwargs):
#     # maybe be a lot of daemons if i do that all the time when status=True
#     if instance.status == True and instance.daemon_active == False: # тоесть мы только только запустили симуляцию и демона пока нету
#         tasks.simulate_days.delay(instance.id)
    # if

# signals.post_save.connect(simulation_daemon, sender=Simulation)