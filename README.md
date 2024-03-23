# Stock Management
Aplicación en Django para gestionar un inventario de productos con fecha de caducidad.



## Requisitos

- Python (3.12.1)
- Django (5.0.2)


Para implementación de cronjob debemos instalar Erlang y RabbitMQ (En este orden)

https://www.erlang.org/downloads


https://www.rabbitmq.com/docs/install-windows#installer

## Configuración

1. Clona este repositorio en tu máquina local:

    ```
    https://github.com/Spoilt83/stock_management.git
    ```

2. Navega al directorio de tu proyecto:

    ```
    cd tu_aplicacion_django
    ```

3. Crea y activa un entorno virtual (opcional pero recomendado):

    ```
    python -m venv env
    source env/bin/activate   # Linux/Mac
    env\Scripts\activate      # Windows
    ```

4. Instala las dependencias del proyecto:

    ```
    pip install -r requirements.txt
    ```

5. Realiza las migraciones de la base de datos:

    ```
    python manage.py migrate
    ```

6. Ejecuta el servidor de desarrollo:

    ```
    python manage.py runserver
    ```

7. Abre tu navegador web y ve a http://localhost:8000/products/login para interactuar con la aplicación.

    username: admin

    password: admin


8. (opcional) Abre tu navegador web y ve a http://localhost:8000/admin.   
     - Se solicitara username y password: (introduce admin para ambos campos)
     - Puedes agregar, consultar, actualizar y eliminar desde aquí.
    


## Estructura del Proyecto

- El proyecto se encuntra conformado por 1 modelo para representar los datos de productos. 

- Se configuro un serializer con 2 campos adicionales para contar los días de expiración y manejar la alertas. 

- Támbien se crearon templates para representar los datos del modelo al usuario.

- Mediante el manejo de views se implementa la logica para hacer uso de los datos y poder manipularlos y representarlos.

- En las vistas se encuentran implementadas funciones para: 

        - listar los diferentes productos
        - listar los productos por un rango de fecha
        - crear un producto
        - actualizar un producto
        - borrar un producto
- Las distintas rutas implementadas fueron configurdas mediante el archivo urls.py

- cronjob que se ejecuta a la media noche de cada dia para enviar notificaciones de alertas por correo de los productos cerca de caducar. En la linea de comandos correr la siguiente línea para iniciar el programa Celery en modo de planificación.

        celery -A stock_management_project beat -l info

- En el archivo task de la carpeta stock, se encuentran los comentario

    - Correo desde donde se envia la alerta
    - Correo al que se envia la alerta

Agregar estos correos para enviar y recibir notificaiones.

- Se crearon unos test para probar funcionalidades del modelo. Para probarlo:

    En la linea de comandos correr la siguiente linea:

      py manage.py test  
    



