import os
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from django.conf import settings
from .models import FileUpload
from .serializers import FileUploadSerializer
from .services import convert_file
from django.http import FileResponse
from django.shortcuts import get_object_or_404


# Create your views here.


@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def upload_and_convert_file(request):
    if 'file' not in request.FILES:
        return Response({"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST)

    uploaded_file = request.FILES['file']
    file_extension = uploaded_file.name.split('.')[-1].lower()

    file_upload = FileUpload.objects.create(
        file=uploaded_file,
        original_file_extension=file_extension
    )

    uploaded_file_path = file_upload.file.path
    unique_folder = uploaded_file_path.split('/')[-2]

    converted_folder = os.path.join(settings.MEDIA_ROOT, 'converted', unique_folder)
    os.makedirs(converted_folder, exist_ok=True)

    converted_files = convert_file(uploaded_file_path, file_extension, converted_folder)

    file_upload.converted_files = converted_files
    file_upload.save()

    return Response({
        "message": "File uploaded and converted successfully",
        "file_id": file_upload.pk,
        "original_file": file_upload.file.url,
        "converted_files": converted_files
    }, status=status.HTTP_201_CREATED)





@api_view(['GET'])
def download_converted_file(request, file_type, file_id):
    file_upload = get_object_or_404(FileUpload, id=file_id)
    
    if file_type not in file_upload.converted_files:
        return Response({"error": "File type not found"}, status=status.HTTP_404_NOT_FOUND)
    
    file_path = file_upload.converted_files[file_type]
    
    if not os.path.exists(file_path):
        return Response({"error": "File not found"}, status=status.HTTP_404_NOT_FOUND)

    return FileResponse(open(file_path, 'rb'), as_attachment=True)
















