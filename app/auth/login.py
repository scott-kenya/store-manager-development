import jwt
import datetime
from app import create_app
from functools import wraps

from flask import request, make_response

app.config['SECRET_KEY']= 'cartoonbaboon'






def logi_required(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		token = request.args.get('token')
		if not token:
			return jsonify({'message':'token missing'}), 403


		#verify if token is valid
		try:
			data = jwt.decode(token, app.config['SECRET_KEY'])
		except:
			return jsonify({'message':'token invalid'}), 403
		return f(*args, **kwargs)








def login():
	rea = request.authorization

	if rea and rea.password == 'password' and rea.username == 'username':
		token = jwt.encode({'user': rea.username, 
			'password': rea.password, 
			'exp': datetime.datetime.utcnow()+ datetime.timedelta(minutes=45)},
			app.config[SECRET_KEY])
		return jsonify({'token':token.decode('UTF-8')})
	return make_response('needs verification',401,
		{'WWW.Authenticate':'Basic realm="login Required"'})



	if __name__ == '__main__':
		app.run()