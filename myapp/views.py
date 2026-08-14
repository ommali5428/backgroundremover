from django.shortcuts import render
from rembg import remove
from PIL import Image
from io import BytesIO
import base64

def index(request):
    context = {}

    if request.method == 'POST' and request.FILES.get('photo'):
        photo = request.FILES['photo']

        # Open image
        inp = Image.open(photo).convert("RGBA")

        # Remove background
        output = remove(inp)

        # Save to memory
        buffer = BytesIO()
        output.save(buffer, format="PNG")

        # Convert to base64
        img_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

        context['result'] = img_base64
        context['download'] = img_base64

    return render(request, 'index.html', context)
