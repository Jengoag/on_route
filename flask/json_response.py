from flask import Response
import json

def json_response(data, status=200):
    return Response(
        json.dumps([dict(ix) for ix in data]),
        status,
        mimetype="application/json"
    )


## queda tal cual o hay que cambiar argumentos??