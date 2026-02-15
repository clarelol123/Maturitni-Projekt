from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'pokedungeon-super-secret-key'

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

@app.route('/ucet')
def ucet():
    return render_template('ucet.html')

@app.route('/kosik')
def kosik():
    cart=session.get('cart',[])
    return render_template('kosik.html', cart=cart)

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

# ==== CART SYSTEM ====
from flask import session, redirect, url_for

PRODUCTS={
'phantasmalflamespack':('Phantasmal Flames Booster Pack',129),
'journeytogetherpack':('Journey Together Booster Pack',109),
'megaevolutionpack':('Mega Evolution Booster Pack',129),
'destinedrivalspack':('Destined Rivals Booster Pack',169),
}

@app.route('/add_to_cart/<product_id>')
def add_to_cart(product_id):
    if product_id not in PRODUCTS:
        return redirect(url_for('shop'))
    name,price=PRODUCTS[product_id]
    cart=session.get('cart',[])
    for i in cart:
        if i['name']==name:
            i['qty']+=1
            session['cart']=cart
            return redirect(url_for('kosik'))
    cart.append({'name':name,'price':price,'qty':1})
    session['cart']=cart
    return redirect(url_for('kosik'))

@app.route('/remove/<int:index>')
def remove(index):
    cart=session.get('cart',[])
    if 0<=index<len(cart):
        cart.pop(index)
    session['cart']=cart
    return redirect(url_for('kosik'))


if __name__ == '__main__':
    app.run(debug=True)

    

