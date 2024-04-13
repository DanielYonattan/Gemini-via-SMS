import os
import config
import google.generativeai as genai
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

genai.configure(api_key=config.GEMINI_KEY)

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    # Get the message the user sent our Twilio number
    inbound_message = request.values.get('Body', None)

    # prompt gemini
    model = genai.GenerativeModel('gemini-pro')
    gemini_response = model.generate_content(config.PROMPT + inbound_message)

    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    resp.message(gemini_response.text)

    return str(resp)

if __name__ == "__main__":
  app.run()
