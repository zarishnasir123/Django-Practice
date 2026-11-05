from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
from django.db.models.signals import pre_init, pre_save, pre_delete, post_save, post_init, post_delete, post_init ,pre_migrate, post_migrate
from django.core.signals import request_started, request_finished, got_request_exception



# @receiver(user_logged_in, sender=User)
# def login_success(sender, request, user, **kwargs):
#     print("-------------------------")
#     print("logged-in Signal... Run Intro..")
#     print("Sender:", sender)
#     print("Request:", request)
#     print("User", user)
#     print("User Password: ", user.password)
#     print(f'Kwargs: {kwargs}')
    
# # user_logged_in.connect(login_success, sender=User)

# @receiver(user_logged_out, sender=User)
# def log_out(sender, request, user, **kwargs):
#     print("-------------------------")
#     print("logged-out Signal... Run Outro..")
#     print("Sender:", sender)
#     print("Request:", request)
#     print("User", user)
#     print(f'Kwargs: {kwargs}')
        
      
# @receiver(user_login_failed)  
# def login_failed(sender, credentials, request, **kwargs):
#     print("-------------------------")
#     print("log in Failed Signal...")
#     print("Sender:", sender)
#     print("credentials", credentials)
#     print("Request:", request)
#     print(f'Kwargs: {kwargs}')
    
    
@receiver(pre_save, sender=User)
def at_beginning_save(sender, instance, **kwargs):
    print("------------------------------")
    print("pre save signal---")
    print("Sender:", sender)
    print("instance:", instance)
    print(f'Kwargs: {kwargs}')
    
    
@receiver(post_save, sender=User)
def at_ending_save(sender, instance, created, **kwargs):
    print("------------------------------")
    print("post save signal---")
    print("Sender:", sender)
    print("instance:", instance)
    print("created:", created)  #True = new record, False = update
    print(f'Kwargs: {kwargs}')


@receiver(pre_delete, sender=User)
def at_beginning_delete(sender, instance, **kwargs):
    print("------------------------------")
    print("pre delete signal---")
    print("Sender:", sender)
    print("instance:", instance)
    print(f'Kwargs: {kwargs}')


@receiver(post_delete, sender=User)
def at_ending_delete(sender, instance, **kwargs):
    print("------------------------------")
    print("post delete signal---")
    print("Sender:", sender)
    print("instance:", instance)
    print(f'Kwargs: {kwargs}')


#init signals run every time a User object is created in Python (also when loaded from the db)
@receiver(pre_init, sender=User)
def at_beginning_init(sender, *args, **kwargs):
    print("------------------------------")
    print("pre init signal---")
    print("Sender:", sender)
    print(f'Args: {args}')
    print(f'Kwargs: {kwargs}')


@receiver(post_init, sender=User)
def at_ending_init(sender, *args, **kwargs):
    print("------------------------------")
    print("post init signal---")
    print("Sender:", sender)
    print(f'Args: {args}')
    print(f'Kwargs: {kwargs}')


#migrate signals: sender is the app's config, they run for every app on "python manage.py migrate"
@receiver(pre_migrate)
def before_install_app(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print("------------------------------")
    print("pre migrate signal---")
    print("Sender:", sender)
    print("app_config:", app_config)
    print("verbosity:", verbosity)
    print("interactive:", interactive)
    print("using:", using)
    print("plan:", plan)
    print("apps:", apps)
    print(f'Kwargs: {kwargs}')


@receiver(post_migrate)
def after_install_app(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print("------------------------------")
    print("post migrate signal---")
    print("Sender:", sender)
    print("app_config:", app_config)
    print("verbosity:", verbosity)
    print("interactive:", interactive)
    print("using:", using)
    print("plan:", plan)
    print("apps:", apps)
    print(f'Kwargs: {kwargs}')


#request signals: no model involved, they run for every request to the site
@receiver(request_started)
def at_beginning_request(sender, environ, **kwargs):
    print("------------------------------")
    print("request started signal---")
    print("Sender:", sender)
    print("Environ:", environ)
    print(f'Kwargs: {kwargs}')


@receiver(request_finished)
def at_ending_request(sender, **kwargs):
    print("------------------------------")
    print("request finished signal---")
    print("Sender:", sender)
    print(f'Kwargs: {kwargs}')


#runs only when a view raises an error
@receiver(got_request_exception)
def at_request_exception(sender, request, **kwargs):
    print("------------------------------")
    print("got request exception signal---")
    print("Sender:", sender)
    print("Request:", request)
    print(f'Kwargs: {kwargs}')
