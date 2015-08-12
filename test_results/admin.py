from django.contrib import admin

from .models import STDTest

# Register your models here.

class STDTestAdmin(admin.ModelAdmin):
    """

    """
    list_display = ('unique_id',
                    'std_name',
                    'result',
                    'test_date',
                    'result_date'
    )

    list_filter = ('result',
                   'test_date',
    )

admin.site.register(STDTest, STDTestAdmin)
