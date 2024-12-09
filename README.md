# Ex.05 Design a Website for Server Side Processing
## Date:09/12/2024

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
calci.html
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Power Calculator</title>
</head>
<body>
    <h1>Power Calculator</h1>
    <p>Enter values to calculate the power of the filament:</p>
    
    <label for="intensity">Intensity (I) in amperes:</label>
    <input type="number" id="intensity" required>
    <br><br>
    
    <label for="resistance">Resistance (R) in ohms:</label>
    <input type="number" id="resistance" required>
    <br><br>
    
    <button onclick="calculatePower()">Calculate Power</button>
    <p id="result"></p>

    <script>
        function calculatePower() {
            const I = parseFloat(document.getElementById('intensity').value);
            const R = parseFloat(document.getElementById('resistance').value);
            
            if (!isNaN(I) && !isNaN(R)) {
                const P = I * I * R; // Formula: P = I² * R
                document.getElementById('result').textContent = `Power: ${P.toFixed(2)} watts`;
            } else {
                document.getElementById('result').textContent = "Please enter valid numbers.";
            }
        }
    </script>
</body>
</html>
```


urls.py
```

from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('', views.index, name='index'),  # Route for the homepage
    path('calculate/', views.calculate_power, name='calculate_power'),  # Route for calculating power
]
```
views.py

```
from django.http import JsonResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # Assumes an HTML file named 'index.html' in templates folder

def calculate_power(request):
    if request.method == 'GET':
        intensity = request.GET.get('intensity')
        resistance = request.GET.get('resistance')

        try:
            I = float(intensity)
            R = float(resistance)
            power = I ** 2 * R
            return JsonResponse({'power': round(power, 2)})
        except (ValueError, TypeError):
            return JsonResponse({'error': 'Invalid input'}, status=400)


```


## SERVER SIDE PROCESSING:
![alt text](<Screenshot 2024-12-09 105958.png>)
## HOMEPAGE:
![alt text](<Screenshot 2024-12-09 101243.png>)
## RESULT:
The program for performing server side processing is completed successfully.
