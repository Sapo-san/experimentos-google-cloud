# Cloud Function con Trigger en Cloud Storage
## Descripción
Implementación de una cloud function que se activa con un trigger de cloud storage, es decir, cuando ocurre algun evento en cloud storage (como subir un archivo, por ejemplo) se ejecuta la cloud function.

## Variables de entorno
Para que script funcione, se necesitan las siguientes variables de entorno:
```bash
# Archivo de credenciales
SERVICE_ACCOUNT_CREDS_FILE="archivo de credenciales obtenido de GCP"

# Storage API
TARGET_BUCKET_NAME="nombre del bucket"
TARGET_FILENAME="nombre del archivo (incluye extensión)"

```

## Dependencias
Ver archivo `requeriments.txt`

## Documentación relevante
- [Implementar Cloud Function con activador en Cloud Storage](https://cloud.google.com/functions/docs/tutorials/storage-1st-gen?hl=es-419)

