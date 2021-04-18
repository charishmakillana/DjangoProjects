from django.shortcuts import render

# Create your views here.
from TravelApp.models import Registration


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