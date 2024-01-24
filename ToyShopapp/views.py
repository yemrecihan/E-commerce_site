from django.shortcuts import render,get_object_or_404,redirect
from .models import Toy
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required

# Create your views here.
def toy_list(request):
    toys= Toy.objects.all()
    return render(request,'ToyShopapp/toy_list.html',{'toys':toys})
def toy_detail(request,toy_id):
    toy= get_object_or_404(Toy,pk=toy_id)
    return render(request,'ToyShopapp/toy_detail.html',{'toy':toy})

@login_required(login_url="/login")
def add_to_cart(request,toy_id):
    if request.method == 'POST':
        toy = get_object_or_404(Toy, id=toy_id)

        if 'cart' not in request.session:
            request.session['cart'] = {}
        
        cart = request.session['cart']

        if toy_id in cart:
            cart[toy_id]['quantity'] += 1
            cart[toy_id]['total'] = float(cart[toy_id]['quantity']) * float(toy.price)
        else:
            cart[toy_id] = {
                
                'quantity': 1,
                'price': float(toy.price),
                'total': float(toy.price),
            }

        cart[toy_id]['name'] = toy.name    
        request.session['cart'] = cart

        messages.success(request, f"{toy.name} added to cart.")

        return HttpResponseRedirect(reverse('ToyShopapp:cart'))
    else:
        return render(request, 'registration/login.html')
    
    



def cart (request):
    if 'cart' in request.session:
        cart = request.session['cart']
        total_quantity = sum(item['quantity'] for item in cart.values())
        total_price = sum(item['total'] for item in cart.values())

        context = {
            'cart': cart,
            'total_quantity': total_quantity,
            'total_price': total_price,
        }

        return render(request, 'ToyShopapp/cart.html', context)
    else:
        # Eğer sepet boşsa, boş bir sepet sayfasını render et.
        return render(request, 'ToyShopapp/cart.html')


def checkout(request):
    return render(request, 'ToyShopapp/payment.html')

def remove_from_cart(request, toy_id):
    try:
        toy = get_object_or_404(Toy, id=toy_id)

        if 'cart' in request.session:
            cart = request.session['cart']

            if toy_id in cart:
                del cart[toy_id]
                request.session['cart'] = cart
                messages.success(request, f"{toy.name} sepetten kaldırıldı.")

        print("Remove işlemi başarılı!")

        return redirect('ToyShopapp:cart')
    except Exception as e:
        print(f"Error in remove_from_cart view: {e}")
        raise e
    


