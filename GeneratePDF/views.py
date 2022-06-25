from django.http import HttpResponse, FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import letter
from datetime import datetime
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
import io


def pdfEmploye(request):
    # Create the HttpResponse object
    response = HttpResponse(content_type='application/pdf')

    # This line force a download
    response['Content-Disposition'] = 'attachment; filename="1.pdf"'

    # READ Optional GET param
    get_param = request.GET.get('name', 'World')

    # Generate unique timestamp
    ts = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')

    p = canvas.Canvas(response)

    # Write content on the PDF
    p.drawString(10, 50, "hello " + get_param + " (Dynamic PDF) - " + ts);

    # Close the PDF object.
    p.showPage()
    p.save()

    # Show the result to the user
    return response


def pdfEntreprie(request):
    # Create the HttpResponse object
    response = HttpResponse(content_type='application/pdf')

    # This line force a download
    response['Content-Disposition'] = 'attachment; filename="1.pdf"'

    # READ Optional GET param
    get_param = request.GET.get('name', 'World')

    # Generate unique timestamp
    ts = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')

    p = canvas.Canvas(response)

    # Write content on the PDF
    p.drawString(100, 500, "Hello " + get_param + " (Dynamic PDF) - " + ts)

    # Close the PDF object.
    p.showPage()
    p.save()

    # Show the result to the user
    return response
