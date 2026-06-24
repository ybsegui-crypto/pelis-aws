# 🎬 Mi lista de pelis

Aplicación web para gestionar una lista de películas y series para ver.
Permite **agregar**, **listar** y **eliminar** películas, con los datos guardados
de forma persistente en la nube.

Trabajo práctico final integrador de la materia **Arquitectura de Sistemas en la Nube**.

## 🧩 Arquitectura (serverless en AWS)

- **Amazon S3** — aloja el frontend (`index.html`) como sitio web estático.
- **Amazon API Gateway** — expone la API REST (HTTP API) con CORS habilitado.
- **AWS Lambda** — función `api-pelis` en Python 3.12 con la lógica del CRUD.
- **Amazon DynamoDB** — tabla `Pelis` donde se almacenan los datos.
- **IAM Role** — otorga a la Lambda permisos para acceder a DynamoDB.

## 📂 Archivos del proyecto

- `index.html` — frontend (HTML, CSS y JavaScript).
- `lambda_function.py` — código de la función Lambda (backend).

## 🔌 Endpoints de la API

| Método | Ruta          | Acción                         |
| ------ | ------------- | ------------------------------ |
| GET    | `/pelis`      | Lista todas las películas      |
| POST   | `/pelis`      | Crea una película nueva        |
| DELETE | `/pelis/{id}` | Elimina una película por su id |

## Integrantes

- Yamila Segui
- Nancy Molina
