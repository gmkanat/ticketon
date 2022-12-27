from django.db import models
from django.utils.translation import gettext as _

from mixins.models import (
    TimeStampMixin,
    IsActiveMixin,
)
from api.models import Ticket


class Comment(TimeStampMixin, IsActiveMixin):
    message = models.CharField(
        max_length=2048,
        verbose_name=_('message'),
    )
    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name=_('Comments')
    )

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

    def __str__(self):
        return self.message[:100]

