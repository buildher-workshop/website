from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    register_setting,
)
from wagtail.fields import RichTextField
from wagtail.models import Page


@register_setting
class SocialMedia(BaseGenericSetting):
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)


class Section(Page):
    introduction = RichTextField(blank=True)
    banner = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    content = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("introduction"),
        FieldPanel("banner"),
        FieldPanel("content"),
        FieldPanel("show_in_menus"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["static_pages"] = Section.objects.live().in_menu()
        context["posts"] = Post.objects.child_of(self).live()
        context["is_root"] = self.get_site().root_page.pk == self.pk
        return context


class Post(Page):
    banner = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    introduction = RichTextField()
    content = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("banner"),
        FieldPanel("introduction"),
        FieldPanel("content"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["static_pages"] = Section.objects.live().in_menu()
        return context
