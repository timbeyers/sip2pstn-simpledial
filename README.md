# A sample Twilio app for customers sending SIP to Twilio and wishing to dial to PSTN or to dial a SIP URI.
Now a Twilio customer can simply do 1-click deployment of the app to Heroku and configure a single Voice URL in the console with a Twilio provisioned phone number and a customer can place calls from their favorite SIP Endpoint to anywhere in the world.


[![Build
Status](https://secure.travis-ci.org/RobSpectre/Twilio-Hackpack-for-Heroku-and-Flask.png)]
(http://travis-ci.org/RobSpectre/Twilio-Hackpack-for-Heroku-and-Flask)
[![Coverage Status](https://coveralls.io/repos/RobSpectre/Twilio-Hackpack-for-Heroku-and-Flask/badge.png)]
(https://coveralls.io/r/RobSpectre/Twilio-Hackpack-for-Heroku-and-Flask)


Deploy this sample app to Heroku now!

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://code.hq.twilio.com/tbeyers/simpledial.git)


## Features

Twilio requires that phone numbers be in E.164 format. To relax this restriction, this app allows the following more intuitive and convenient formats.
The following formats for phone-number are supported:
1) E.164 format - i.e. +14157664555
2) US domestic formats - i.e. 14157664555,4157664555
3) Any time 011 exit code from US - i.e. 0114415627220000
4) SIP URI - i.e. username@somedomain.com

The previously mentioned formats can be used when you enter a phone number in your SIP endpoint (i.e. Bria or Zoiper iPhone app).

Some conversion examples
Origination | Termination | National format     |  E.164 (Twilio format)
-----------------------------------------------------------------------
USA         | USA         |        415 555 2671 |  +14155552671
UK          | UK          |       0 207183 8750 |  +442071838750
USA         | UK          |  011 44 207183 8750 |  +442071838750


## Usage

This sample app ships with one ready-to-go endpoints for your Twilio Voice apps.  The one routes /voice containcode you can modify.
You can edit `hackpack/app.py`.

This app solves a specific voice use case. If you want a more generic app to play with both Voice and SMS then please see: Twilio-Hackpack-for-Heroku-and-Flask

```

## Installation

Step-by-step on how to deploy, configure and develop on this sample app.

### Fastest Deploy

Use Heroku to deploy this hackpack immediately:

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/RobSpectre/Twilio-Hackpack-for-Heroku-and-Flask)

### Getting Started 

1) Grab latest source
<pre>
git clone git://github.com/RobSpectre/Twilio-Hackpack-for-Heroku-and-Flask.git 
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


### Configuration

Want to use the built-in Twilio Client template?  Configure your hackpack with
three easy options.


### What you need to do to make calls from your SIP Endpoint (Bria client) to any cell phone or mobile on earth
1) Create an account on Heroku
2) Deploy this app to Heroku (1-click)
 -> Make note of the URL of this app
3) Buy a phone number on the Twilio console
4) Navigate to SIP Domain->Domains->Voice URL and assign Heroku URL
 -> Assign your phone number to the callerId parameter in Heroku URL
 -> You need the /voice route
 i.e. http://sip2pstn-simpledial.herokuapp.com/voice?callerId=+19097428752

Start placing calls!

### Development

Getting your local environment setup to work with this hackpack is similarly easy. After you configure your hackpack with the steps above, use this guide to get going locally:

1) Install the dependencies.

make init

2) Launch local development webserver
<pre>
heroku local
</pre>

3) Open browser to [http://localhost:5000](http://localhost:5000).

4) Tweak away on `hackpack/app.py`.


## Meta 

* No warranty expressed or implied.  Software is as is. Diggity.
* [MIT License](http://www.opensource.org/licenses/mit-license.html)
* Lovingly crafted by [Twilio New
 York](http://www.meetup.com/Twilio/New-York-NY/) 


## Community Contributors

Here we recognize crack members of the Twilio community who worked on this
hackpack.

* [Timothée Boucher](http://www.timotheeboucher.com/) - idea for production
  branch
* [Oscar](http://labcoder.com/) - Bug fix for user input
* [Zachary
  Woase](http://zacharyvoase.com/) - [Twilio signature
  validation](https://github.com/RobSpectre/Twilio-Hackpack-for-Heroku-and-Flask/pull/7) for production branch.
* [Kevin Burke](http://www.twentymilliseconds.com/) - Better FTU for Twilio
  Client.


[![githalytics.com
alpha](https://cruel-carlota.pagodabox.com/33a5ddd61dd29dd933422bca2b3dfa0e
"githalytics.com")](http://githalytics.com/RobSpectre/Twilio-Hackpack-for-Heroku-and-Flask)
