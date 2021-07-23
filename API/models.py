from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
# Importamos para realizar consultas personalizadas
from sqlalchemy import text

db = SQLAlchemy()

#### USUARIX ###
class Usuario1(db.Model):
	__tablename__ = 'usuario1'
	id 				= db.Column(db.Integer, primary_key=True)
	username	= db.Column(db.String(50), nullable=False) 
	surname 	= db.Column(db.String(50), nullable=True) 
	email			= db.Column(db.String(50), nullable=False) 
	password	= db.Column(db.String(50), nullable=False) 
	#country		= db.Column(db.Integer, nullable=False) 
	createdAt = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())
	country = db.Column(db.Integer, db.ForeignKey('pais00.id'), nullable=False);

	# Añadimos la relación
	account = db.relationship('Cuenta0', lazy='dynamic', cascade="all,delete", backref="parent")
	userCurr = db.relationship('UserCurrency0', lazy='dynamic', cascade="all,delete", backref="parent")
	countryR = db.relationship('Pais0')
	
	@classmethod
	def create(cls, username, surname, email, password, country):
		# Instanciamos un nuevo usuario y lo guardamos en la bd
		user = Usuario1(username	= username,
										surname 	= surname,
										email 		= email,
										password 	= password,
										country 	= country
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
			'id'			: self.id,
			'username': self.username,
			'surname'	: self.surname,
			'email'		: self.email,
			'password': self.password,
			'country'	: self.country,
			'createdAt': self.createdAt
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
			query = 'SELECT * FROM usuario1 WHERE "createdAt" <='+"'"+str(year)+"-12-01' and " + '"createdAt" >= ' + "'" + str(year)+"-01-01'"
			result = db.session.execute(query)
			return result
		except Exception as e:
			print(e)
			return False

#### PAIS ####			
class Pais0(db.Model):
	__tablename__ = 'pais00'
	id 					= db.Column(db.Integer, primary_key=True)
	countryName	= db.Column(db.String(45), nullable=False) 
	
	user = db.relationship('Usuario1', cascade="all,delete", backref="parent", lazy='dynamic')
	
	@classmethod
	def create(cls, countryName):
		# Instanciamos un nuevo usuario y lo guardamos en la bd
		country = Pais0(countryName	= countryName)
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
			'countryName': self.countryName,
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
			query = 'SELECT username, surname FROM usuario1 WHERE country =(SELECT id FROM pais00 WHERE "countryName" =' +"'" + country +"')" 
			result = db.session.execute(query)
			return result
		except Exception as e:
			print(e)
			return False

#### CUENTA ####			
class Cuenta0(db.Model):
	__tablename__ = 'cuenta0'
	id 					= db.Column(db.Integer, primary_key=True) #numeroCuenta
	userId 			= db.Column(db.Integer, db.ForeignKey("usuario1.id"), nullable=False)
	balance 		= db.Column(db.Float, nullable=False) 

	user = db.relationship('Usuario1')
	
	@classmethod
	def create(cls, userId, balance):
		# Instanciamos un nuevo usuario y lo guardamos en la bd
		account = Cuenta0(userId = userId, balance = balance)
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
			'id'			: self.id,
			'userId'	: self.userId,
			'balance'	:	self.balance
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
			query = "SELECT id FROM cuenta0  WHERE balance > " + str(minB)
			result = db.session.execute(query)
			return result
		except Exception as e:
			print(e)
			return False

#### USER CURRENCY ####			
class UserCurrency0(db.Model):
	__tablename__ = 'usercurr0'
	userId			= db.Column(db.Integer, db.ForeignKey('usuario1.id'), primary_key=True) 
	currencyId	= db.Column(db.Integer, db.ForeignKey('currency0.id'), primary_key = True, nullable=False) 
	balance 		= db.Column(db.Float, nullable=False) 

	currency = db.relationship("Currency0")
	user     = db.relationship("Usuario1")
	
	@classmethod
	def create(cls, userId, currencyId, balance):
		# Instanciamos un nuevo usuario y lo guardamos en la bd
		userCurr = UserCurrency0(userId = userId, currencyId = currencyId, balance = balance)
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
			'currencyId': self.currencyId,
			'userId'		: self.userId,
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

#### PRECIO MONEDAY ####			
class CurrencyValue1(db.Model):
	__tablename__ = 'currencyValue2'
	currencyId	= db.Column(db.Integer, db.ForeignKey('currency0.id'), primary_key = True, nullable=False) 
	value				= db.Column(db.Float, nullable=False) 
	createdAt		= db.Column(db.DateTime(), primary_key = True, nullable=False, default=db.func.current_timestamp())

	currency = db.relationship("Currency0")	

	@classmethod
	def create(cls, currencyId, value):
		# Instanciamos un nuevo usuario y lo guardamos en la bd
		currencyValue = CurrencyValue1( currencyId = currencyId, value = value)
		return currencyValue.save()

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
			'currencyId'				: self.currencyId,
			'value'			:	self.value,
			'createdAt'	: self.createdAt.strftime('%y-%m-%d %H:%M:%S:%f')
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
class Currency0(db.Model):
	__tablename__ = 'currency0'
	id					= db.Column(db.Integer, primary_key = True, nullable=False) 
	sigla				= db.Column(db.String(10), nullable=False) 
	name				= db.Column(db.String(80),  nullable=False)

	#userCurrencyR  = db.relationship('UserCurrency0', cascade="all,delete", backref="parent", lazy='dynamic')
	currencyValue = db.relationship('CurrencyValue1', cascade="all,delete", backref="parent", lazy='dynamic')
	
	@classmethod
	def create(cls, sigla, name):
		# Instanciamos un nuevo usuario y lo guardamos en la bd
		currency = Currency0(sigla = sigla, name = name)
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
			'name'	: self.name
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
