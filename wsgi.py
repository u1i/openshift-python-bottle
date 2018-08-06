from bottle import Bottle, response
from datetime import datetime

application = Bottle(__name__)

@application.route("/")
def hello():
	return "Hello from Bottle!<hr>" + str(datetime.now())

@application.route("/api")
def hello():
	response.content_type = "application/json"
	stuff = { "message":"Hello from Bottle!","time": str(datetime.now())}
	return dict(stuff)

if __name__ == "__main__":
	application.run()
