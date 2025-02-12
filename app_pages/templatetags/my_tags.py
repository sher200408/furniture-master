
from django import  template

register = template.Library()


@register.simple_tag
def get_lange_url(request,lang):
    '/en/blogs/2/comments'
    url = request.path.split('/')
    url[1]= lang
    return '/'.join(url)

@register.simple_tag
def get_lang_flog(lang):
    if lang == "en":
        return "🌌En"
    elif lang == "uz":
        return "🌍Uz"
    elif lang == "ru":
        return "🪐RU"