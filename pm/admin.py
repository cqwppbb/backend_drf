from django.contrib import admin
from pm import models

# Register your models here.


class machine_data_admin(admin.ModelAdmin):
    list_display = ("area", "station", "item", "val", "ctime")


class pm_data_admin(admin.ModelAdmin):
    list_display = (
        "area",
        "machine",
        "station",
        "item",
        "detail",
        "frequency",
        "type",
        "ctime",
    )


class pm_push_admin(admin.ModelAdmin):
    list_display = (
        "area",
        "machine",
        "station",
        "item",
        "detail",
        "frequency",
        "type",
        "val_last",
        "val_current",
        "time_last",
        "life",
        "push",
        "done",
        "ctime",
    )


class pm_finish_record_admin(admin.ModelAdmin):
    list_display = (
        "area",
        "machine",
        "station",
        "item",
        "detail",
        "frequency",
        "type",
        "life",
        "user",
        "ctime",
    )


class pm_modify_record_admin(admin.ModelAdmin):
    list_display = (
            "area",
            "machine",
            "station",
            "item",
            "detail",
            "frequency",
            "type",
            "user",
            "ctime",
    )


admin.site.register(models.machine_data, machine_data_admin)
admin.site.register(models.pm_data, pm_data_admin)
admin.site.register(models.pm_push, pm_push_admin)
admin.site.register(models.pm_finish_record, pm_finish_record_admin)
admin.site.register(models.pm_modify_record, pm_modify_record_admin)


admin.site.site_header = "PM后台数据台账"
admin.site.site_title = "PM后台数据台账"
admin.site.index_title = "PM数据"
