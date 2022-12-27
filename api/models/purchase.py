from django.db import models
from django.utils.translation import gettext as _

from api.models import User, Ticket
from mixins.models import (
    TimeStampMixin,
    IsActiveMixin,
)


class Purchase(TimeStampMixin, IsActiveMixin):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='purchases',
        verbose_name=_('User'),
    )
    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        related_name='purchases',
        verbose_name=_('Ticket'),
    )

    class Meta:
        verbose_name = _('Purchase')
        verbose_name_plural = _('Purchases')
        unique_together = ('user', 'ticket')

    def __str__(self):
        return f'{self.user} - {self.ticket}'
