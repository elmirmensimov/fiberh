
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Product
from django.http import JsonResponse
from .forms import ContactForm



def contact(request):
    form = ContactForm()
    context = {
        'form': form
    }
    return render(request, "contact.html", context)

def convert_currency(request):
    if request.method == 'POST':
        amount = float(request.POST.get('amount'))

        # API'den güncel döviz kuru al
        url = 'https://api.exchangeratesapi.io/latest?base=TRY&symbols=AZN'
        response = requests.get(url)
        data = response.json()
        exchange_rate = data['rates']['AZN']

        # TL üzerine %5 ekleyerek hesapla
        new_amount = amount * 1.05

        # Kur bilgisini kullanarak TL'yi Azerbaycan manatına çevir
        converted_amount = new_amount * exchange_rate

        # Sonucu JsonResponse ile gönder
        return JsonResponse({'result': round(converted_amount, 2)})

    return render(request, 'convert.html')




def product_detail(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product_detail.html', context)



def index(request):
    return render(request, 'templates/index.html')


# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')


def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("parolunuz uyğun gəlmir!")
        else:

            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')


@login_required
def view_profile(request):
    user = request.user
    context = {'user': user}
    return render(request, 'home.html', context)