from flask import Flask
from flask import request
from flask import json
from flask import jsonify
from flask_cors import CORS, cross_origin
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"
@app.route("/sendMail", methods=["POST"])
@cross_origin()
def sendMail():
    to_email = request.json["to_email"]
    if request.method == "POST":

        message = Mail(
        from_email='nishantbhagat435@gmail.com',
        to_emails=to_email,
        subject='You have successfully subscribed to our Newsletter!',
        html_content='<strong>You have successfully subscribed to our Newsletter!</strong>')
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e)
        
        return {"status": "sent"}


if __name__ == "__main__":
    app.run()