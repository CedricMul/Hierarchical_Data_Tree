from django.contrib import admin
from data_tree_app.models import File
from mptt.admin import DraggableMPTTAdmin

admin.site.register(
    File,
    DraggableMPTTAdmin
    )
