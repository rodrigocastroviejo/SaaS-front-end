from datetime import datetime, timedelta
import random

def generate_documents(count=5):
    documents = []
    statuses = ['completado', 'procesando', 'pendiente']
    types = ['contrato', 'factura', 'reporte', 'propuesta']
    
    for i in range(count):
        doc_type = random.choice(types)
        status = random.choice(statuses)
        date = datetime.now() - timedelta(days=random.randint(0, 30))
        
        documents.append({
            'id': i + 1,
            'nombre': f'{doc_type.capitalize()}_{random.randint(1000, 9999)}.pdf',
            'tipo': doc_type,
            'fecha': date.strftime('%Y-%m-%d'),
            'estado': status,
            'icono': 'file-earmark-text' if doc_type == 'reporte' else 'file-earmark'
        })
    
    return documents

def generate_transactions(count=8):
    transactions = []
    types = ['recarga', 'gasto', 'comisión']
    descriptions = {
        'recarga': ['Recarga de saldo', 'Depósito bancario', 'Transferencia recibida'],
        'gasto': ['Generación de documento', 'Plan premium', 'Servicio adicional'],
        'comisión': ['Comisión por transacción', 'Tarifa de servicio']
    }
    
    for i in range(count):
        trans_type = random.choice(types)
        amount = round(random.uniform(10, 500), 2)
        if trans_type != 'recarga':
            amount = -abs(amount)
        
        transactions.append({
            'id': i + 1,
            'descripcion': random.choice(descriptions[trans_type]),
            'fecha': (datetime.now() - timedelta(days=random.randint(0, 60))).strftime('%Y-%m-%d %H:%M'),
            'monto': amount,
            'tipo': trans_type,
            'estado': 'completado' if random.random() > 0.2 else 'pendiente'
        })
    
    # Ordenar por fecha (más reciente primero)
    transactions.sort(key=lambda x: x['fecha'], reverse=True)
    return transactions