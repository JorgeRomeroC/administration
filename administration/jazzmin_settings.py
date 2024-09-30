# Configuración de Jazzmin para personalizar el panel de administración de Django
JAZZMIN_SETTINGS = {
    # Título de la ventana
    "site_title": "System School",

    # Título en la pantalla de inicio de sesión
    "site_header": "System School",

    # Marca del sitio en la esquina superior izquierda
    "site_brand": "System School",

    # Logo del sitio (asegúrate de que el logo esté en la carpeta de archivos estáticos)
    "site_logo": "img/logo_school-bg.png",

    # Logo de inicio de sesión
    "login_logo": "img/logo_school-bg.png",
    # Clases CSS aplicadas al logo de inicio de sesión
    "login_logo_classes": "img-fluid mx-auto d-block",
    # Ruta al archivo CSS personalizado
    "custom_css": "css/custom.css",

    # Clases CSS aplicadas al logo
    "site_logo_classes": "img-circle",

    # Icono del sitio (favicon)
    "site_icon": "img/logo_school-bg.png",

    # Texto de bienvenida en la pantalla de inicio de sesión
    "welcome_sign": "Bienvenido System School",

    # Copyright en el pie de página
    "copyright": "Jorge Romero C",

    "user_avatar": "photo",

    # Modelos a buscar en la barra de búsqueda
    "search_model": ["auth.User", "auth.Group"],

    # Menú superior
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Support", "url": "https://github.com/JorgeRomeroC", "new_window": True},
        {"model": "auth.User"},
    ],
    "related_modal_active": True,
}