from django import template
from django.template import loader

from mezzanine.pages.models import Page

register = template.Library()


@register.simple_tag
def page_by_slug(slug):
    """
    Returns a page instance into the template context.
    :param slug: Slug name of the page instance
    :return: A Page instance
    """
    try:
        page = Page.objects.get(slug=slug)
        if page.__class__ == 'Page':
            page = page.get_content_model()
        return page
    except Page.DoesNotExist:
        return None


@register.simple_tag
def get_page_children(page, model=None):
    """
    Returns a children of the page. Pages can be filtered out by the model
    name.
    :param page: A page instance
    :param model: Optional model name string
    :return: A list of pages
    """
    children = Page.objects.filter(parent=page)
    children = [p.get_content_model() for p in children]
    if model:
        children = [p for p in children if p.__class__.__name__ == model]
    return children


@register.simple_tag()
def get_top_pages(model=None):
    """
    Returns a list of pages with no parent. Pages can be filtered out by the
    model name.
    :param model: Optional model name string
    :return: A list of pages
    """
    return get_page_children(page=None, model=model)


@register.simple_tag(takes_context=True)
def box(context, page, template_name=None):
    template_name = template_name if template_name else'boxes/box.html'
    template = loader.get_template(template_name)
    context['page'] = page
    output = template.render(context)
    return output