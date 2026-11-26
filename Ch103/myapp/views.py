import logging
from django.http import HttpResponse

# a logger named after this file: 'myapp.views'. It uses the 'myapp' settings of LOGGING in settings.py
logger = logging.getLogger(__name__)

# Create your views here.
def home(request):
    # one message for each level, from the lowest to the highest
    logger.debug('debug: details that help while writing the code')
    logger.info('info: the home page was opened')
    logger.warning('warning: something unexpected, but the page still works')
    logger.error('error: something failed')
    logger.critical('critical: a very serious problem, the app may stop')
    return HttpResponse('<h1>Home Page</h1>')
