import psycopg2
def autenticar_usuario(username, password,ip):
    try:
        # Te conectas directamente con las credenciales del rol
        conn = psycopg2.connect(
            host=ip,
            user=username,
            password=password,
            database="Tienda"
        )
        
        # Una vez conectado, puedes verificar el rol (por si quieres usarlo lógicamente)
        cursor = conn.cursor()
        # 2. Obtener el nombre del rol activo (ej: 'admin')
        cursor.execute("SELECT CURRENT_USER;")
        rol_nombre = cursor.fetchone()[0]
        print("🔐 Usuario logueado (rol PostgreSQL):", rol_nombre)

        # 3. Buscar el rol_id en la tabla roles
        cursor.execute("SELECT rol_id FROM roles WHERE nombre_rol = %s;", (rol_nombre,))
        print("🔍 Buscando rol_id en la tabla 'roles' para el rol:", rol_nombre)
        resultado = cursor.fetchone()
        print("🔍 Resultado de la búsqueda:", resultado)
        if not resultado:
            print("❌ El rol no existe en la tabla 'roles'")
            conn.close()
            return None
        
        rol_id = resultado[0]
        print("🔑 ID del rol:", rol_id)
        # 4. Obtener los permisos asociados a ese rol
        cursor.execute("""
            SELECT p.nombre_permiso
            FROM roles_permisos rp
            JOIN permisos p ON rp.permiso_id = p.permiso_id
            WHERE rp.rol_id = %s;
        """, (rol_id,))
        print("🔍 Buscando permisos asociados al rol_id:", rol_id)
        permisos = [fila[0] for fila in cursor.fetchall()]
        print("📜 Permisos del rol:", permisos)

        return {
            "conn": conn,
            "rol": rol_nombre,
            "rol_id": rol_id,
            "permisos": permisos
        }

    except psycopg2.Error as e:
        print("🚨 Error al conectar:", e)
        return None
    

def mostrar_tablas_disponibles(permisos):
    tablas = {
        'productos:leer': 'Productos',
        'pedidos:leer': 'Pedidos',
        'clientes:leer': 'Clientes'
    }
    
    disponibles = []
    for permiso, tabla in tablas.items():
        if permiso in permisos:
            disponibles.append(tabla)
    
    print("\nTablas disponibles:")
    for i, tabla in enumerate(disponibles, 1):
        print(f"{i}. {tabla}")
    
    return disponibles

    