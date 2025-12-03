from flask import render_template, request, redirect, url_for, flash
from app.blueprints.dashboard import dashboard_bp
from app.utils.mock_data import generate_documents, generate_transactions
from datetime import datetime

@dashboard_bp.route('')
def index():
    documents = generate_documents(5)
    transactions = generate_transactions(8)
    return render_template('index.html', 
                         documents=documents, 
                         transactions=transactions, now=datetime.now())

@dashboard_bp.route('/generate-document', methods=['GET', 'POST'])
def generate_document():
    if request.method == 'POST':
        # Simulación de generación de documento
        flash('Documento generado exitosamente (simulación)', 'success')
        return redirect(url_for('dashboard.index'))
    return render_template('generate_document.html', now=datetime.now())