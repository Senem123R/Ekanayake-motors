from flask import Flask, render_template, jsonify, request, session, redirect, url_for
from firebase_config import db
from functools import wraps
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dev-secret-key-change-this')

# ── Admin credentials (set in .env file) ──
ADMIN_EMAIL    = os.getenv('ADMIN_EMAIL',    'admin@ekanayake.lk')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'admin123')

# ════════════════════════════════════════
#  LOGIN REQUIRED DECORATOR
# ════════════════════════════════════════
def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'admin_logged_in' not in session:
            return redirect(url_for('admin_login'))
        return f(*args, **kwargs)
    return decorated


# ════════════════════════════════════════
#  PUBLIC ROUTES
# ════════════════════════════════════════

@app.route('/')
def index():
    return render_template('index.html')


# ════════════════════════════════════════
#  PUBLIC API  (used by index.html)
# ════════════════════════════════════════

@app.route('/api/products')
def get_products():
    docs = db.collection('products').order_by('id').get()
    return jsonify([doc.to_dict() for doc in docs])


@app.route('/api/orders', methods=['POST'])
def save_order():
    data = request.json
    db.collection('orders').add({
        'name':    data.get('name', ''),
        'phone':   data.get('phone', ''),
        'part':    data.get('part', ''),
        'vehicle': data.get('vehicle', ''),
        'city':    data.get('city', ''),
        'note':    data.get('note', ''),
        'status':  'new'
    })
    return jsonify({'success': True})


# ════════════════════════════════════════
#  ADMIN AUTH ROUTES
# ════════════════════════════════════════

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    error = None
    if request.method == 'POST':
        email    = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        if email == ADMIN_EMAIL and password == ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            session['admin_email']     = email
            return redirect(url_for('admin'))
        else:
            error = 'Wrong email or password. Please try again.'
    return render_template('login.html', error=error)


@app.route('/admin/logout')
def admin_logout():
    session.clear()
    return redirect(url_for('admin_login'))


# ════════════════════════════════════════
#  ADMIN PANEL  (protected)
# ════════════════════════════════════════

@app.route('/admin')
@login_required
def admin():
    return render_template('admin.html')


# ════════════════════════════════════════
#  ADMIN API  (protected)
# ════════════════════════════════════════

@app.route('/api/admin/products')
@login_required
def admin_get_products():
    docs = db.collection('products').order_by('id').get()
    return jsonify([doc.to_dict() for doc in docs])


@app.route('/api/admin/products', methods=['POST'])
@login_required
def admin_add_product():
    data   = request.json
    docs   = db.collection('products').order_by('id', direction='DESCENDING').limit(1).get()
    last_id = docs[0].to_dict()['id'] if docs else 0
    new_id  = last_id + 1
    product = {
        'id':       new_id,
        'num':      data.get('num', ''),
        'type':     data.get('type', ''),
        'brand':    data.get('brand', ''),
        'vehicles': data.get('vehicles', ''),
        'price':    int(data.get('price', 0)),
        'mfg':      bool(data.get('mfg', False)),
        'imgUrl':   data.get('imgUrl', '')
    }
    db.collection('products').document(str(new_id)).set(product)
    return jsonify({'success': True, 'id': new_id})


@app.route('/api/admin/products/<product_id>', methods=['PUT'])
@login_required
def admin_update_product(product_id):
    data = request.json
    db.collection('products').document(product_id).update(data)
    return jsonify({'success': True})


@app.route('/api/admin/products/<product_id>', methods=['DELETE'])
@login_required
def admin_delete_product(product_id):
    db.collection('products').document(product_id).delete()
    return jsonify({'success': True})


@app.route('/api/admin/orders')
@login_required
def admin_get_orders():
    status = request.args.get('status', '')
    if status:
        docs = db.collection('orders').where('status', '==', status).get()
    else:
        docs = db.collection('orders').get()
    return jsonify([{'id': d.id, **d.to_dict()} for d in docs])


@app.route('/api/admin/orders/<order_id>', methods=['PUT'])
@login_required
def admin_update_order(order_id):
    data = request.json
    db.collection('orders').document(order_id).update(data)
    return jsonify({'success': True})


# ════════════════════════════════════════
#  RUN
# ════════════════════════════════════════
if __name__ == '__main__':
    app.run(debug=True, port=5000)