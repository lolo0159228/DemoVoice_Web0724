from django import template
from home.models import Voice

register = template.Library()

@register.simple_tag
def get_like_status(SongId,user):
    i = Voice.objects.get(Songname=SongId)
    j = i.like.filter(account_number=user)
    if j:
        return "btn-danger likeactive"
    else:
        return "btn-light"
