from flask import Blueprint,  render_template, request, redirect, url_for, flash
from flask_login import  login_required,  current_user
from .models import Manage
from .  import db
dashboard = Blueprint('dashboard',__name__)

@dashboard.route('/dashboard',  methods =['GET', 'POST'] )
@login_required
def home():
    manages = Manage.query.filter_by(user_id=current_user.id).all()
    if request.method == 'POST':
        title = request.form['title']
        incoming_stock = request.form['incoming_stock']
        outgoing_stock = request.form['outgoing_stock']
        if incoming_stock <= outgoing_stock:
            flash("Incoming stock must be greater than outgoing stock.", category='errors')
        else:
            total_stock = int(incoming_stock) - int(outgoing_stock)
            new_manage = Manage(title=title, incoming_stock=incoming_stock, outgoing_stock=outgoing_stock, total_stock=total_stock, user_id=current_user.id)
            db.session.add(new_manage)
            flash("Item Added successfully.", category='success')
            db.session.commit()
    return render_template("dashboard.html", user=current_user, manages=manages)


@dashboard.route('/edit_manage/<int:manage_id>', methods=['GET', 'POST'])
@login_required
def edit_manage(manage_id):
    manage = Manage.query.get_or_404(manage_id)
    if request.method == 'POST':
        incoming_stock = request.form['incoming_stock']
        outgoing_stock = request.form['outgoing_stock']
        if incoming_stock <= outgoing_stock:
            flash("Incoming stock must be greater than outgoing stock.", category='errors')
        else:
            manage.title = request.form['title']
            manage.incoming_stock = incoming_stock
            manage.outgoing_stock = outgoing_stock
            manage.total_stock = int(incoming_stock) - int(outgoing_stock)
            db.session.commit()
            flash("Changes saved successfully.", category='success')
            return redirect(url_for('dashboard.home'))
    return render_template('edit_manage.html', manage=manage)




@dashboard.route('/delete_manage/<int:manage_id>', methods=['POST'])
def delete_manage(manage_id):
    manage = Manage.query.get_or_404(manage_id)
    db.session.delete(manage)
    flash("Item deleted successfully.", category='success')
    db.session.commit()
    return redirect(url_for('dashboard.home', user= current_user))




   

