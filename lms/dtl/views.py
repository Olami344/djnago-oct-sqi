from django.shortcuts import render

# Create your views here.
def example_dtl(request):
   
    return render(request, "dtl/dtl.html")

def test_dtl(request):
    context = {
        "food": "rice",
        "ingredients": ["tomatoes", "salt", "pepper", "onions", "groundnut oil"],
        "is_favorite": True,
        "time_in_minutes": "30mins"
    }
    return render(request,"dtl/test-dtl.html", context)