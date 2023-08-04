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

## Credenciales
De correr aplicación en local, el archivo de credenciales se obtiene desde GCP, autorizando a una cuenta de servicio en la _Pantalla de consentimiento de OAuth_ o usando una cuenta de usuario que tenga los permisos necesarios. 

## Dependencias
Ver archivo `requeriments.txt`

## Documentación relevante
- [Implementar Cloud Function con activador en Cloud Storage](https://cloud.google.com/functions/docs/tutorials/storage-1st-gen?hl=es-419)

- [Permisos de OAuth 2.0 para las API de Google](https://developers.google.com/identity/protocols/oauth2/scopes?hl=es-419)

- [Cuentas de servicio](https://cloud.google.com/compute/docs/access/service-accounts?hl=es-419)
