Consideraciones previas:

La base de datos ya tiene algunos datos cargados en sus tablas para comprobar las funciones.

Hay un usuario de los ya creados que es el Manager, este tiene privilegios especiales y no debe borrarse.
admin: admin@electrolaucha.com
Password: alfabeta5

Email manager: manager@electrolaucha.com
Password: Betagamma8

Por el momento, los ingresos a usuario, contraseña y los formularios deben respetar mayúsculas y minúsculas.

Se incluye archivo requirements.txt.

Home: es la vista principal, donde se presenta el negocio y hay links hacia las demás funciones:
Puede navegar por la misma para ver su estética, y hacer click en alguna de las imágenes de Productos.
Los link a las funciones principales están en la solapa superior.

Registro: Al hacer click en regístrese en la página anterior, nos llevará al formulario de registro.
Puede ingresar un usuario desde aquí, con la condición de que el email no sea el de otro usuario, en ese caso arrojará el error “inténtelo nuevamente en unos minutos”.  Todos los campos son requeridos. Para el caso que nos compete, sírvase verificar los mails de los usuarios en la base de datos.

Login: Se implementa un login muy rudimentario, accediendo desde la página principal.
Si me logueo con un usuario cualquiera: se muestra página EN CONSTRUCCIÓN.
Si me logueo como el manager: Accedo a las funciones solo para él.

Ver todas las compras: Veo las compras en mi BD (acá se ve el funcionamiento de una clase)

Ver todos los usuarios: Veo los usuarios en mi BD (acá se ve el funcionamiento de una clase)

Ver productos a la venta: Veo los productos a la venta, que están en mi BD (acá se ve el funcionamiento de una clase).

Ingresar productos a la venta: Me permite ingresar productos al listado anterior:
El modelo, similar al mail en los usuarios, debe ser único, de no hacerlo me dará el mensaje “Intentelo nuevamente en unos minutos”. Si repito Ver productos a la venta, veo que está el nuevo producto.

Ver modelos de un producto disponibles: Me permite ver todos los modelos disponibles de un producto en cuestión. 
Con esto cumplo con la búsqueda en la BD.

Ingreso de compras: puedo ingresar compras a un usuario en particular, inclusive el manager.
Si repito ver todas las compras luego de ingresar una nueva:
Vemos que esta la nueva compra ingresada.
Para finalizar, ingresaremos al panel de administrador. Aquí podemos ver y crear registros en la BD, entre otras cosas.




