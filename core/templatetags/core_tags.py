from django import template
from django.urls import resolve

register = template.Library()

@register.simple_tag(takes_context=True)
def url_replace_settlement(context, target_slug):
    """
    Меняет текущий поселок в URL на целевой.
    Например: /zapovednoe/news/ -> /kolosok/news/
    """
    request = context['request']
    path = request.path
    
    # Получаем текущий slug из URL (он передается во views)
    # Обычно он есть в context, но надежнее взять из path
    # Наша структура: /slug/...
    
    path_parts = path.strip('/').split('/')
    
    if path_parts:
        current_slug = path_parts[0]
        # Если первый элемент пути — это наш текущий поселок, меняем его
        if current_slug in ['zapovednoe', 'kolosok']:
            # Заменяем только первое вхождение
            return path.replace(current_slug, target_slug, 1)
            
    # Если что-то пошло не так, возвращаем корень целевого поселка
    return f"/{target_slug}/"