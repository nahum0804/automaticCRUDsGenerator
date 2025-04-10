-- Categorías de productos
CREATE TABLE categorias (
    categoria_id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    descripcion TEXT
);

-- Proveedores
CREATE TABLE proveedores (
    proveedor_id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    contacto VARCHAR(100)
);

-- Productos (relacionados con categorías y proveedores)
CREATE TABLE productos (
    producto_id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL DEFAULT 0,
    categoria_id INT,
    proveedor_id INT,
    FOREIGN KEY (categoria_id) REFERENCES categorias(categoria_id),
    FOREIGN KEY (proveedor_id) REFERENCES proveedores(proveedor_id)
);

-- Clientes
CREATE TABLE clientes (
    cliente_id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

-- Pedidos
-- 1. Crear el tipo ENUM
CREATE TYPE estado_pedido AS ENUM ('pendiente', 'completado', 'cancelado');

-- 2. Crear la tabla usando el ENUM
CREATE TABLE pedidos (
    pedido_id SERIAL PRIMARY KEY,
    cliente_id INT,
    fecha_pedido TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    estado estado_pedido DEFAULT 'pendiente',
    FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id)
);
select Tienda from Schema

-- Roles de usuarios
CREATE TABLE roles (
    rol_id SERIAL PRIMARY KEY,
    nombre_rol VARCHAR(50) NOT NULL UNIQUE -- Ej: 'admin', 'inventario', 'vendedor'
);

-- Permisos específicos por recurso
CREATE TABLE permisos (
    permiso_id SERIAL PRIMARY KEY,
    nombre_permiso VARCHAR(50) NOT NULL UNIQUE, -- Ej: 'productos:leer', 'pedidos:escribir'
    descripcion TEXT
);

-- Asignación de permisos a roles
CREATE TABLE roles_permisos (
    rol_id SERIAL,
    permiso_id INT,
    PRIMARY KEY (rol_id, permiso_id),
    FOREIGN KEY (rol_id) REFERENCES roles(rol_id),
    FOREIGN KEY (permiso_id) REFERENCES permisos(permiso_id)
);
--drop table usuarios


-- Permisos para productos
INSERT INTO permisos (nombre_permiso, descripcion) VALUES
    ('productos:leer', 'Ver listado de productos'),
    ('productos:escribir', 'Crear nuevos productos'),
    ('productos:actualizar', 'Modificar productos existentes'),
    ('productos:eliminar', 'Eliminar productos');

-- Permisos para pedidos
INSERT INTO permisos (nombre_permiso, descripcion) VALUES
    ('pedidos:leer', 'Ver pedidos'),
    ('pedidos:escribir', 'Crear pedidos'),
    ('pedidos:actualizar', 'Cambiar estado de pedidos');

-- Permisos para clientes
INSERT INTO permisos (nombre_permiso, descripcion) VALUES
    ('clientes:leer', 'Ver información de clientes'),
    ('clientes:actualizar', 'Editar datos de clientes');
SELECT FROM roles
-- Rol: Administrador (todos los permisos)
INSERT INTO roles_permisos (rol_id, permiso_id)
SELECT 1, permiso_id FROM permisos; -- Asume que rol_id 1 es 'admin'

-- Rol: Vendedor (solo pedidos y lectura de productos)
INSERT INTO roles_permisos (rol_id, permiso_id)
VALUES
    (2, (SELECT permiso_id FROM permisos WHERE nombre_permiso = 'productos:leer')),
    (2, (SELECT permiso_id FROM permisos WHERE nombre_permiso = 'pedidos:leer')),
    (2, (SELECT permiso_id FROM permisos WHERE nombre_permiso = 'pedidos:escribir'));

-- Agregar datos
INSERT INTO categorias (nombre, descripcion) VALUES
    ('Electrónicos', 'Dispositivos electrónicos y gadgets'),
    ('Ropa', 'Prendas de vestir para todas las edades'),
    ('Hogar', 'Artículos para el hogar y decoración');

INSERT INTO proveedores (nombre, contacto) VALUES
    ('TechGlobal', 'contacto@techglobal.com'),
    ('ModaTotal', 'info@modatotal.com'),
    ('HogarPlus', 'soporte@hogarplus.com');

INSERT INTO productos (nombre, precio, stock, categoria_id, proveedor_id) VALUES
    ('Smartphone X', 599.99, 50, 1, 1),   -- Electrónicos / TechGlobal
    ('Laptop Pro', 1299.99, 30, 1, 1),
    ('Camisa Casual', 29.99, 200, 2, 2),   -- Ropa / ModaTotal
    ('Jarrón Decorativo', 49.99, 80, 3, 3); -- Hogar / HogarPlus

INSERT INTO clientes (nombre, email) VALUES
    ('Ana López', 'ana.lopez@email.com'),
    ('Carlos Ruiz', 'carlos.ruiz@email.com'),
    ('Marta Díaz', 'marta.diaz@email.com');
-- Insert pedidos
INSERT INTO pedidos (cliente_id, estado) VALUES
    (1, 'completado'),  -- Pedido de Ana López
    (2, 'pendiente'),   -- Pedido de Carlos Ruiz
    (3, 'cancelado');   -- Pedido de Marta Díaz
--insert roles
INSERT INTO roles (nombre_rol) VALUES
    ('admin'),
    ('manager'),
    ('empleado'),
    ('cliente');

--manager
INSERT INTO roles_permisos (rol_id, permiso_id) VALUES
    (2, 1), -- productos:leer
    (2, 2), -- productos:escribir
    (2, 3), -- productos:actualizar
    (2, 5), -- pedidos:leer
    (2, 7); -- pedidos:actualizar

--Empleado
INSERT INTO roles_permisos (rol_id, permiso_id) VALUES
    (3, 1), -- productos:leer
    (3, 5); -- pedidos:leer

--Cliente
INSERT INTO roles_permisos (rol_id, permiso_id) VALUES
    (4, 1); -- productos:leer

--Insertar usuarios

-- Rol admin: acceso total
CREATE ROLE admin WITH LOGIN PASSWORD 'password_admin' SUPERUSER;

-- Rol manager: permisos específicos
CREATE ROLE manager WITH LOGIN PASSWORD 'password_manager';

-- Rol empleado: solo lectura
CREATE ROLE empleado WITH LOGIN PASSWORD 'password_empleado';

-- Rol cliente: acceso limitado
CREATE ROLE cliente WITH LOGIN PASSWORD 'password_cliente';
--datos ejemplo de auditoria
--INSERT INTO auditoria (usuario_id, accion, tabla_afectada, registro_id) VALUES
--    (1, 'DELETE', 'productos', 3), -- admin_juan eliminó un producto
--    (2, 'UPDATE', 'pedidos', 2);   -- manager_ana actualizó un pedido
GRANT SELECT ON roles TO PUBLIC;
GRANT SELECT ON permisos TO PUBLIC;
GRANT SELECT ON roles_permisos TO PUBLIC;
--admin_juan puede hacer cualquier acción (CRUD completo).

--manager_ana puede agregar/editar productos y actualizar pedidos, pero no eliminarlos.

--empleado_pedro solo puede ver productos y pedidos.

--cliente_maria solo ve productos (ni siquiera pedidos).