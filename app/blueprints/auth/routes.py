from flask import render_template, redirect, url_for, request, flash
from app.blueprints.auth import auth_bp
from datetime import datetime

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Simulación de login - solo frontend
        flash('Inicio de sesión simulado correctamente', 'success')
        return redirect(url_for('dashboard.index'))
    return render_template('auth/login.html', now=datetime.now())

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Simulación de registro - solo frontend
        flash('Registro simulado correctamente', 'success')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', now=datetime.now())