from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from TravelApp.models import Registration
from .forms import PhoneNumberForm


def destination(request):
    return render(request,'index.html')
def registrationpage(request):
    try:
        # a = request.GET['firstname']
        # b = request.GET['lastname']
        # Registration.objects.create(
        #     firstname=a,
        #     lastname=b
        # )
        # result = a+b
        #
        # l =  Registration.objects.all()
        # store = []
        # for i in l:
        #     store.append([i.firstname, i.lastname])

        first_name = request.GET['firstname']
        last_name = request.GET['lastname']
        email = request.GET['email']
        phone_number = request.GET['phonenumber']
        name= first_name+' '+last_name
        Registration.objects.create(firstname=first_name,lastname=last_name,phonenumber=phone_number)
        details = Registration.objects.all()
        store = []
        for i in details:
            store.append([i.firstname,i.lastname,i.phonenumber])
        return render(request,'result.html',{'store_data':'store'})
    except:
        return render(request, 'index.html')


class PhoneNumberView(View):

    def get(self, request):
        form = PhoneNumberForm()
        return render(
            request, 'index.html', {
                'form': form
            }
        )

    def post(self, request):
        form = PhoneNumberForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            # need to take the decision wether we have to show the existing details else we need to save it into DB

            return HttpResponse('Yes')
        return render(
            request, 'index.html', {
                'form': form
            }
        )

# or can be written as a class


def phone_number_view(request):
    if request.method == 'GET':
        form = PhoneNumberForm()

    if request.method == 'POST':
        form = PhoneNumberForm(request.POST)
        # import pdb
        # pdb.set_trace()
        # check whether it's valid:
        print(form.errors)
        if form.is_valid():
            return HttpResponse('Yes')
    import ipdb
    ipdb.set_trace()

    return render(
        request, 'index.html', {
            'form': form
        }
    )
