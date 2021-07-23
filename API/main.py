from flask import Flask
from flask import jsonify
from config import config
from models import db
from models import Usuario1, Pais0, Cuenta0, UserCurrency0, CurrencyValue1, Currency0
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
	users = [ user.json() for user in Usuario1.query.all() ] 
	return jsonify({'users': users })

@app.route('/api/users/<id>', methods=['GET'])
def get_user(id):
	user = Usuario1.query.filter_by(id=id).first()
	if user is None:
		return jsonify({'message': 'El usuario no existe'}), 404

	return jsonify({'users': user.json() })

@app.route('/api/users/', methods=['POST'])
def create_user():
	json = request.get_json(force=True)

	if json.get('username') is None:
		return jsonify({'message': 'El formato está mal'}), 400

	user 		= Usuario1.create(json['username'],	
														json['surname'],
														json['email'],
														json['password'],	
														json['countryId'])

	return jsonify({
									'users'		: user.json(), 
								})

@app.route('/api/users/<id>', methods=['PUT'])
def update_user(id):
	user = Usuario1.query.filter_by(id=id).first()
	if user is None:
		return jsonify({'message': 'El usuario no existe'}), 404
	json = request.get_json(force=True)
	fields = ["username", "surname", "email", "password", "countryId"]
	for i in fields:
		if json.get(i) is None:
			return jsonify({'message': 'Solicitud Incorrecta'}), 400
	user.username = json['username']
	user.surname	= json['surname']
	user.email 		= json['email']
	user.password = json['password']
	user.country	= json['countryId']
	user.update()
	return jsonify({'users': user.json() })

@app.route('/api/users/<id>', methods=['DELETE'])
def delete_user(id):
	user = Usuario1.query.filter_by(id=id).first()
	if user is None:
		return jsonify({'message': 'El usuario no existe'}), 404

	user.delete()

	return jsonify({'users': user.json() })


##########
## PAIS #######
@app.route('/api/countries', methods=['GET'])
def get_countries():
	countries = [ country.json() for country in Pais0.query.all() ] 
	return jsonify({'countries': countries })

@app.route('/api/countries/<id>', methods=['GET'])
def get_country(id):
	country = Pais0.query.filter_by(id=id).first()
	if country is None:
		return jsonify({'message': 'El pais no existe'}), 404

	return jsonify({'countries': country.json() })

@app.route('/api/countries/', methods=['POST'])
def create_country():
	print("POSTTT")
	json = request.get_json(force=True)
	print(json)
	if json.get('countryName') is None:
		return jsonify({'message': 'El formato está mal'}), 400

	country 		= Pais0.create(json['countryName'])

	return jsonify({
									'countries'		: country.json(), 
								})

@app.route('/api/countries/<id>', methods=['PUT'])
def update_country(id):
	country = Pais0.query.filter_by(id=id).first()
	if country is None:
		return jsonify({'message': 'El pais no existe'}), 404
	json = request.get_json(force=True)
	if json.get("countryName") is None:
		return jsonify({'message': 'Solicitud Incorrecta'}), 400
	country.countryName = json['countryName']
	country.update()
	return jsonify({'countries': country.json() })

@app.route('/api/countries/<id>', methods=['DELETE'])
def delete_country(id):
	country = Pais0.query.filter_by(id=id).first()
	if country is None:
		return jsonify({'message': 'El pais no existe'}), 404

	country.delete()

	return jsonify({'countries': country.json() })

### CUENTA ######
@app.route('/api/accounts', methods=['GET'])
def get_accounts():
	accounts = [ account.json() for account in Cuenta0.query.all() ] 
	return jsonify({'accounts': accounts })

@app.route('/api/accounts/<id>', methods=['GET'])
def get_account(id):
	account = Cuenta0.query.filter_by(id=id).first()
	if account is None:
		return jsonify({'message': 'La cuenta no existe'}), 404

	return jsonify({'accounts': account.json() })

@app.route('/api/accounts/', methods=['POST'])
def create_account():
	json = request.get_json(force=True)
	
	fields = ['userId', 'balance']
	for i in fields:
		if json.get(i) is None:
			return jsonify({'message': 'El formato está mal'}), 400

	account = Cuenta0.create( json['userId'],	json['balance'])

	return jsonify({'accounts'		: account.json() })

@app.route('/api/accounts/<id>', methods=['PUT'])
def update_account(id):
	account = Cuenta0.query.filter_by(id=id).first()
	if account is None:
		return jsonify({'message': 'La cuenta no existe'}), 404
	json = request.get_json(force=True)
	fields = ['id', 'userId', 'balance']
	for i in fields:
		if json.get(i) is None:
			return jsonify({'message': 'Solicitud Incorrecta'}), 400
	account.userId	= json['userId']
	account.balance	= json['balance']
	account.update()
	return jsonify({'accounts': account.json() })

@app.route('/api/accounts/<id>', methods=['DELETE'])
def delete_account(id):
	account = Cuenta0.query.filter_by(id=id).first()
	if account is None:
		return jsonify({'message': 'La cuenta no existe'}), 404

	account.delete()

	return jsonify({'accounts': account.json() })


### USUARIX MONEDA ######
@app.route('/api/userCurrencies', methods=['GET'])
def get_userCurrencies():
	userCurrencies = [ userCurrency.json() for userCurrency in UserCurrency0.query.all() ] 
	return jsonify({'userCurrencies': userCurrencies })

@app.route('/api/userCurrencies/<userId>/<currencyId>', methods=['GET'])
def get_userCurrency(userId, currencyId):
	userCurrency = UserCurrency0.query.filter_by(userId=userId, currencyId = currencyId).first()
	if userCurrency is None:
		return jsonify({'message': 'Usuarix-Moneda no existe'}), 404

	return jsonify({'userCurrencies': userCurrency.json() })

@app.route('/api/userCurrencies/', methods=['POST'])
def create_userCurrency():
	json = request.get_json(force=True)
	
	fields = ['userId', 'currencyId','balance']
	for i in fields:
		if json.get(i) is None:
			return jsonify({'message': 'El formato está mal'}), 400

	userCurrency = UserCurrency0.create( json['userId'], json['currencyId'],	json['balance'])

	return jsonify({'userCurrencies'		: userCurrency.json() })

@app.route('/api/userCurrencies/<userId>/<currencyId>', methods=['PUT'])
def update_userCurrency(userId, currencyId):
	userCurrency = UserCurrency0.query.filter_by(userId=userId, currencyId = currencyId).first()
	if userCurrency is None:
		return jsonify({'message': 'Usuarix-Moneda no existe'}), 404
	json = request.get_json(force=True)
	print(json)
	fields = ['currencyId', 'userId', 'balance']
	for i in fields:
		if json.get(i) is None:
			return jsonify({'message': 'Solicitud Incorrecta'}), 400
	userCurrency.userId	= json['userId']
	userCurrency.currencyId = json['currencyId']
	userCurrency.balance	= json['balance']
	userCurrency.update()
	return jsonify({'userCurrencies': userCurrency.json() })

@app.route('/api/userCurrencies/<userId>/<currencyId>', methods=['DELETE'])
def delete_userCurrency(userId, currencyId):
	userCurrency = UserCurrency0.query.filter_by(userId=userId, currencyId = currencyId).first()
	if userCurrency is None:
		return jsonify({'message': 'Usuarix-Moneda no existe'}), 404

	userCurrency.delete()

	return jsonify({'userCurrencies': userCurrency.json() })


### PRCIOMONEDA ######
@app.route('/api/currencyValues', methods=['GET'])
def get_currencyValues():
	currencyValues = [ currencyValue.json() for currencyValue in CurrencyValue1.query.all() ] 
	return jsonify({'currencyValues': currencyValues })

@app.route('/api/currencyValues/<currencyId>/<createdAt>', methods=['GET'])
def get_currencyValue(currencyId, createdAt):
	createdAt = createdAt.replace('_',' ')
	createdAt = createdAt.replace('"','')
	createdAt = datetime.strptime(createdAt,'%y-%m-%d %H:%M:%S:%f')
	currencyValue = CurrencyValue1.query.filter_by(currencyId=currencyId, createdAt=createdAt).first()
	if currencyValue is None:
		return jsonify({'message': 'La moneda no existe'}), 404

	return jsonify({'currencyValues': currencyValue.json() })

@app.route('/api/currencyValues/', methods=['POST'])
def create_currencyValue():
	json = request.get_json(force=True)
	
	fields = [ 'currencyId','value']
	for i in fields:
		if json.get(i) is None:
			return jsonify({'message': 'El formato está mal'}), 400

	currencyValue = CurrencyValue1.create( json['currencyId'],json['value'])

	return jsonify({'currencyValues'		: currencyValue.json() })

@app.route('/api/currencyValues/<currencyId>/<createdAt>', methods=['PUT'])
def update_currencyValue(currencyId, createdAt):
	currencyValue = CurrencyValue1.query.filter_by(currencyId=currencyId, createdAt=createdAt).first()
	if currencyValue is None:
		return jsonify({'message': 'La moneda no existe'}), 404
	json = request.get_json(force=True)
	print(json)
	fields = ['currencyId', 'value']
	for i in fields:
		if json.get(i) is None:
			return jsonify({'message': 'Solicitud Incorrecta'}), 400
	currencyValue.currencyId = json['currencyId']
	currencyValue.value= json['value']
	currencyValue.update()
	return jsonify({'currencyValues': currencyValue.json() })

@app.route('/api/currencyValues/<currencyId>/<createdAt>', methods=['DELETE'])
def delete_currencyValue(currencyId, createdAt):
	currencyValue = CurrencyValue1.query.filter_by(currencyId=currencyId, createdAt=createdAt).first()
	if currencyValue is None:
		return jsonify({'message': 'La moneda no existe'}), 404

	currencyValue.delete()

	return jsonify({'currencyValues': currencyValue.json() })

###  MONEDA ######
@app.route('/api/currencies', methods=['GET'])
def get_currencies():
	currencies = [ currency.json() for currency in Currency0.query.all() ] 
	return jsonify({'currencies': currencies })

@app.route('/api/currencies/<id>', methods=['GET'])
def get_currency(id):
	currency = Currency0.query.filter_by(id=id).first()
	if currency is None:
		return jsonify({'message': 'La moneda no existe'}), 404

	return jsonify({'currencies': currency.json() })

@app.route('/api/currencies/', methods=['POST'])
def create_currency():
	json = request.get_json(force=True)
	
	fields = ['sigla', 'name']
	for i in fields:
		if json.get(i) is None:
			return jsonify({'message': 'El formato está mal'}), 400

	currency = Currency0.create( json['sigla'], json['name'])

	return jsonify({'currencies'		: currency.json() })

@app.route('/api/currencies/<id>', methods=['PUT'])
def update_currency(id):
	currency = Currency0.query.filter_by(id=id).first()
	if currency is None:
		return jsonify({'message': 'La moneda no existe'}), 404
	json = request.get_json(force=True)
	print(json)
	fields = ['sigla', 'name']
	for i in fields:
		if json.get(i) is None:
			return jsonify({'message': 'Solicitud Incorrecta'}), 400
	currency.sigla	= json['sigla']
	currency.name   = json['name']
	currency.update()
	return jsonify({'currencies': currency.json() })

@app.route('/api/currencies/<id>', methods=['DELETE'])
def delete_currency(id):
	currency = Currency0.query.filter_by(id=id).first()
	if currency is None:
		return jsonify({'message': 'La moneda no existe'}), 404

	currency.delete()

	return jsonify({'currencies': userCurrency.json() })

####### QUERIES ####
@app.route('/api/users/registeredBefore/<year>', methods=['GET'])
def get_registeredYear(year):
	users = [dict(user) for user in Usuario1.registeredYear(year = year).fetchall()]
	return jsonify({'users': users })

@app.route('/api/accounts/balanceOver/<minB>', methods=['GET'])
def get_minBalance(minB):
	accounts = [dict(account) for account in Cuenta0.minBalance(minB = minB).fetchall()]
	return jsonify({'accounts': accounts })

@app.route('/api/countries/getCitizens/<country>', methods=['GET'])
def get_getCitizens(country):
	countries = [dict(country) for country in Pais0.getCitizens(country=country).fetchall()]
	return jsonify({'countries': countries })

