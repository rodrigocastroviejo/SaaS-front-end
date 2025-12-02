// Tema toggle para Flowbite
document.addEventListener('DOMContentLoaded', function() {
    const themeToggleBtn = document.getElementById('theme-toggle');
    const themeIcon = document.getElementById('theme-icon');
    
    // Verificar tema guardado o preferencia del sistema
    const savedTheme = localStorage.getItem('theme') || 
                      (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    
    // Aplicar tema inicial
    document.documentElement.classList.toggle('dark', savedTheme === 'dark');
    updateIcon(savedTheme);
    
    // Toggle tema
    themeToggleBtn.addEventListener('click', function() {
        const isDark = document.documentElement.classList.toggle('dark');
        const theme = isDark ? 'dark' : 'light';
        
        localStorage.setItem('theme', theme);
        updateIcon(theme);
    });
    
    function updateIcon(theme) {
        if (themeIcon) {
            if (theme === 'dark') {
                themeIcon.classList.remove('bi-moon-stars');
                themeIcon.classList.add('bi-sun');
            } else {
                themeIcon.classList.remove('bi-sun');
                themeIcon.classList.add('bi-moon-stars');
            }
        }
    }
    
    // Inicializar componentes de Flowbite
    if (typeof flowbite !== 'undefined') {
        flowbite.init();
    }
});