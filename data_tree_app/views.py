from django.shortcuts import render, reverse, HttpResponseRedirect
from data_tree_app.models import File
from data_tree_app.forms import FileForm

def file_view(request):
    return render(request, 'index.html', {'files': File.objects.all()})

def form_view(request):
    form = FileForm()
    return render(request, 'form.html', {'form': form})

def form_submit(request):
    if request.method == 'POST':
        form = FileForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            File.objects.create(
                # name = models.CharField(max_length=60, unique=True)
                # parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
                # isFile = models.BooleanField(default=False)
                name = data['name'],
                parent = data['parent'],
                isFile = data['isFile']
            )
            return HttpResponseRedirect(reverse('home'))
