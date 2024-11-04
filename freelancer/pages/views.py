from django.shortcuts import render

# Create your views here.
def services(request):
    our_services = ["tailoring", "laundry"]
    context = {"all_services": our_services}
    return render(request, "pages/services.html", context)

def testimonials(request):
    our_testimonies = {
        "Solomon": "they have good customer services",
        "Vanilla": "they pay attention to details",
        "Gabriel": "they are so professional in all their doings"
    }
    context = {"all_testimonies": our_testimonies}
    return render(request, "pages/testimonials.html", context)

def case_studies(request):
    return render(request, "pages/case_studies.html")

def blog(request):
    return render(request, "pages/blog.html")

def pricing(request):
    our_prices = {"tailoring": "300k", "laundry": "150k"}
    context = {"prices": our_prices}
    return render(request, "pages/pricing.html", context)