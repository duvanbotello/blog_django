from django import template
from users.models import InformationUsers

register = template.Library()

@register.simple_tag
def user_imagen(user):
    user_information = InformationUsers.objects.filter(user=user).first()
    if user_information:
        return user_information.imagen.url
    
    