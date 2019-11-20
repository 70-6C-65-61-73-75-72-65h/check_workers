# myapp/tasks.py
 
import logging
 
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from app.celery import app

from .models import Simulation, get_simulation
# import myapp.models

@app.task
def simulate_days(sim_id):
    sim = Simulation.objects.get(id=sim_id)
    print('\n\nstart in simulate_days\n\n')
    it = 0
    while sim.status == True:
        it += 1
        print(f'\n\n {it} iter in simulate_days\n\n')
        sim.daemon_active = True
        sim.today = sim.today + timedelta(1)
        time.sleep(5)
        # если мы паралельно что-то изменили из вне этого демона в этой симуляции, то без refresh_from_db 
        # запишется то что мы тут изменяли это время ( это разумнее для сохранения изменения из демона в бд )
        sim.refresh_from_db()# а вот здесь надо уже проверить не нажали ли мы стоп симуляция пока проходила симуляция  
        sim.save()
        sim.refresh_from_db() # а вот здесь надо уже проверить не нажали ли мы стоп симуляция пока проходила симуляция\
    # демон в ноль чтоб можно было потом опять создавать этого демона по симуляции времени
    print('\n\nend in simulate_days\n\n')
    sim.daemon_active = False
    sim.save()


from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

@receiver(post_save, sender=Simulation)
def simulation_daemon(sender, instance, created, **kwargs):
    # maybe be a lot of daemons if i do that all the time when status=True
    # print(f'receiver simulation_daemon status:{instance.status} and daemon_active:{instance.daemon_active}')
    if instance.status == True and instance.daemon_active == False: # тоесть мы только только запустили симуляцию и демона пока нету
        print('start simulation_daemon')
        simulate_days.delay(instance.id)
        print('end simulation_daemon')

# @app.task
# def send_verification_email(user_id):
#     UserModel = get_user_model()
#     try:
#         user = UserModel.objects.get(pk=user_id)
#         send_mail(
#             'Verify your QuickPublisher account',
#             'Follow this link to verify your account: '
#                 'http://localhost:8000%s' % reverse('verify', kwargs={'uuid': str(user.verification_uuid)}),
#             'from@quickpublisher.dev',
#             [user.email],
#             fail_silently=False,
#         )
#     except UserModel.DoesNotExist:
#         logging.warning("Tried to send verification email to non-existing user '%s'" % user_id)
