from flask import Flask
from flask import jsonify
from config import config
from models import db
from models import Usuario, Pais, Cuenta, UsuarioMoneda, PrecioMoneda, Moneda
from flask import request
from datetime import datetime
from sqlalchemy import Date, cast, func

def create_app(enviroment):
	app = Flask(__name__)
	app.config.from_object(enviroment)
	with app.app_context():
		db.init_app(app)
		db.create_all()
	return app


enviroment = config['development']
app = create_app(enviroment)
####

###USUARIX
@app.route('/api/users', methods=['GET'])
def get_users():
	users = [ user.json() for user in Usuario.query.all() ] 
	return jsonify({'users': users })

@app.route('/api/users/<id>', methods=['GET'])
def get_user(id):
	user = Usuario.query.filter_by(id=id).first()
	if user is None:
		return jsonify({'message': 'El usuario no existe'}), 404

	return jsonify({'users': user.json() })

@app.route('/api/users/', methods=['POST'])
def create_user():
	json = request.get_json(force=True)
	
	print('POSTT')
	fields = ['nombre', 'apellido', 'correo', 'contrasena', 'pais']
	for i in fields:
		if json.get(i) is None:
			return jsonify({'message': 'El formato está mal'}), 400

	user 		= Usuario.create(json['nombre'],	
														json['apellido'],
														json['correo'],
														json['contrasena'],	
														json['pais'])

	return jsonify({
									'users'		: user.json(), 
								})

@app.route('/api/users/<id>', methods=['PUT'])
def update_user(id):
	user = Usuario.query.filter_by(id=id).first()
	if user is None:
		return jsonify({'message': 'El usuario no existe'}), 404
	json = request.get_json(force=True)
	fields = ["nombre", "apellido", "correo", "contrasena", "pais"]
	for i in fields:
		if json.get(i) is None:
			return jsonify({'message': 'Solicitud Incorrecta'}), 400
	user.nombre 		= json['nombre']
	user.apellido		= json['apellido']
	user.correo 		= json['correo']
	user.contrasena = json['contrasena']
	user.country		= json['pais']
	user.update()
	return jsonify({'users': user.json() })

@app.route('/api/users/<id>', methods=['DELETE'])
def delete_user(id):
	user = Usuario.query.filter_by(id=id).first()
	if user is None:
		return jsonify({'message': 'El usuario no existe'}), 404

	user.delete()

	return jsonify({'users': user.json() })


##########
## PAIS #######
@app.route('/api/countries', methods=['GET'])
def get_countries():
	countries = [ country.json() for country in Pais.query.all() ] 
	return jsonify({'countries': countries })

@app.route('/api/countries/<id>', methods=['GET'])
def get_country(id):
	country = Pais.query.filter_by(id=id).first()
	if country is None:
		return jsonify({'message': 'El pais no existe'}), 404

	return jsonify({'countries': country.json() })

@app.route('/api/countries/', methods=['POST'])
def create_country():
	json = request.get_json(force=True)
	if json.get('nombre') is None:
		return jsonify({'message': 'El formato está mal'}), 400

	country 		= Pais.create(json['nombre'])

	return jsonify({
									'countries'		: country.json(), 
								})

@app.route('/api/countries/<id>', methods=['PUT'])
def update_country(id):
	country = Pais.query.filter_by(id=id).first()
	if country is None:
		return jsonify({'message': 'El pais no existe'}), 404
	json = request.get_json(force=True)
	if json.get("nombre") is None:
		return jsonify({'message': 'Solicitud Incorrecta'}), 400
	country.nombre = json['nombre']
	country.update()
	return jsonify({'countries': country.json() })

@app.route('/api/countries/<id>', methods=['DELETE'])
def delete_country(id):
	country = Pais.query.filter_by(id=id).first()
	if country is None:
		return jsonify({'message': 'El pais no existe'}), 404

	country.delete()

	return jsonify({'countries': country.json() })

### CUENTA ######
@app.route('/api/accounts', methods=['GET'])
def get_accounts():
	accounts = [ account.json() for account in Cuenta.query.all() ] 
	return jsonify({'accounts': accounts })

@app.route('/api/accounts/<id>', methods=['GET'])
def get_account(id):
	account = Cuenta.query.filter_by(id=id).first()
	if account is None:
		return jsonify({'message': 'La cuenta no existe'}), 404

	return jsonify({'accounts': account.json() })

@app.route('/api/accounts/', methods=['POST'])
def create_account():
	json = request.get_json(force=True)
	
	fields = ['id_usuario', 'balance']
	for i in fields:
		if json.get(i) is None:
			return jsonify({'message': 'El formato está mal'}), 400

	account = Cuenta.create( json['id_usuario'],	json['balance'])

	return jsonify({'accounts'		: account.json() })

@app.route('/api/accounts/<id>', methods=['PUT'])
def update_account(id):
	account = Cuenta.query.filter_by(id=id).first()
	if account is None:
		return jsonify({'message': 'La cuenta no existe'}), 404
	json = request.get_json(force=True)
	fields = ['id', 'id_usuario', 'balance']
	for i in fields:
		if json.get(i) is None:
			return jsonify({'message': 'Solicitud Incorrecta'}), 400
	account.id_usuario	= json['id_usuario']
	account.balance	= json['balance']
	account.update()
	return jsonify({'accounts': account.json() })

@app.route('/api/accounts/<id>', methods=['DELETE'])
def delete_account(id):
	account = Cuenta.query.filter_by(id=id).first()
	if account is None:
		return jsonify({'message': 'La cuenta no existe'}), 404

	account.delete()

	return jsonify({'accounts': account.json() })


### USUARIX MONEDA ######
@app.route('/api/userCurrencies', methods=['GET'])
def get_userCurrencies():
	userCurrencies = [ userCurrency.json() for userCurrency in UsuarioMoneda.query.all() ] 
	return jsonify({'userCurrencies': userCurrencies })

@app.route('/api/userCurrencies/<id_usuario>/<id_moneda>', methods=['GET'])
def get_userCurrency(id_usuario, id_moneda):
	userCurrency = UsuarioMoneda.query.filter_by(id_usuario=id_usuario, id_moneda = id_moneda).first()
	if userCurrency is None:
		return jsonify({'message': 'Usuarix-Moneda no existe'}), 404

	return jsonify({'userCurrencies': userCurrency.json() })

@app.route('/api/userCurrencies/', methods=['POST'])
def create_userCurrency():
	json = request.get_json(force=True)
	
	fields = ['id_usuario', 'id_moneda','balance']
	for i in fields:
		if json.get(i) is None:
			return jsonify({'message': 'El formato está mal'}), 400

	userCurrency = UsuarioMoneda.create( json['id_usuario'], json['id_moneda'],	json['balance'])

	return jsonify({'userCurrencies'		: userCurrency.json() })

@app.route('/api/userCurrencies/<id_usuario>/<id_moneda>', methods=['PUT'])
def update_userCurrency(id_usuario, id_moneda):
	userCurrency = UsuarioMoneda.query.filter_by(id_usuario=id_usuario, id_moneda = id_moneda).first()
	if userCurrency is None:
		return jsonify({'message': 'Usuarix-Moneda no existe'}), 404
	json = request.get_json(force=True)
	fields = ['id_moneda', 'id_usuario', 'balance']
	for i in fields:
		if json.get(i) is None:
			return jsonify({'message': 'Solicitud Incorrecta'}), 400
	userCurrency.id_usuario	= json['id_usuario']
	userCurrency.id_moneda 	= json['id_moneda']
	userCurrency.balance		= json['balance']
	userCurrency.update()
	return jsonify({'userCurrencies': userCurrency.json() })

@app.route('/api/userCurrencies/<id_usuario>/<id_moneda>', methods=['DELETE'])
def delete_userCurrency(id_usuario, id_moneda):
	userCurrency = UsuarioMoneda.query.filter_by(id_usuario=id_usuario, id_moneda = id_moneda).first()
	if userCurrency is None:
		return jsonify({'message': 'Usuarix-Moneda no existe'}), 404

	userCurrency.delete()

	return jsonify({'userCurrencies': userCurrency.json() })


### PRCIOMONEDA ######
@app.route('/api/currencyValues', methods=['GET'])
def get_currencyValues():
	currencyValues = [ currencyValue.json() for currencyValue in PrecioMoneda.query.all() ] 
	return jsonify({'currencyValues': currencyValues })

@app.route('/api/currencyValues/<id_moneda>/<fecha>', methods=['GET'])
def get_currencyValue(id_moneda, fecha):
	fecha = fecha.replace('_',' ')
	fecha = fecha.replace('"','')
	fecha = datetime.strptime(fecha,'%y-%m-%d %H:%M:%S:%f')
	currencyValue = PrecioMoneda.query.filter_by(id_moneda=id_moneda, fecha=fecha).first()
	if currencyValue is None:
		return jsonify({'message': 'La moneda no existe'}), 404

	return jsonify({'currencyValues': currencyValue.json() })

@app.route('/api/currencyValues/', methods=['POST'])
def create_currencyValue():
	json = request.get_json(force=True)
	
	fields = [ 'id_moneda','value']
	for i in fields:
		if json.get(i) is None:
			return jsonify({'message': 'El formato está mal'}), 400

	currencyValue = PrecioMoneda.create( json['id_moneda'],json['value'])

	return jsonify({'currencyValues'		: currencyValue.json() })

@app.route('/api/currencyValues/<id_moneda>/<fecha>', methods=['PUT'])
def update_currencyValue(id_moneda, fecha):
	currencyValue = PrecioMoneda.query.filter_by(id_moneda=id_moneda, fecha=fecha).first()
	if currencyValue is None:
		return jsonify({'message': 'La moneda no existe'}), 404
	json = request.get_json(force=True)
	print(json)
	fields = ['id_moneda', 'valor']
	for i in fields:
		if json.get(i) is None:
			return jsonify({'message': 'Solicitud Incorrecta'}), 400
	currencyValue.id_moneda = json['id_moneda']
	currencyValue.valor			= json['valor']
	currencyValue.update()
	return jsonify({'currencyValues': currencyValue.json() })

@app.route('/api/currencyValues/<id_moneda>/<fecha>', methods=['DELETE'])
def delete_currencyValue(id_moneda, fecha):
	currencyValue = PrecioMoneda.query.filter_by(id_moneda=id_moneda, fecha=fecha).first()
	if currencyValue is None:
		return jsonify({'message': 'La moneda no existe'}), 404

	currencyValue.delete()

	return jsonify({'currencyValues': currencyValue.json() })

###  MONEDA ######
@app.route('/api/currencies', methods=['GET'])
def get_currencies():
	currencies = [ currency.json() for currency in Moneda.query.all() ] 
	return jsonify({'currencies': currencies })

@app.route('/api/currencies/<id>', methods=['GET'])
def get_currency(id):
	currency = Moneda.query.filter_by(id=id).first()
	if currency is None:
		return jsonify({'message': 'La moneda no existe'}), 404

	return jsonify({'currencies': currency.json() })

@app.route('/api/currencies/', methods=['POST'])
def create_currency():
	json = request.get_json(force=True)
	
	fields = ['sigla', 'nombre']
	for i in fields:
		if json.get(i) is None:
			return jsonify({'message': 'El formato está mal'}), 400

	currency = Moneda.create( json['sigla'], json['nombre'])

	return jsonify({'currencies'		: currency.json() })

@app.route('/api/currencies/<id>', methods=['PUT'])
def update_currency(id):
	currency = Moneda.query.filter_by(id=id).first()
	if currency is None:
		return jsonify({'message': 'La moneda no existe'}), 404
	json = request.get_json(force=True)
	print(json)
	fields = ['sigla', 'nombre']
	for i in fields:
		if json.get(i) is None:
			return jsonify({'message': 'Solicitud Incorrecta'}), 400
	currency.sigla		= json['sigla']
	currency.nombre   = json['nombre']
	currency.update()
	return jsonify({'currencies': currency.json() })

@app.route('/api/currencies/<id>', methods=['DELETE'])
def delete_currency(id):
	currency = Moneda.query.filter_by(id=id).first()
	if currency is None:
		return jsonify({'message': 'La moneda no existe'}), 404

	currency.delete()

	return jsonify({'currencies': userCurrency.json() })

####### QUERIES ####
@app.route('/api/consultas/1/<year>', methods=['GET'])
def get_registeredYear(year):
	users = [dict(user) for user in Usuario.registeredYear(year = year).fetchall()]
	return jsonify({'users': users })

@app.route('/api/consultas/2/<minB>', methods=['GET'])
def get_minBalance(minB):
	accounts = [dict(account) for account in Cuenta.minBalance(minB = minB).fetchall()]
	return jsonify({'accounts': accounts })

@app.route('/api/consultas/3/<country>', methods=['GET'])
def get_getCitizens(country):
	countries = [dict(country) for country in Pais.getCitizens(country=country).fetchall()]
	return jsonify({'countries': countries })

