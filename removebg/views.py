# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status
# from PIL import Image
# from rembg import remove
# import io
# from django.core.files.uploadedfile import InMemoryUploadedFile
# from django.http import HttpResponse  # Import HttpResponse

# @api_view(['POST'])
# def remove_background(request):
#     if 'image' not in request.FILES:
#         return Response({"error": "No image provided"}, status=status.HTTP_400_BAD_REQUEST)
    
#     uploaded_image = request.FILES['image']
    
#     # Process the image using rembg
#     img = Image.open(uploaded_image)
#     img_byte_arr = io.BytesIO()
#     img.save(img_byte_arr, format='PNG')

#     result = remove(img_byte_arr.getvalue())
    
#     img_result = Image.open(io.BytesIO(result))
    
#     # Convert the processed image back to bytes
#     img_io = io.BytesIO()
#     img_result.save(img_io, format='PNG')
#     img_io.seek(0)

#     # Send the image back in the response
#     response = HttpResponse(img_io, content_type='image/png')
#     response['Content-Disposition'] = 'attachment; filename="image_without_bg.png"'
    
#     return response

# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status
# from PIL import Image
# from rembg import remove, new_session
# import io
# from django.http import HttpResponse

# # Create a session with the U2Net model
# session = new_session("u2net")

# @api_view(['POST'])
# def remove_background(request):
#     if 'image' not in request.FILES:
#         return Response({"error": "No image provided"}, status=status.HTTP_400_BAD_REQUEST)
    
#     uploaded_image = request.FILES['image']
    
#     # Open the uploaded image
#     img = Image.open(uploaded_image)
    
#     # Resize the image for performance optimization
#     max_size = (800, 800)
#     img.thumbnail(max_size, Image.Resampling.LANCZOS)  # Use Image.Resampling.LANCZOS instead of ANTIALIAS
    
#     # Convert the image to bytes and process it
#     img_byte_arr = io.BytesIO()
#     img.save(img_byte_arr, format='PNG')
    
#     # Remove background using the selected session
#     result = remove(img_byte_arr.getvalue(), session=session)
    
#     # Convert the result back to an image
#     img_result = Image.open(io.BytesIO(result))
    
#     # Prepare the image for response
#     img_io = io.BytesIO()
#     img_result.save(img_io, format='PNG')
#     img_io.seek(0)
    
#     # Return the processed image as an HTTP response
#     response = HttpResponse(img_io, content_type='image/png')
#     response['Content-Disposition'] = 'attachment; filename="image_without_bg.png"'
    
#     return response


# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status
# from PIL import Image
# from rembg import remove, new_session
# import io
# from django.http import HttpResponse
# import os

# # Create a session with the U2Net model, you can try different models for accuracy vs speed trade-off
# session = new_session("u2net")  # You can also use "u2net_human_seg" if you are working with human images.

# @api_view(['POST'])
# def remove_background(request):
#     if 'image' not in request.FILES:
#         return Response({"error": "No image provided"}, status=status.HTTP_400_BAD_REQUEST)
    
#     uploaded_image = request.FILES['image']
    
#     # Open the uploaded image and determine its format
#     img = Image.open(uploaded_image)
#     img_format = img.format
    
#     # Resize large images for performance optimization while keeping aspect ratio
#     max_dimension = max(img.size)
#     if max_dimension > 1200:  # Only resize if larger than 1200px
#         resize_factor = 1200 / max_dimension
#         new_size = (int(img.width * resize_factor), int(img.height * resize_factor))
#         img = img.resize(new_size, Image.Resampling.LANCZOS)
    
#     # Convert the image to bytes and process with rembg
#     img_byte_arr = io.BytesIO()
#     img.save(img_byte_arr, format=img_format)
    
#     # Remove background using the rembg model session
#     result = remove(img_byte_arr.getvalue(), session=session)
    
#     # Convert the result back to an image, keeping transparency
#     img_result = Image.open(io.BytesIO(result))

#     # Convert the processed image to bytes and prepare the response
#     img_io = io.BytesIO()
    
#     # Ensure we save it in a format that supports transparency like PNG
#     img_result.save(img_io, format='PNG')
#     img_io.seek(0)
    
#     # Send the processed image back as a response
#     response = HttpResponse(img_io, content_type='image/png')
#     response['Content-Disposition'] = 'attachment; filename="image_without_bg.png"'
    
#     return response


# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status
# from PIL import Image, ImageFilter, ImageEnhance
# from rembg import remove, new_session
# import io
# from django.http import HttpResponse
# import os

# # Create a session with the U2Net model, you can try different models for accuracy vs speed trade-off
# session = new_session("u2net")  # You can also use "u2net_human_seg" if you are working with human images.

# @api_view(['POST'])
# def remove_background(request):
#     if 'image' not in request.FILES:
#         return Response({"error": "No image provided"}, status=status.HTTP_400_BAD_REQUEST)
    
#     uploaded_image = request.FILES['image']
    
#     # Open the uploaded image and determine its format
#     img = Image.open(uploaded_image)
#     img_format = img.format
    
#     # Resize large images for performance optimization while keeping aspect ratio
#     max_dimension = max(img.size)
#     if max_dimension > 1200:  # Only resize if larger than 1200px
#         resize_factor = 1200 / max_dimension
#         new_size = (int(img.width * resize_factor), (int(img.height * resize_factor)))
#         img = img.resize(new_size, Image.Resampling.LANCZOS)
    
#     # Convert the image to bytes and process with rembg
#     img_byte_arr = io.BytesIO()
#     img.save(img_byte_arr, format=img_format)
    
#     # Remove background using the rembg model session
#     result = remove(img_byte_arr.getvalue(), session=session)
    
#     # Convert the result back to an image, keeping transparency
#     img_result = Image.open(io.BytesIO(result))

#     # Apply Image Enhancements for better quality

#     # Sharpen the image
#     img_result = img_result.filter(ImageFilter.SHARPEN)

#     # Enhance the contrast and brightness (adjust factors as needed)
#     enhancer = ImageEnhance.Contrast(img_result)
#     img_result = enhancer.enhance(1.3)  # Increase contrast (factor > 1 increases contrast)

#     enhancer = ImageEnhance.Brightness(img_result)
#     img_result = enhancer.enhance(1.1)  # Increase brightness slightly
    
#     # Optional: Further enhance colors, saturation, or apply denoising techniques here

#     # Convert the processed image to bytes and prepare the response
#     img_io = io.BytesIO()
    
#     # Ensure we save it in a format that supports transparency like PNG
#     img_result.save(img_io, format='PNG')
#     img_io.seek(0)
    
#     # Send the processed image back as a response
#     response = HttpResponse(img_io, content_type='image/png')
#     response['Content-Disposition'] = 'attachment; filename="image_without_bg.png"'
    
#     return response

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from PIL import Image, ImageFilter, ImageEnhance
from rembg import remove, new_session
import io
from django.http import HttpResponse

# Create a session with the U2Net model, you can try different models for accuracy vs speed trade-off
session = new_session("u2net")  # You can also use "u2net_human_seg" if you are working with human images.

@api_view(['POST'])
def remove_background(request):
    if 'image' not in request.FILES:
        return Response({"error": "No image provided"}, status=status.HTTP_400_BAD_REQUEST)
    
    uploaded_image = request.FILES['image']
    
    # Open the uploaded image and determine its format
    img = Image.open(uploaded_image)
    img_format = img.format
    
    # Resize large images moderately for performance, but not overly aggressive to avoid blur
    max_dimension = max(img.size)
    if max_dimension > 1500:  # Resize only if larger than 1500px
        resize_factor = 1500 / max_dimension
        new_size = (int(img.width * resize_factor), int(img.height * resize_factor))
        img = img.resize(new_size, Image.Resampling.LANCZOS)
    
    # Convert the image to bytes and process with rembg
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format=img_format)
    
    # Remove background using the rembg model session
    result = remove(img_byte_arr.getvalue(), session=session)
    
    # Convert the result back to an image, keeping transparency
    img_result = Image.open(io.BytesIO(result))

    # Apply Image Enhancements to improve quality, but without making it blurry

    # Apply light sharpening to enhance edges without overdoing it
    img_result = img_result.filter(ImageFilter.UnsharpMask(radius=1, percent=125, threshold=3))

    # Enhance contrast slightly to avoid over-processing
    enhancer = ImageEnhance.Contrast(img_result)
    img_result = enhancer.enhance(1.2)  # Adjust contrast, but keep it moderate

    # Enhance brightness slightly, but don't over-brighten
    enhancer = ImageEnhance.Brightness(img_result)
    img_result = enhancer.enhance(1.05)  # Small brightness boost to maintain natural look

    # Optionally enhance color saturation slightly to make the image more vivid
    enhancer = ImageEnhance.Color(img_result)
    img_result = enhancer.enhance(1.1)  # Small color boost for natural tones
    
    # Convert the processed image to bytes and prepare the response
    img_io = io.BytesIO()
    
    # Ensure we save it in a format that supports transparency like PNG
    img_result.save(img_io, format='PNG')
    img_io.seek(0)
    
    # Send the processed image back as a response
    response = HttpResponse(img_io, content_type='image/png')
    response['Content-Disposition'] = 'attachment; filename="image_without_bg.png"'
    
    return response
