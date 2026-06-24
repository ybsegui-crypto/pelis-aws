import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Pelis')

HEADERS = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': '*',
    'Access-Control-Allow-Methods': '*'
}

def lambda_handler(event, context):
    method = event['requestContext']['http']['method']
    path = event.get('rawPath', '/')

    try:
        if method == 'GET':
            return listar()
        elif method == 'POST':
            body = json.loads(event.get('body') or '{}')
            return crear(body)
        elif method == 'DELETE':
            peli_id = event['pathParameters']['id']
            return borrar(peli_id)
        else:
            return responder(404, {'error': 'Ruta no encontrada'})
    except Exception as e:
        print(f'ERROR: {e}')
        return responder(500, {'error': str(e)})


def listar():
    result = table.scan()
    return responder(200, result['Items'])


def crear(body):
    item = {
        'id': str(uuid.uuid4()),
        'titulo': body.get('titulo', 'Sin título'),
        'genero': body.get('genero', 'general'),
        'estado': 'pendiente'
    }
    table.put_item(Item=item)
    return responder(201, item)


def borrar(peli_id):
    table.delete_item(Key={'id': peli_id})
    return responder(200, {'borrada': peli_id})


def responder(status, body):
    return {
        'statusCode': status,
        'headers': HEADERS,
        'body': json.dumps(body, default=str)
    }