from django.contrib import admin
from .models import PatientProfile, PatientRecord, PatientSTDTest, PatientApproval
from test_results.models import STDTest

class PatientSTDTestInLine(admin.TabularInline):
    model = PatientSTDTest
    extra = 0

class PatientProfileAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'surname',
                    'unique_id',
                    'date_of_birth',
                    'location',
    )

    list_filter = ('surname',
        'location',
    )

    search_fields = ('name',
                     'surname',
                     'location',
    )

class PatientRecordAdmin(admin.ModelAdmin):
    inlines = (PatientSTDTestInLine,)

class PatientSTDTestAdmin(admin.ModelAdmin):
    list_display = ('test',
                    'record',
    )

class PatientApprovalAdmin(admin.ModelAdmin):
    list_display = ('approval',
                    'last_checkup',
    )

admin.site.register(PatientSTDTest, PatientSTDTestAdmin)
admin.site.register(PatientProfile, PatientProfileAdmin)
admin.site.register(PatientRecord, PatientRecordAdmin)
admin.site.register(PatientApproval, PatientApprovalAdmin)