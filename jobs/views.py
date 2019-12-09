from django.shortcuts import render
from django.http import FileResponse
from pathlib import Path

# Create your views here.

def index(request):
    return render(request, 'jobs/home.html')

def cv_download(request):
    pdf_file = Path(Path().cwd(),'Ayodele--Akinbohun--Software-Engineer-Resume.pdf').resolve()
    response = FileResponse(open(pdf_file, 'rb'),as_attachment=True)
    return response
    