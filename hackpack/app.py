import re

from flask import Flask
from flask import render_template
from flask import url_for
from flask import request

from twilio import twiml
from twilio.util import TwilioCapability

import phonenumbers # libphonenumber
# Declare and configure application
app = Flask(__name__, static_url_path='/static')
app.config.from_pyfile('local_settings.py')

def str2bool(v):
  return v.lower() in ("yes", "true", "t", "1")

# Voice Request URL
@app.route('/voice', methods=['GET', 'POST'])
def voice():
    to = request.values.get('To', None)
    regionCode = request.values.get('regionCode','US')
    if to is None:
        return ("Point the voice URL of your registration-enabled Twilio SIP domain to this script. "
                "You will see what it can do for you :-)")
    found_number = re.search("^sip:([+]?[0-9]{10,14})@", to)
    if found_number:
        number = phonenumbers.parse(found_number.group(1),regionCode)
        to = phonenumbers.format_number(number,phonenumbers.PhoneNumberFormat.E164)
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




# Installation success page
@app.route('/')
def index():

    voice_url = url_for('.voice', _external=True) + "?callerId=+1NXXNXXXXXX"

    params = {
         'Voice URL': voice_url
    }
    return render_template('index.html', params=params,
                           configuration_error=None)
