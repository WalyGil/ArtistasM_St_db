import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect('proveedores.db')
cursor = conn.cursor()

# Crear tabla de proveedores
cursor.execute('''
    CREATE TABLE IF NOT EXISTS proveedores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        tipo TEXT NOT NULL,
        estilo TEXT NOT NULL,
        precio_promedio REAL NOT NULL,
        puntuacion REAL NOT NULL,
        ubicacion TEXT NOT NULL
    )
''')

# Insertar algunos datos de prueba
proveedores_iniciales = [
    ("DJ Carlos", "DJ", "Moderno", 500, 4.5, "Madrid"),
    ("Animaciones Pedro", "Animación", "Infantil", 300, 4.8, "Barcelona"),
    ("Fotografía María", "Fotografía", "Elegante", 600, 4.6, "Madrid")
]

cursor.executemany('''
    INSERT INTO proveedores 
    (nombre, tipo, estilo, precio_promedio, puntuacion, ubicacion) 
    VALUES (?, ?, ?, ?, ?, ?)
''', proveedores_iniciales)

# Guardar cambios y cerrar conexión
conn.commit()
conn.close()