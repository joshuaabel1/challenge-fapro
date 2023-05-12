
### UF Value API

### Levantar el proyecto:

1. Crear un entorno virtual:
   
   ```
   python3 -m venv myenv

   ```
    Para Windows:

   ```
   python -m venv myenv

   ```


2. Activar el entorno virtual
   
   Para Unix o MacOS:

    ```
   source myenv/bin/activate

   ```

   Para windows:

    ```
   .\myenv\Scripts\activate

    ```

3. Instalar las dependencias del proyecto

    ```
    pip install -r requirements.txt

    ```

4. Levantar el servidor de desarrollo de Django

    ```
    python manage.py runserver
    ```
    
    ```
    python3 manage.py runserver
    ```
#### Overview:

Este proyecto es una API que permite consultar el valor de la UF (Unidad de Fomento) para una fecha determinada. La fecha debe ser posterior al 01-01-2013 y debe estar en el formato YYYY-MM-DD.


#### Endpoint:

El endpoint para consultar el valor de la UF es:

```
/uf-value/<str:date>/

```

Aquí, <str:date> debe ser reemplazado por la fecha para la que quieres consultar el valor de la UF.

#### Uso:

Para usar el endpoint, realiza una solicitud GET a la URL. Por ejemplo:

```
GET /uf-value/2023-05-11/

```
Esto devolverá el valor de la UF para el 11 de mayo de 2023.

```
{
    "date": "2023-05-11",
    "uf_value": "35963.32"
}
```
#### Respuestas:

- 200 OK: La consulta fue exitosa y el valor de la UF para la fecha dada se incluye en el cuerpo de la respuesta. El cuerpo de la respuesta tendrá el siguiente formato:

```
{
    "date": "YYYY-MM-DD",
    "uf_value": valor
}
```
Aquí, YYYY-MM-DD es la fecha para la que se consultó y valor es el valor de la UF para esa fecha.

- 400 BAD REQUEST: Hubo un problema con la consulta. Esto puede deberse a una de las siguientes razones:

    -La fecha está en un formato incorrecto. En este caso, el cuerpo de la respuesta será:

    ```
    {
        "error": "Incorrect date format. Please use the format YYYY-MM-DD."
    }
    ```
    - La fecha es anterior al 01-01-2013. En este caso, el cuerpo de la respuesta será:

    ```
    {
    "error": "The minimum date that can be queried is 01-01-2013."
    }

    ```

    - No se pudo recuperar el valor de la UF para la fecha especificada. En este caso, el cuerpo de la respuesta será:

    ```
    {
    "error": "Failed to retrieve UF value for the specified date."
    }

    ```

#### Test:

Ejecutar las pruebas.

```
python manage.py test uf_api.tests
```
