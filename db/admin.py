from django.contrib import admin
from db.models import *


# Register your models here.
class FacultAdmin(admin.ModelAdmin):
    list_display = ['name']

    class Meta:
        models = Facult


admin.site.register(Facult, FacultAdmin)


class StatusAdmin(admin.ModelAdmin):
    list_display = ['name']

    class Meta:
        models = Status


admin.site.register(Status, StatusAdmin)


class DocumentAdmin(admin.ModelAdmin):
    list_display = ['people', 'tip', 'date', 'file']
    list_filter = ['tip']
    search_fields = ['people__fio']

    class Meta:
        models = Document


admin.site.register(Document, DocumentAdmin)


class PeopleAdmin(admin.ModelAdmin):
    list_display = ['obshaga', 'komnata', 'fio', 'birthday', 'status', 'facult', 'zahislenie', 'uhod', 'image', ]
    search_fields = ['obshaga', 'komnata', 'fio', 'status', 'facult']
    list_filter = ['obshaga']

    class Meta:
        models = People


admin.site.register(People, PeopleAdmin)


class TipAdmin(admin.ModelAdmin):
    list_display = ['name']

    class Meta:
        models = Tip


admin.site.register(Tip, TipAdmin)


class ObshagaAdmin(admin.ModelAdmin):
    list_display = ['name']

    class Meta:
        models = Obshaga


admin.site.register(Obshaga, ObshagaAdmin)
