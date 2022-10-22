from flask_restful import Resource
from flask import jsonify, request

clientes = [
    {
        "id": "1",
        "nombre":"Pacman",
        "apellido": "Boga"
    },
    {
        "id": "2",
        "nombre":"Luisa",
        "apeelido": "Ramirez"
    }
] 


class Clientes(Resource):
    def get(self): # Read all
        return jsonify( ## usamos este serializador JSON porque Python no convierte
                        # directamente los objetos "lista" a JSON
            {
                "clientes": clientes
            }
        )

    def post(self): # Create
        cliente = request.get_json()
        clientes.append(cliente)
        return cliente, 201
        

class Cliente(Resource):
    def get(self, id): # Read id
            return (
            {
                "cliente": clientes[int(id)], # hay que convertir el String a entero
            }
        )

    def delete(self, id): # Delete id

        clientes.pop(int(id))
        return {
            "Mensaje" : f"Registro {id} borrado"
        }

    def put(self, id): # Update id
        cliente = request.get_json() # Suponiendo que se ha etregado todo el registro completo en el request
        clientes[int(id)] = cliente
        return cliente

        


