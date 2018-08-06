from bottle import Bottle, response
application = Bottle(__name__)

@application.route("/")
def hello():
	return "Hello from Bottle!"

@application.route("/api")
def hello():
	response.content_type = "application/json"
	return '{"message":"Hello from Bottle!"}'

if __name__ == "__main__":
	application.run()
