from django.shortcuts import render, redirect
from .forms import EnquiryForm  # import the form

def inquiries_view(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/enquiries/?success=true')  # optional confirmation modal
    else:
        form = EnquiryForm()

    return render(request, 'inquiries/enquiries.html', 
                  {
                      'enquiry_form': form
                      },
    )

