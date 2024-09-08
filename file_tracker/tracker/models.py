from django.db import models
from django.contrib.auth.models import User

class File(models.Model):
    unique_id = models.CharField(max_length=100, unique=True)
    file_name = models.CharField(max_length=255)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name

class FileLog(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    passed_from = models.ForeignKey(User, related_name='passed_from', on_delete=models.CASCADE)
    passed_to = models.ForeignKey(User, related_name='passed_to', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.file.file_name} passed from {self.passed_from} to {self.passed_to}'

class FileHolder(models.Model):
    file = models.OneToOneField(File, on_delete=models.CASCADE)
    current_holder = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.file.file_name} is with {self.current_holder}'
from django.db import models
from django.contrib.auth.models import User

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    comment = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_passed = models.BooleanField(default=False)
    passed_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='passed_files')