from django import template

register = template.Library()

#without decorator
# def myreplace(value,arg):
#     return value.replace(arg, 'We are')
#
# register.filter('iamToweare', myreplace)

#with decorator
@register.filter(name='iamToweare')
def myreplace(value,arg):
    return value.replace(arg, 'We are')