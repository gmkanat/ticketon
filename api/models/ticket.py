from django.db import models
from django.utils.translation import gettext as _

from mixins.models import (
    TimeStampMixin,
    IsActiveMixin,
)


class Category(TimeStampMixin, IsActiveMixin):
    name = models.CharField(
        max_length=255,
        verbose_name=_('Name'),
    )
    image = models.ImageField(
        upload_to='categories',
        verbose_name=_('Image'),
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name


class Image(TimeStampMixin, IsActiveMixin):
    image = models.ImageField(
        upload_to='images',
        verbose_name=_('Image'),
    )

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')

    def __str__(self):
        return self.image.url


class City(IsActiveMixin):
    name = models.CharField(
        max_length=255,
        verbose_name=_('Name'),
    )

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Cities')

    def __str__(self):
        return self.name


class TicketPrice(TimeStampMixin, IsActiveMixin):
    STUDENT = 'STUDENT'
    CHILD = 'CHILD'
    PENSIONER = 'PENSIONER'
    ADULT = 'ADULT'
    PERSON_TYPE_CHOISES = [
        (STUDENT, STUDENT),
        (CHILD, CHILD),
        (PENSIONER, PENSIONER),
        (ADULT, ADULT),
    ]
    person_type = models.CharField(
        max_length=255,
        choices=PERSON_TYPE_CHOISES,
        default=ADULT,
    )
    price = models.IntegerField(
        verbose_name=_('Price'),
        default=0,
    )

    class Meta:
        verbose_name = _('Price')
        verbose_name_plural = _('Prices')

    def __str__(self):
        return f'{self.person_type} {self.price}'


class Ticket(TimeStampMixin, IsActiveMixin):
    name = models.CharField(
        max_length=255,
        verbose_name=_('Name'),
    )
    description = models.TextField(
        verbose_name=_('Description'),
        null=True,
        blank=True,
    )
    price = models.ManyToManyField(
        TicketPrice,
        related_name='tickets',
        verbose_name=_('Prices'),
    )
    images = models.ManyToManyField(
        Image,
        related_name='tickets',
        verbose_name=_('Images'),
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='tickets',
        verbose_name=_('Category'),
        null=True,
        blank=True,
    )
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name='tickets',
        verbose_name=_('City'),
        null=True,
        blank=True,
    )
    start_time = models.DateTimeField(
        verbose_name=_('Start time'),
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _('Ticket')
        verbose_name_plural = _('Tickets')

    def __str__(self):
        return self.name
