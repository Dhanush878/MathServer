from django.shortcuts import render
from django.http import JsonResponse

def index(request):
   
    return render(request, 'index.html')  # Ensure the HTML file is saved as 'index.html' in the templates folder.

def calculate_power(request):
    
    if request.method == 'GET':
        try:
            intensity = float(request.GET.get('intensity', 0))
            resistance = float(request.GET.get('resistance', 0))
            power = intensity ** 2 * resistance
            return JsonResponse({'power': round(power, 2)})  # Return the power value
        except (ValueError, TypeError):
            return JsonResponse({'error': 'Invalid input. Please provide valid numbers.'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)
