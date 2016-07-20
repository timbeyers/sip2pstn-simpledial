import re

from flask import Flask
from flask import render_template
from flask import url_for
from flask import request

from twilio import twiml
from twilio.util import TwilioCapability

# Declare and configure application
app = Flask(__name__, static_url_path='/static')
app.config.from_pyfile('local_settings.py')

def str2bool(v):
  return v.lower() in ("yes", "true", "t", "1")

# Voice Request URL
@app.route('/voice', methods=['GET', 'POST'])
def voice():
    to = request.values.get('To', None)
    if to is None:
        return ("Point the voice URL of your registration-enabled Twilio SIP domain to this script. "
                "You will see what it can do for you :-)")

    found_us_pstn = re.search("^sip:[+]?1?([0-9]{10})@", to)
    found_int_pstn = re.search("^sip:[+]?([0-9]{10,14})@", to)
    if found_us_pstn:
        to = "+1{0}".format(found_us_pstn.group(1))
    elif found_int_pstn:
        to = "+{0}".format(found_int_pstn.group(1))

    answer_on_bridge = str2bool(request.values.get('answerOnBridge', "True"))
    record_param = request.values.get('record', 'do-not-record')

    response = twiml.Response()

    if to.startswith("sip:"):
        with response.dial(answerOnBridge=answer_on_bridge, record=record_param) as d:
            d.sip(to)
    else:
        caller_id = request.values.get('callerId', app.config['TWILIO_CALLER_ID'])
        with response.dial(answerOnBridge=answer_on_bridge, callerId=caller_id, record=record_param) as d:
            d.number(to)

    return str(response)


# SMS Request URL
@app.route('/sms', methods=['GET', 'POST'])
def sms():
    response = twiml.Response()
    response.sms("Congratulations! You deployed the Twilio Hackpack "
                 "for Heroku and Flask.")
    return str(response)


# Twilio Client demo template
@app.route('/client')
def client():
    configuration_error = None
    for key in ('TWILIO_ACCOUNT_SID', 'TWILIO_AUTH_TOKEN', 'TWILIO_APP_SID',
                'TWILIO_CALLER_ID'):
        if not app.config.get(key, None):
            configuration_error = "Missing from local_settings.py: " \
                                  "{0}".format(key)
            token = None

    if not configuration_error:
        capability = TwilioCapability(app.config['TWILIO_ACCOUNT_SID'],
                                      app.config['TWILIO_AUTH_TOKEN'])
        capability.allow_client_incoming("joey_ramone")
        capability.allow_client_outgoing(app.config['TWILIO_APP_SID'])
        token = capability.generate()
    params = {'token': token}
    return render_template('client.html', params=params,
                           configuration_error=configuration_error)


@app.route('/client/incoming', methods=['POST'])
def client_incoming():
    try:
        from_number = request.values.get('PhoneNumber', None)

        resp = twiml.Response()

        if not from_number:
            resp.say("Your app is missing a Phone Number. "
                     "Make a request with a Phone Number to make outgoing "
                     "calls with the Twilio hack pack.")
            return str(resp)

        if 'TWILIO_CALLER_ID' not in app.config:
            resp.say(
                "Your app is missing a Caller ID parameter. "
                "Please add a Caller ID to make outgoing calls with Twilio "
                "Client")
            return str(resp)

        with resp.dial(callerId=app.config['TWILIO_CALLER_ID']) as r:
            # If we have a number, and it looks like a phone number:
            if from_number and re.search('^[\d\(\)\- \+]+$', from_number):
                r.number(from_number)
            else:
                r.say("We couldn't find a phone number to dial. Make sure "
                      "you are sending a Phone Number when you make a "
                      "request with Twilio Client")

        return str(resp)

    except:
        resp = twiml.Response()
        resp.say("An error occurred. Check your debugger at twilio dot com "
                 "for more information.")
        return str(resp)


# Installation success page
@app.route('/')
def index():
    params = {
        'Voice Request URL': url_for('.voice', _external=True),
#        'SMS Request URL': url_for('.sms', _external=True),
#        'Client URL': url_for('.client', _external=True)
    }
    return render_template('index.html', params=params,
                           configuration_error=None)
