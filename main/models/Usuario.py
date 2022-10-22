from .. import db
from sqlalchemy import Column as _Column, Integer as _Integer, String as _String, DateTime as _DateTime
import datetime as dt

class Usuario(db.Model):
    id = _Column(_Integer, primary_key=True)
    nombre = _Column(_String(45), nullable=False)
    apellido = _Column(_String(45), nullable=False)
    email = _Column(_String(60), nullable=False, unique=True, index=True)
    role = _Column(_String(45), nullable=False, default="cliente")
    telefono = _Column(_Integer, nullable=False)
    password = _Column(_String(100), nullable=False)
    fecha_registro = _Column(_DateTime, default=dt.datetime.now(), nullable=False)
    compras = db.relationship('Compra', back_populates="usuario", cascade="all, delete-orphan")
    
    # Un represantador de conveniencia
    def __repr__(self):
        return f'{self.nombre}'

    # Implementacion de la serializacion a JSON desde python object
    def to_json(self):
        usuario_json = {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'email': self.email,
            'telefono': self.telefono,
            'role': self.role,
            'fecha': str(self.fecha_registro)
        }
        return usuario_json

    # Implementacion de la conversion desde JSON a python object
    @staticmethod
    def from_json(usuario_json):
        id = usuario_json.get('id')
        nombre = usuario_json.get('nombre')
        apellido = usuario_json.get('apellido')
        email = usuario_json.get('email')
        telefono = usuario_json.get('telefono')
        password = usuario_json.get('password')
        role = usuario_json.get('role')
        fecha_registro = usuario_json.get('fecha_registro')
        return Usuario(
            id = id,
            nombre = nombre,
            apellido = apellido,
            email = email,
            telefono = telefono,
            plain_password = password,
            role = role,
            fecha_registro = fecha_registro
        )
