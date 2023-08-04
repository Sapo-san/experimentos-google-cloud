
# Imports Google
from google.cloud import storage

# Otros imports
from os import getenv, path
from dotenv import load_dotenv

load_dotenv() # Cargar variables de entorno desde .env

### Constantes -------------------------------------
SCOPES = [ 
    # SCOPES: OAuth2.0 URIs que contienen el nombre de la app de google
    # a utilizar e indican que tipo de data accede y el nival de acceso
    'https://www.googleapis.com/auth/devstorage.read_only',
]

# Nombre del archivo de credenciales (debe estar en mismo directorio
# que cloud function)
SERVICE_ACCOUNT_CREDS_FILE = getenv('SERVICE_ACCOUNT_CREDS_FILE')

# Nombre del bucket
TARGET_BUCKET_NAME=getenv('TARGET_BUCKET_NAME')

# Nombre del archivo a obtener del bucket
TARGET_FILENAME=getenv('TARGET_FILENAME')

### ---------------------------------------------------------------------------
def main(event, context):
    
    ## Verificamos si evento es el correcto -----------------------------------
    message = None
    if context.event_type != "google.storage.object.finalize":
        message = "Evento no es subida de archivo finalizada. Fin de ejecución"
        print(message)
        return
    
    if event["bucket"] != TARGET_BUCKET_NAME:
        message = "No es bucket objetivo. Fin de ejecución"
        print(message)
        return

    if event["name"] != TARGET_FILENAME:
        message = "Archivo modificado no es archivo objetivo. Fin de ejecución"
        print(message)
        return
    
    ## ------------------------------------------------------------------------
        
    # Creamos cliente de api de storage autenticado
    storage_client = None
    '''
    - Si se corre en local, recordar usar .env y json con credenciales
    
    - Si se corre en ambiente GCP, agregar variables de entorno por
    consola o UI a la funcion, json con credenciales no es necesario
    por que el cliente las obtendria del entorno
    '''
    if path.isfile(".env"):
        # con credenciales de la cuenta de servicio (archivo .json indicado en .env)
        storage_client = storage.Client.from_service_account_json(
            SERVICE_ACCOUNT_CREDS_FILE
            )
    else:
        # Con credenciales obtenidas del entorno de GCP
        storage_client = storage.Client()
    
    ## ------------------------------------------------------------------------
    
    '''
        Descarga y retorna los bytes un archivo *source_blob_name* ubicado en
        cloud bucket *bucket_name* 
        
        Fuente:
        - https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_download_file.py
    '''
    # Representación local del bucket
    bucket = storage_client.bucket(TARGET_BUCKET_NAME)
    
    # Representación local del archivo
    blob = bucket.blob(TARGET_FILENAME)
    
    # Descargamos como bytes, ya que el ambiente donde se ejecuta
    # la cloud function es solo de lectura...
    file_bytes = blob.download_as_bytes()
    #blob.download_as_file(TARGET_FILENAME)

    print("Descargado {} desde bucket {}".format(
            TARGET_FILENAME, TARGET_BUCKET_NAME
        )
    )

    '''
    Aquí es donde se trabajaria con los bytes descargados
    A modo de ejemplo:
        pandas.read_excel(file_bytes)
    '''    


if __name__ == '__main__':
    main()
