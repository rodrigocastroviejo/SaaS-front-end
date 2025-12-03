// theme-toggle.js - Script para funcionalidad de toggle

document.addEventListener('DOMContentLoaded', function() {
    'use strict';
    
    const themeToggleBtn = document.getElementById('theme-toggle');
    const themeIcon = document.getElementById('theme-icon');
    
    // Si no hay botón, no hacer nada
    if (!themeToggleBtn) {
        return;
    }
    
    // ===== 1. FUNCIÓN PARA ACTUALIZAR EL ÍCONO =====
    function updateIcon() {
        if (!themeIcon) {
            return;
        }
        
        const isDark = document.documentElement.classList.contains('dark');
        
        if (isDark) {
            themeIcon.classList.remove('bi-moon-stars');
            themeIcon.classList.add('bi-sun');
        } else {
            themeIcon.classList.remove('bi-sun');
            themeIcon.classList.add('bi-moon-stars');
        }
    }
    
    // ===== 2. INICIALIZAR EL ÍCONO =====
    // El tema ya fue aplicado por theme-init.js, solo actualizamos el ícono
    updateIcon();
    
    // ===== 3. MANEJAR EL TOGGLE =====
    themeToggleBtn.addEventListener('click', function() {
        // Alternar clase 'dark'
        const isDark = document.documentElement.classList.toggle('dark');
        const theme = isDark ? 'dark' : 'light';
        
        // Actualizar atributos
        document.documentElement.setAttribute('data-theme', theme);
        
        // Guardar en localStorage
        try {
            localStorage.setItem('theme', theme);
            
            // Opcional: También guardar en cookie para compatibilidad SSR
            document.cookie = `theme=${theme}; path=/; max-age=${60 * 60 * 24 * 365}; SameSite=Lax`;
        } catch (e) {
            console.warn('No se pudo guardar la preferencia del tema:', e);
        }
        
        // Actualizar el ícono
        updateIcon();
        
        // Opcional: Disparar evento personalizado para otros componentes
        window.dispatchEvent(new CustomEvent('theme-changed', { 
            detail: { theme: theme } 
        }));
    });
    
    // ===== 4. MANEJAR CAMBIOS EN LA PREFERENCIA DEL SISTEMA =====
    // Solo si el usuario no ha guardado una preferencia explícita
    if (window.matchMedia) {
        const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
        
        mediaQuery.addEventListener('change', function(e) {
            // Solo cambiar si el usuario no ha guardado una preferencia
            try {
                const savedTheme = localStorage.getItem('theme');
                if (!savedTheme || savedTheme === 'system') {
                    const newTheme = e.matches ? 'dark' : 'light';
                    document.documentElement.classList.toggle('dark', e.matches);
                    document.documentElement.setAttribute('data-theme', newTheme);
                    updateIcon();
                }
            } catch (error) {
                console.debug('No se pudo verificar localStorage en cambio de preferencia');
            }
        });
    }
    
    // ===== 5. INICIALIZAR FLOWBITE =====
    if (typeof flowbite !== 'undefined') {
        flowbite.init();
    }
});