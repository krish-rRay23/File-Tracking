from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import File, FileLog, FileHolder
from .forms import FileForm, PassFileForm

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.uploaded_by = request.user
            file.save()
            FileHolder.objects.create(file=file, current_holder=request.user)
            return redirect('file_list')
    else:
        form = FileForm()
    return render(request, 'tracker/upload_file.html', {'form': form})

@login_required
def pass_file(request, file_id):
    file = File.objects.get(id=file_id)
    if request.method == 'POST':
        form = PassFileForm(request.POST)
        if form.is_valid():
            passed_to = form.cleaned_data['passed_to']
            FileLog.objects.create(file=file, passed_from=request.user, passed_to=passed_to)
            file_holder = FileHolder.objects.get(file=file)
            file_holder.current_holder = passed_to
            file_holder.save()
            return redirect('file_list')
    else:
        form = PassFileForm()
    return render(request, 'tracker/pass_file.html', {'form': form, 'file': file})

@login_required
def file_list(request):
    files = File.objects.filter(uploaded_by=request.user)
    return render(request, 'tracker/file_list.html', {'files': files})

@login_required
def file_log(request, file_id):
    logs = FileLog.objects.filter(file_id=file_id)
    return render(request, 'tracker/file_log.html', {'logs': logs})
