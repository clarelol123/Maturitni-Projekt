from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key='pokedungeon-secret'

PRODUCTS = {
    "destinedrivalsboosterbox": {
        "name": "Destinedrivalsboosterbox",
        "price": 8999,
        "image": "pokedungeon logo.png"
    },
    "destinedrivalsboosterbundle": {
        "name": "Destinedrivalsboosterbundle",
        "price": 2499,
        "image": "pokedungeon logo.png"
    },
    "destinedrivalsetb": {
        "name": "Destinedrivalsetb",
        "price": 3199,
        "image": "pokedungeon logo.png"
    },
    "destinedrivalspack": {
        "name": "Destinedrivalspack",
        "price": 169,
        "image": "pokedungeon logo.png"
    },
    "journeytogetherboosterbox": {
        "name": "Journeytogetherboosterbox",
        "price": 4999,
        "image": "pokedungeon logo.png"
    },
    "journeytogetherboosterbundle": {
        "name": "Journeytogetherboosterbundle",
        "price": 899,
        "image": "pokedungeon logo.png"
    },
    "journeytogetheretb": {
        "name": "Journeytogetheretb",
        "price": 1799,
        "image": "pokedungeon logo.png"
    },
    "journeytogetherpack": {
        "name": "Journeytogetherpack",
        "price": 109,
        "image": "pokedungeon logo.png"
    },
    "megaevolutionboosterbox": {
        "name": "Megaevolutionboosterbox",
        "price": 5799,
        "image": "pokedungeon logo.png"
    },
    "megaevolutionboosterbundle": {
        "name": "Megaevolutionboosterbundle",
        "price": 999,
        "image": "pokedungeon logo.png"
    },
    "megaevolutionetb": {
        "name": "Megaevolutionetb",
        "price": 1599,
        "image": "pokedungeon logo.png"
    },
    "megaevolutionpack": {
        "name": "Megaevolutionpack",
        "price": 129,
        "image": "pokedungeon logo.png"
    },
    "phantasmalflamesboosterbox": {
        "name": "Phantasmalflamesboosterbox",
        "price": 5499,
        "image": "pokedungeon logo.png"
    },
    "phantasmalflamesboosterbundle": {
        "name": "Phantasmalflamesboosterbundle",
        "price": 999,
        "image": "pokedungeon logo.png"
    },
    "phantasmalflamesetb": {
        "name": "Phantasmalflamesetb",
        "price": 1499,
        "image": "pokedungeon logo.png"
    },
    "phantasmalflamespack": {
        "name": "Phantasmalflamespack",
        "price": 129,
        "image": "pokedungeon logo.png"
    }
}

app.secret_key='pokedungeon-secret'

#ostatni

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/phantasmal')
def phantasmal():
    return render_template('phantasmalflamesetb.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/kosik')
def kosik():
    cart=session.get('cart',{})
    return render_template('kosik.html', cart=cart, products=PRODUCTS)

#phantasmal

@app.route('/phantasmalflamespack')
def phantasmalflamespack():
    return render_template('phantasmalflamespack.html')

@app.route('/phantasmalflamesboosterbundle')
def phantasmalflamesboosterbundle():
    return render_template('phantasmalflamesboosterbundle.html')

@app.route('/phantasmalflamesboosterbox')
def phantasmalflamesboosterbox():
    return render_template('phantasmalflamesboosterbox.html')

#megaevolution

@app.route('/megaevolutionpack')
def megaevolutionpack():
    return render_template('megaevolutionpack.html')

@app.route('/megaevolution')
def megaevolution():
    return render_template('megaevolutionetb.html')

@app.route('/megaevolutionboosterbundle')
def megaevolutionboosterbundle():
    return render_template('megaevolutionboosterbundle.html')

@app.route('/megaevolutionboosterbox')
def megaevolutionboosterbox():
    return render_template('megaevolutionboosterbox.html')

#destined rivals

@app.route('/destinedrivalspack')
def destinedrivalspack():
    return render_template('destinedrivalspack.html')

@app.route('/destinedrivals')
def destinedrivals():
    return render_template('destinedrivalsetb.html')

@app.route('/destinedrivalsboosterbundle')
def destinedrivalsboosterbundle():
    return render_template('destinedrivalsboosterbundle.html')

@app.route('/destinedrivalsboosterbox')
def destinedrivalsboosterbox():
    return render_template('destinedrivalsboosterbox.html')

#jt

@app.route('/journeytogetherpack')
def journeytogetherpack():
    return render_template('journeytogetherpack.html')

@app.route('/journeytogether')
def journeytogether():
    return render_template('journeytogetheretb.html')

@app.route('/journeytogetherboosterbundle')
def journeytogetherboosterbundle():
    return render_template('journeytogetherboosterbundle.html')

@app.route('/journeytogetherboosterbox')
def journeytogetherboosterbox():
    return render_template('journeytogetherboosterbox.html')



    
@app.route("/add_to_cart/<product_id>")
def add_to_cart(product_id):
    if product_id not in PRODUCTS:
        return redirect(url_for('shop'))
    cart=session.get('cart',{})
    if product_id in cart:
        cart[product_id]['qty']+=1
    else:
        p=PRODUCTS[product_id]
        cart[product_id]={'name':p['name'],'price':p['price'],'image':p['image'],'qty':1}
    session['cart']=cart
    return redirect(url_for('kosik'))

@app.route("/remove_from_cart/<product_id>")
def remove_from_cart(product_id):
    cart=session.get('cart',{})
    cart.pop(product_id,None)
    session['cart']=cart
    return redirect(url_for('kosik'))




@app.route("/plus/<product_id>")
def plus(product_id):
    cart=session.get('cart',{})
    if product_id in cart:
        cart[product_id]['qty']+=1
    session['cart']=cart
    return redirect(url_for('kosik'))

@app.route("/minus/<product_id>")
def minus(product_id):
    cart=session.get('cart',{})
    if product_id in cart:
        cart[product_id]['qty']-=1
        if cart[product_id]['qty']<=0:
            cart.pop(product_id)
    session['cart']=cart
    return redirect(url_for('kosik'))

# ===== Fake order completion =====
from flask import redirect, url_for, session
import random, string

@app.route('/konec_objednavky', methods=['POST'])
def konec_objednavky():
    if not session.get('cart'):
        return redirect(url_for('kosik'))
    order_id = 'PD-' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    session.pop('cart', None)
    return render_template('objednavkakonec.html', order_id=order_id)


if __name__ == '__main__':
    app.run(debug=True)


