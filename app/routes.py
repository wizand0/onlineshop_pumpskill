from app import app, db
from flask import render_template, request, redirect

from app.forms import BrandUpdateForm
from app.models import Brand


@app.route('/index')
@app.route('/')
def index():
    brands_list = Brand.query.all()
    return render_template('index.html', brands_list=brands_list)


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