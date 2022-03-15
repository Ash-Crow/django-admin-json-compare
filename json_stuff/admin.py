import json
from django.contrib import admin
from json_stuff import models
from deepdiff import DeepDiff

from django_admin_json_compare import json_compare

# Register your models here.


@admin.register(models.Stuff)
class StuffAdmin(admin.ModelAdmin):
    def view_json_diff(self, obj):
        return json_compare(obj.json_current, obj.json_new)

    view_json_diff.short_description = "Différence"

    def view_raw_json_diff(self, obj):
        ddiff = DeepDiff(obj.json_current, obj.json_new, ignore_order=True, verbose_level=2).to_json()
        return ddiff

    view_raw_json_diff.short_description = "Différence brute"

    readonly_fields = ["view_json_diff", "view_raw_json_diff"]

    class Media:
        css = {"all": ("json_compare.css",)}
