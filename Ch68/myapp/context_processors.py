from datetime import date

#a context processor takes the request and returns a dictionary;
#its keys are available in EVERY template, without sending them from each view
#(it runs on every page, so keep it light)


#fixed values for the whole site
def site_info(request):
    return {
        'site_name': 'My Django Site',
        'site_email': 'info@mydjangosite.com',
        'current_year': date.today().year,
    }


#values that depend on the request: the cart is kept in the session
def cart(request):
    #session example: {'cart': {'1': 2, '5': 1}}  ->  product id: quantity
    cart = request.session.get('cart', {})
    return {
        'cart_items': sum(cart.values()),  #total quantity of all products
        'cart_products': len(cart),        #how many different products
    }


#values about who is visiting
def user_info(request):
    if request.user.is_authenticated:
        greeting = f'Hello, {request.user.username}'
    else:
        greeting = 'Hello, Guest'
    return {
        'greeting': greeting,
    }
