from app import app, db
from flask import render_template, request, redirect, url_for

from app.forms import BrandUpdateForm, ItemCreationForm, ItemUpdateForm, AddToCartForm
from app.models import Brand, Item, User, UsersItem

import os

def get_user():
    return User.query.first()

@app.route('/create-user')
def create_user():
    # db.session.add(User(name='Test user'))
    # db.session.commit()
    # from flask import jsonify
    # return jsonify({'ok': True})
    user = get_user()
    from flask import jsonify
    return jsonify({'id': user.id, 'name': user.name})


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/index')
@app.route('/')
def index():
    brands_list = Brand.query.all()
    items_list = Item.query.all()

    context = {
        'brands_list': brands_list,
        'items_list': items_list,
    }
    return render_template('index.html', **context)



@app.route('/brand-update/<brand_id>', methods=['GET', 'POST'])
def brand_update(brand_id):
    brand = Brand.query.get(brand_id)
    form = BrandUpdateForm(title=brand.title)
    if form.validate_on_submit():
        action = request.form.get('action', '')
        if action == 'save':
            brand.title = form.title.data
        elif action == 'del':
            db.session.delete(brand)
        db.session.commit()
        return redirect('/index')
    return render_template('brand_update.html', brand=brand, form=form)


@app.route('/item-create', methods=['GET', 'POST'])
def item_create():
    form = ItemCreationForm()
    form.brand.choices = [(brand.id, brand.title) for brand in Brand.query.all()]
    if form.validate_on_submit():
        new_item = Item()
        new_item.title = form.title.data
        new_item.price = form.price.data
        new_item.brand_id = form.brand.data
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('brand_update', brand_id=form.brand.data))
    return render_template('item_create.html', form=form)


@app.route('/item-detail/<item_id>', methods=['GET', 'POST'])
def item_detail(item_id):
    item = Item.query.get(item_id)
    form = AddToCartForm()
    if form.validate_on_submit():
        item_to_cart = UsersItem()
        item_to_cart.user = get_user()
        item_to_cart.item = item
        db.session.add(item_to_cart)
        db.session.commit()
        return redirect(url_for('cart'))
    return render_template('item_detail.html', item=item, form=form)



@app.route('/brand-create', methods=['GET', 'POST'])
def brand_create():
    form = BrandUpdateForm()
    if form.validate_on_submit():
        db.session.add(Brand(title=form.title.data))
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('brand_create.html', form=form)


@app.route('/item-update/<item_id>', methods=['GET', 'POST'])
def item_update(item_id):
    item = Item.query.get(item_id)
    form = ItemUpdateForm(title=item.title, price=item.price)
    success_url = url_for('index')
    if form.validate_on_submit():
        action = request.form.get('action', '')
        if action == 'save':
            item.title = form.title.data
            item.price = form.price.data
            file = form.logo.data
            if allowed_file(file.filename):
                logo = f'images/items/{file.filename}'
                file.save(os.path.join(app.config['STATIC_ROOT'], logo))
                item.logo = logo
            success_url = url_for('item_detail', item_id=item.id)
        elif action == 'del':
            db.session.delete(item)
        db.session.commit()
        return redirect(success_url)
    return render_template('item_update.html', item=item, form=form)


@app.route('/cart')
def cart():
    users_items = UsersItem.query.filter_by(user=get_user()).all()
    return render_template('cart.html', users_items=users_items)
