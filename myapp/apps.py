from django.apps import AppConfig


class MyappConfig(AppConfig):
    name = 'myapp'
    label = 'myapp'

    def ready(self):
        # for receivers in tasks
        import myapp.tasks
