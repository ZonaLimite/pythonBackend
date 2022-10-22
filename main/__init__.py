import os
from flask import Flask
from dotenv import load_dotenv

# Importo el modulo para crear la api-rest
from flask_restful import Api

# Importo el modulo para conectarme a una base de datos
from flask_sqlalchemy import SQLAlchemy

api = Api()

db = SQLAlchemy()

def create_app():
    # Comprobacion y asignacion de freawork
    app = Flask(__name__)
    
    # Cargar las variables de entorno
    load_dotenv()

    # Configuracion de la base de datos
    PATH = os.getenv("DATABASE_PATH")
    DB_NAME = os.getenv("DATABASE_NAME")
    # Genera el archivo de base de datos si no existe
    if not os.path.exists(f'{PATH}{DB_NAME}'):
        print(f'path={PATH}')
        print(f'base={DB_NAME}')        
        os.chdir(f'{PATH}')
        file = os.open(f'{DB_NAME}',os.O_CREAT)


    # Detecta cambios en la base y hace un segumiento (a false)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =  False
    # Inicializa la base datos(SQlite)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{PATH}{DB_NAME}'
    db.init_app(app)

    import main.resources as resources
    api.add_resource(resources.ClientesResource, '/clientes')
    api.add_resource(resources.ClienteResource, '/cliente/<id>')
    ##api.add_resource(resources.UsuariosResource, '/usuarios')
    ##api.add_resource(resources.UsuarioResource, '/usuario/<id>')
    ##api.add_resource(resources.ComprasResource, '/compras')
    ##api.add_resource(resources.CompraResource, '/compra/<id>')
    api.add_resource(resources.ProductosResource, '/productos')
    api.add_resource(resources.ProductoResource, '/producto/<id>')
    ##api.add_resource(resources.ProductosComprasResource, '/productos-compras')
    ##api.add_resource(resources.ProductoCompraResource, '/producto-compra/<id>')

    # Inicializacion del framework Restful
    api.init_app(app)

    return app


