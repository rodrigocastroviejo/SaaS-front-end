// Este script debe cargarse de forma SINCRÓNICA en el <head>
(function() {
    'use strict';
    
    try {
        // ===== 1. DETECCIÓN DEL TEMA INICIAL =====
        var savedTheme = null;
        
        // Intentar leer de localStorage (puede fallar en algunos contextos)
        try {
            savedTheme = localStorage.getItem('theme');
        } catch (e) {
            console.debug('localStorage no disponible en inicialización');
        }
        
        // ===== 2. APLICAR EL TEMA INMEDIATAMENTE =====
        var shouldApplyDark = false;
        
        if (savedTheme === 'dark') {
            shouldApplyDark = true;
        } else if (savedTheme === 'light') {
            shouldApplyDark = false;
        } else {
            // No hay tema guardado o es 'system', usar preferencia del sistema
            if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
                shouldApplyDark = true;
            }
        }
        
        // Aplicar la clase 'dark' al elemento html
        if (shouldApplyDark) {
            document.documentElement.classList.add('dark');
            document.documentElement.setAttribute('data-theme', 'dark');
            document.documentElement.setAttribute('data-initial-theme', 'dark');
        } else {
            document.documentElement.classList.remove('dark');
            document.documentElement.setAttribute('data-theme', 'light');
            document.documentElement.setAttribute('data-initial-theme', 'light');
        }
        
        // ===== 3. MOSTRAR LA PÁGINA =====
        // Marcar que el tema ya fue aplicado
        document.documentElement.classList.add('theme-applied');
        
        // Asegurarse de que la página se muestre después de aplicar el tema
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', function() {
                document.documentElement.style.visibility = 'visible';
                document.documentElement.style.opacity = '1';
            });
        } else {
            // DOM ya está listo
            document.documentElement.style.visibility = 'visible';
            document.documentElement.style.opacity = '1';
        }
        
        // ===== 4. DEBUG (opcional) =====
        console.debug('Tema inicializado:', shouldApplyDark ? 'dark' : 'light', 
                     '| Guardado:', savedTheme);
                     
    } catch (error) {
        console.error('Error en inicialización del tema:', error);
        // En caso de error, asegurar que la página sea visible
        document.documentElement.classList.add('theme-applied');
        document.documentElement.style.visibility = 'visible';
        document.documentElement.style.opacity = '1';
    }
})();