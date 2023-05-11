from django.contrib import admin
from qbank.models import Qbank


class QbankAdmin(admin.ModelAdmin):
    """Override for the `Qbank` model

    Added to prevent display of `created_at` and `last_updated` attributes
    to user as these are generated automatically.
    """

    exclude = ('created_at', 'last_updated',)


admin.site.register(Qbank, QbankAdmin)
