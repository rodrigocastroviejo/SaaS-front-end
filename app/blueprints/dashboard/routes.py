from flask import render_template, request, redirect, url_for, flash
from app.blueprints.dashboard import dashboard_bp
from app.utils.mock_data import generate_documents, generate_transactions

@dashboard_bp.route('/')
@dashboard_bp.route('/dashboard')
def index():
    documents = generate_documents(5)
    transactions = generate_transactions(8)
    return render_template('dashboard/index.html', 
                         documents=documents, 
                         transactions=transactions)

@dashboard_bp.route('/generate-document', methods=['GET', 'POST'])
def generate_document():
    if request.method == 'POST':
        # Simulación de generación de documento
        flash('Documento generado exitosamente (simulación)', 'success')
        return redirect(url_for('dashboard.index'))
    return render_template('dashboard/generate_document.html')