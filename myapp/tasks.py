# myapp/tasks.py
 
import logging
 
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from app.celery import app

from .models import Simulation, get_simulation
# import myapp.models
from datetime import timedelta
import datetime
import time
@app.task(name='app.myapp.tasks.simulate_days')
def simulate_days(sim_id):
    print('\n\n start in simulated day \n\n')
    sim = Simulation.objects.get(id=sim_id)
    if sim.status == True:
        sim.daemon_active = True
        sim.today = sim.today + timedelta(1)
        sim.save()
        simulate_days.apply_async(queue='low_priority', args=(instance.id), countdown=5)
    print('\n\nend in simulate_days\n\n')
    # if this is the first break from the if sim.status == True condition -> firstly change daemon_active value and then it not gonna be changed
    if sim.daemon_active == True and sim.status == False:
        sim.daemon_active = False
        sim.save()


from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

@receiver(post_save, sender=Simulation)
def simulation_daemon(sender, instance, created, **kwargs):
    # maybe be a lot of daemons if i do that all the time when status=True
    # print(f'receiver simulation_daemon status:{instance.status} and daemon_active:{instance.daemon_active}')
    if instance.status == True and instance.daemon_active == False: # тоесть мы только только запустили симуляцию и демона пока нету
        print('start tasks')
        simulate_days.apply_async(args=[instance.id], queue='low_priority', countdown=5)
        print('end tasks')
        # eta=datetime.datetime.now() + timedelta(seconds=5)
        # countdown=5
        # datetime.datetime.now()