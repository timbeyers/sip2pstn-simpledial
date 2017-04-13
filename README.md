# Twilio sip2pstn-simpledial for Heroku and Flask
* <b> Connect your SIP-based IP Phone to Twilio and call any phone in the world </b>
* <b> To make calls - Try the `Deploy to Heroku` button to deploy the Webapp in under 5 minutes </b>
* <b> To receive calls - All you need is a Twilio provisioned [phone number](https://www.twilio.com/user/account/phone-numbers/incoming) </b>

Deploy this sample app to Heroku now!

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/timbeyers/sip2pstn-simpledial.git)

## What phones can I use?
You can use any IP phone that supports SIP. This includes both hard IP phones from brands like Polycom, Cisco, Obihai, Grandstream, as well as soft phones on laptops and smartphones like Bria or Zoiper.
[Instructions to configure your SIP Endpoint](https://www.twilio.com/docs/api/twilio-sip/pv-sip-registration#configure-your-sip-endpoint)

## Why connect your phone to Twilio?
1. No contracts or monthly charges. You just pay low charges for calls you make or receive.
2. No cost to register your IP phone with Twilio so you can receive calls.
3. You can instantly provision a local telephone number in 50 countries to give you local presence.
4. Build custom call handling logic so you can be reached on the right device at the right time in the right place.

## Features
Twilio requires that phone numbers be in E.164 format. To relax this restriction, this app allows the following more commonly known formats.
Each of the following formats are supported. It is assumed the calls originate from US.

1. E.164 format - i.e. +14157664555
2. US domestic formats - i.e. 14157664555,4157664555
3. Any time 011 exit code from US - i.e. 0114415627220000
4. SIP URI - i.e. sip:username@somedomain.com

The previously mentioned formats can be used when you enter a phone number in your SIP Endpoint (i.e. Bria or Zoiper iPhone app).

Some conversion examples:

From        | To          | National format     |  E.164
------------|-------------|---------------------|-----------------------
USA         | USA         | 415 555 2671        |  +14155552671
UK          | UK          | 0 207183 8750       |  +442071838750
USA         | UK          | 011 44 207183 8750  |  +442071838750

Note: [E.164](https://en.wikipedia.org/wiki/E.164) format is required by Twilio.


### Getting Started

1) Grab latest source
<pre>
git clone git://github.com/timbeyers/sip2pstn-simpledial
</pre>

2) Navigate to folder and create new Heroku Cedar app
<pre>
heroku create
</pre>

3) Deploy to Heroku
<pre>
git push heroku master
</pre>

4) Scale your dynos
<pre>
heroku scale web=1
</pre>

5) Visit the home page of your new Heroku app to see your newly configured app!
<pre>
heroku open
</pre>


### Usage

There exists a route /voice that contains the code you can augment for more advanced call handling.
You can edit `hackpack/app.py`.

This app solves a specific voice use case. If you want a more generic app that let's you play with both Voice and SMS then please see: [Twilio-Hackpack-for-Heroku-and-Flask](https://github.com/RobSpectre/Twilio-Hackpack-for-Heroku-and-Flask)

* The following code is executed when a SIP INVITE is received by Twilio and your SIP Domain Voice URL points to this Webapp
* To learn more about Twilio's Voice Request see [here](https://www.twilio.com/docs/api/twiml/twilio_request)
* The `To:` field in the Twilio request will be of the form: `sip:phonenumber@yoursipdomain.sip.us1.twilio.com`
* The following code extracts the phone number and converts to the format to E.164 if it is in US National format
* The code supports bridging a call from SIP to PSTN as well as from SIP to SIP

```python
# Voice Request URL
# URL params: countryCode=[international country code - ISO alpha2]
@app.route('/voice', methods=['GET', 'POST'])
def voice():
    to = request.values.get('To', None)
    regionCode = request.values.get('countryCode','US')
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
```


## Meta

* No warranty expressed or implied.  Software is as is. Diggity.
* [MIT License](http://www.opensource.org/licenses/mit-license.html)

## Community Contributors
* Hackpack authors provided a great framework to build off of
* Yan Zhou and  Nakul Rathod for adding call handling logic
