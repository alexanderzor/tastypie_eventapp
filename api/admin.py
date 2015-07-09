from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from models import New, Broadcast, Summary

class NewsAdmin(admin.ModelAdmin):
    #details = forms.CharField(widget=CKEditorWidget())
    list_display = ('title','date', 'time')

    class Meta:
        model = New

admin.site.register(New, NewsAdmin)

class BroadcastAdmin(admin.ModelAdmin):
    day = forms.CheckboxSelectMultiple
    list_display = ('title', 'time', 'day')

    class Meta:
        model = Broadcast

admin.site.register(Broadcast, BroadcastAdmin)


class SummaryAdmin(admin.ModelAdmin):
    list_display = ('title',)

    class Meta:
        model = Summary

admin.site.register(Summary, SummaryAdmin)
