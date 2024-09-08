from django.shortcuts import render, redirect, get_object_or_404
from .forms import UploadFileForm, PassFileForm
from .models import UploadedFile

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            comment = form.cleaned_data['comment']
            uploaded_file = UploadedFile(file=file, comment=comment)
            uploaded_file.save()
            return redirect('file_list')
    else:
        form = UploadFileForm()
    return render(request, 'tracker/upload_file.html', {'form': form})

def file_list(request):
    files = UploadedFile.objects.all()
    return render(request, 'tracker/file_list.html', {'files': files})

def view_logs(request, file_id):
    file = get_object_or_404(UploadedFile, id=file_id)
    return render(request, 'tracker/view_logs.html', {'file': file})

def pass_file(request, file_id):
    file = get_object_or_404(UploadedFile, id=file_id)
    if request.method == 'POST':
        form = PassFileForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            file.is_passed = True
            file.passed_to = user
            file.save()
            return redirect('file_list')
    else:
        form = PassFileForm()
    return render(request, 'tracker/pass_file.html', {'form': form, 'file': file})