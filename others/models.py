from django.db import models
from django.utils.translation import gettext_lazy as _


class About(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name=_("about_title"),
        default="About us"
    )
    subtitle = models.CharField(
        max_length=200,
        null=True, blank=True,
        verbose_name=_("about_subtitle"),
    )
    description = models.TextField(
        null=True, blank=True,
        verbose_name=_("about_description"),
    )
    ending = models.TextField(
        null=True, blank=True,
        verbose_name=_("about_ending"),
    )

    class Meta:
        verbose_name = _("About Section")
        verbose_name_plural = _("About Sections")

    def __str__(self):
        return self.title


class Contact(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name=_("contact_title"),
        default="Contact"
    )
    subtitle = models.CharField(
        max_length=200,
        null=True, blank=True,
        verbose_name=_("contact_subtitle"),
    )
    person = models.CharField(
        max_length=200,
        null=True, blank=True,
        verbose_name=_("contact_name"),
    )
    description = models.TextField(
        null=True, blank=True,
        verbose_name=_("contact_description"),
    )
    ending = models.TextField(
        null=True, blank=True,
        verbose_name=_("contact_ending"),
    )

    class Meta:
        verbose_name = _("contact Section")
        verbose_name_plural = _("contact Sections")

    def __str__(self):
        return self.title


class Terms(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name=_("terms_title"),
        default="Terms & Conditions"
    )
    subtitle_1 = models.CharField(
        max_length=200,
        null=True, blank=True,
        verbose_name=_("terms_subtitle_1"),
    )
    description_1 = models.TextField(
        null=True, blank=True,
        verbose_name=_("terms_description_1"),
    )
    subtitle_2 = models.CharField(
        max_length=200,
        null=True, blank=True,
        verbose_name=_("terms_subtitle_2"),
    )
    description_2 = models.TextField(
        null=True, blank=True,
        verbose_name=_("terms_description_2"),
    )

    class Meta:
        verbose_name = _("Terms Section")
        verbose_name_plural = _("Terms Sections")

    def __str__(self):
        return self.title


class Part(models.Model):
    terms = models.ForeignKey(
        Terms,
        on_delete=models.CASCADE,
        related_name="parts",
        verbose_name=_("related_terms")
    )
    part = models.CharField(
        max_length=50,
        verbose_name=_("part_label")
    )
    partno = models.CharField(
        max_length=50,
        verbose_name=_("part_number")
    )
    partname = models.CharField(
        max_length=200,
        verbose_name=_("part_name")
    )
    partdesc = models.TextField(
        null=True, blank=True,
        verbose_name=_("part_description")
    )

    class Meta:
        verbose_name = _("Terms Part")
        verbose_name_plural = _("Terms Parts")
        ordering = ['partno']

    def __str__(self):
        return f"{self.part} {self.partno}: {self.partname}"


class Section(models.Model):
    terms = models.ForeignKey(
        Terms,
        on_delete=models.CASCADE,
        related_name="sections",
        verbose_name=_("related_terms")
    )
    sect = models.CharField(
        max_length=50,
        verbose_name=_("section_label")
    )
    sectno = models.CharField(
        max_length=50,
        verbose_name=_("section_number")
    )
    sectname = models.CharField(
        max_length=200,
        verbose_name=_("section_name")
    )
    sectdesc = models.TextField(
        null=True, blank=True,
        verbose_name=_("section_description")
    )

    class Meta:
        verbose_name = _("Terms Section Detail")
        verbose_name_plural = _("Terms Section Details")
        ordering = ['sectno']

    def __str__(self):
        return f"{self.sect} {self.sectno}: {self.sectname}"


class Privacy(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name=_("privacy_title"),
        default="Privacy"
    )
    description = models.TextField(
        null=True, blank=True,
        verbose_name=_("privacy_description"),
    )
    ending = models.TextField(
        null=True, blank=True,
        verbose_name=_("privacy_ending"),
    )

    class Meta:
        verbose_name = _("Privacy Section")
        verbose_name_plural = _("Privacy Sections")

    def __str__(self):
        return self.title


class Faq(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name=_("faq_title"),
        default="FAQ"
    )
    subtitle = models.CharField(
        max_length=200,
        null=True, blank=True,
        verbose_name=_("faq_subtitle"),
    )
    question = models.CharField(
        max_length=500,
        null=True, blank=True,
        verbose_name=_("faq_question"),
    )
    answer = models.TextField(
        null=True, blank=True,
        verbose_name=_("faq_answer"),
    )

    class Meta:
        verbose_name = _("Faq Section")
        verbose_name_plural = _("Faq Sections")
        ordering = ["id",]

    def __str__(self):
        return self.title
