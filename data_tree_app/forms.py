from django import forms
from data_tree_app.models import File
from mptt.forms import TreeNodeChoiceField


class FileForm(forms.Form):
    # name = models.CharField(max_length=60, unique=True)
    # parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    # isFile = models.BooleanField(default=False)
    isFile = forms.BooleanField(required=False)
    parent = TreeNodeChoiceField(queryset=File.objects.all())
    name = forms.CharField(max_length=60)


#Create page for form, view for that and submission of form