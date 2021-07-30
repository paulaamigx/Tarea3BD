from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
# Importamos para realizar consultas personalizadas
from sqlalchemy import text

db = SQLAlchemy()

#### USUARIX ###
class Usuario(db.Model):
	__tablename__ = 'usuario_t3'
	id 							= db.Column(db.Integer, primary_key=True)
	nombre    			= db.Column(db.String(50), nullable=False) 
	apellido 				= db.Column(db.String(50), nullable=True) 
	correo					= db.Column(db.String(50), nullable=False) 
	contrasena			= db.Column(db.String(50), nullable=False) 
	pais						= db.Column(db.Integer, db.ForeignKey('pais_t3.id'), nullable=False);
	fecha_registro 	= db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())

	# Añadimos la relación
	cuenta_R	 			= db.relationship('Cuenta', lazy='dynamic', cascade="all,delete", backref="parent")
	usuarioMoneda_R = db.relationship('UsuarioMoneda', lazy='dynamic', cascade="all,delete", backref="parent")
	pais_R 					= db.relationship('Pais')
	
	@classmethod
	def create(cls, nombre, apellido, correo, contrasena, pais):
		# Instanciamos un nuevo usuario y lo guardamos en la bd
		user = Usuario(nombre			= nombre,
										apellido 		= apellido,
										correo 			= correo,
										contrasena	= contrasena,
										pais 				= pais
									 )
		return user.save()

	def save(self):
		try:
			db.session.add(self)
			db.session.commit()

			return self

		except Exception as e:
			print(e)
			return False

	def json(self):
		return {
			'id'						: self.id,
			'nombre'				: self.nombre,
			'apellido'			: self.apellido,
			'correo'				: self.correo,
			'contrasena'		: self.contrasena,
			'pais'					: self.pais,
			'fecha_registro': self.fecha_registro
			}
	def update(self):
		self.save()
	def delete(self):
		try:
			db.session.delete(self)
			db.session.commit()

			return True
		except:
			return False
	def registeredYear(year):
		try:
			query = 'SELECT * FROM usuario_t3 WHERE "fecha_registro" <='+"'"+str(year)+"-12-01' and " + '"fecha_registro" >= ' + "'" + str(year)+"-01-01'"
			result = db.session.execute(query)
			return result
		except Exception as e:
			print(e)
			return False

#### PAIS ####			
class Pais(db.Model):
	__tablename__ = 'pais_t3'
	id 			= db.Column(db.Integer, primary_key=True)
	nombre	= db.Column(db.String(45), nullable=False) 
	
	usuario_R = db.relationship('Usuario', cascade="all,delete", backref="parent", lazy='dynamic')
	
	@classmethod
	def create(cls, nombre):
		# Instanciamos un nuevo usuario y lo guardamos en la bd
		country = Pais(nombre	= nombre)
		return country.save()

	def save(self):
		try:
			db.session.add(self)
			db.session.commit()

			return self

		except Exception as e:
			print(e)
			return False

	def json(self):
		return {
			'id'			: self.id,
			'nombre'	: self.nombre,
			}
	def update(self):
		self.save()
	def delete(self):
		try:
			db.session.delete(self)
			db.session.commit()

			return True
		except:
			return False

	def getCitizens(country):
		try:
			query = 'SELECT id, nombre, apellido FROM usuario_t3 WHERE country =(SELECT id FROM pais_t3 WHERE "nombre" =' +"'" + country +"')" 
			result = db.session.execute(query)
			return result
		except Exception as e:
			print(e)
			return False

#### CUENTA ####			
class Cuenta(db.Model):
	__tablename__ = 'cuenta_bancaria_t3'
	id 					= db.Column(db.Integer, primary_key=True) #numeroCuenta
	id_usuario	= db.Column(db.Integer, db.ForeignKey("usuario_t3.id"), nullable=False)
	balance 		= db.Column(db.Float, nullable=False) 

	user = db.relationship('Usuario')
	
	@classmethod
	def create(cls, id_usuario, balance):
		# Instanciamos un nuevo usuario y lo guardamos en la bd
		account = Cuenta(id_usuario = id_usuario, balance = balance)
		return account.save()

	def save(self):
		try:
			db.session.add(self)
			db.session.commit()

			return self

		except Exception as e:
			print(e)
			return False

	def json(self):
		return {
			'id'					: self.id,
			'id_usuario'	: self.id_usuario,
			'balance'			:	self.balance
			}
	def update(self):
		self.save()
	def delete(self):
		try:
			db.session.delete(self)
			db.session.commit()

			return True
		except:
			return False

	def minBalance(minB):
		try:
			query = "SELECT id FROM cuenta_bancaria_t3  WHERE balance > " + str(minB)
			result = db.session.execute(query)
			return result
		except Exception as e:
			print(e)
			return False

#### USER CURRENCY ####			
class UsuarioMoneda(db.Model):
	__tablename__ = 'usuario_tiene_moneda_t3'
	id_usuario			= db.Column(db.Integer, db.ForeignKey('usuario_t3.id'), primary_key=True) 
	id_moneda	= db.Column(db.Integer, db.ForeignKey('moneda_t3.id'), primary_key = True, nullable=False) 
	balance 		= db.Column(db.Float, nullable=False) 

	moneda_R	= db.relationship("Moneda")
	usuario_R = db.relationship("Usuario")
	
	@classmethod
	def create(cls, id_usuario, id_moneda, balance):
		# Instanciamos un nuevo usuario y lo guardamos en la bd
		userCurr = UsuarioMoneda(id_usuario = id_usuario, id_moneda = id_moneda, balance = balance)
		return userCurr.save()

	def save(self):
		try:
			db.session.add(self)
			db.session.commit()

			return self

		except Exception as e:
			print(e)
			return False

	def json(self):
		return {
			'id_moneda': self.id_moneda,
			'id_usuario'		: self.id_usuario,
			'balance'		:	self.balance
			}
	def update(self):
		self.save()
	def delete(self):
		try:
			db.session.delete(self)
			db.session.commit()

			return True
		except:
			return False

#### PRECIO MONEDA ####			
class PrecioMoneda(db.Model):
	__tablename__ = 'precio_moneda_t3'
	id_moneda	= db.Column(db.Integer, db.ForeignKey('moneda_t3.id'), primary_key = True, nullable=False) 
	valor				= db.Column(db.Float, nullable=False) 
	fecha		= db.Column(db.DateTime(), primary_key = True, nullable=False, default=db.func.current_timestamp())

	#moneda_R= db.relationship("Moneda")	

	@classmethod
	def create(cls, id_moneda, valor):
		# Instanciamos un nuevo usuario y lo guardamos en la bd
		currencyvalor = PrecioMoneda( id_moneda = id_moneda, valor = valor)
		return currencyvalor.save()

	def save(self):
		try:
			db.session.add(self)
			db.session.commit()

			return self

		except Exception as e:
			print(e)
			return False

	def json(self):
		return {
			'id_moneda'	: self.id_moneda,
			'valor'			:	self.valor,
			'fecha'			: self.fecha.strftime('%y-%m-%d %H:%M:%S:%f')
			}
	def update(self):
		self.save()
	def delete(self):
		try:
			db.session.delete(self)
			db.session.commit()

			return True
		except:
			return False

#### MONEDA ####			
class Moneda(db.Model):
	__tablename__	= 'moneda_t3'
	id						= db.Column(db.Integer, primary_key = True, nullable=False) 
	sigla					= db.Column(db.String(10), nullable=False) 
	nombre				= db.Column(db.String(80),  nullable=False)

	#usuarioMoneda_R = db.relationship('UsuarioMoneda', cascade="all,delete", backref="parent", lazy='dynamic')
	precioMoneda_R	 = db.relationship('PrecioMoneda', cascade="all,delete", backref="parent", lazy='dynamic')
	
	@classmethod
	def create(cls, sigla, nombre):
		# Instanciamos un nuevo usuario y lo guardamos en la bd
		currency = Moneda(sigla = sigla, nombre = nombre)
		return currency.save()

	def save(self):
		try:
			db.session.add(self)
			db.session.commit()

			return self

		except Exception as e:
			print(e)
			return False

	def json(self):
		return {
			'id'				: self.id,
			'sigla'			:	self.sigla,
			'nombre'		: self.nombre
			}
	def update(self):
		self.save()
	def delete(self):
		try:
			db.session.delete(self)
			db.session.commit()

			return True
		except:
			return False
