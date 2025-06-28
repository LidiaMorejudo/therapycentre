from django.shortcuts import render

def inquiries_view(request):
    return render(request, 'inquiries/enquiries.html')

