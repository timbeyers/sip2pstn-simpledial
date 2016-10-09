# Connect your IP Phone to Twilio and call anywhere in world.
### <5MIN! Just do 1-click deployment to Heroku and configure a Voice URL in the Twilio console 
### With a Twilio provisioned [phone number](https://www.twilio.com/user/account/phone-numbers/incoming) you can place and receive calls anywhere in the world - all you need is an internet connection.





Deploy this sample app to Heroku now!

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/timbeyers/sip2pstn-simpledial.git)

## What phones can I use?
You can use any IP phone that supports SIP. This includes both hard IP phones from brands like Polycom, Cisco, Obihai, Grandstream, as well as soft phones on laptops and smartphones like Bria or Zoiper.
### [Instructions to configure your SIP Endpoint](https://www.twilio.com/docs/api/twilio-sip/pv-sip-registration#configure-your-sip-endpoint)

## Why connect your phone to Twilio?
1. No contracts or monthly charges. You just pay low charges for calls you make or receive.
2. No cost to register your IP phone with Twilio so you can receive calls.
3. You can instantly provision a local telephone number in 50 countries to give you local presence
4. Build custom call handling logic so you can be reached on the right device at the right time in the right place

## Features
Twilio requires that phone numbers be in E.164 format. To relax this restriction, this app allows the following more commonly known formats.
Each of the following formats are supported. It is assumed the calls originate from US.
1. E.164 format - i.e. +14157664555
2. US domestic formats - i.e. 14157664555,4157664555
3. Any time 011 exit code from US - i.e. 0114415627220000
4. SIP URI - i.e. sip:username@somedomain.com

The previously mentioned formats can be used when you enter a phone number in your SIP Endpoint (i.e. Bria or Zoiper iPhone app).

Some conversion examples:

Origination | Termination | National format     |  E.164 (Twilio format)
------------|-------------|---------------------|-----------------------
USA         | USA         |        415 555 2671 |  +14155552671
UK          | UK          |       0 207183 8750 |  +442071838750
USA         | UK          |  011 44 207183 8750 |  +442071838750


## Usage

There exists a route /voice that contains you can augment for more advanced call handling. 
You can edit `hackpack/app.py`.

This app solves a specific voice use case. If you want a more generic app that let's you play with both Voice and SMS then please see: Twilio-Hackpack-for-Heroku-and-Flask

```

## Installation

Step-by-step on how to deploy, configure and develop on this sample app.

### Fastest Deploy

Use Heroku to deploy this hackpack immediately:

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://heroku.com/deploy?template=https://github.com/timbeyers/sip2pstn-simpledial.git)

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


### Development

Getting your local environment setup to work with this app is similarly easy. After you configure your hackpack with the steps above, use this guide to get going locally:

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

Here we recognize members of the Twilio community who worked on this.

* [Timothée Boucher](http://www.timotheeboucher.com/) - idea for production
  branch
* [Oscar](http://labcoder.com/) - Bug fix for user input
* [Zachary
  Woase](http://zacharyvoase.com/) - [Twilio signature
  validation](https://github.com/RobSpectre/Twilio-Hackpack-for-Heroku-and-Flask/pull/7) for production branch.
* [Kevin Burke](http://www.twentymilliseconds.com/) - Better FTU for Twilio
  Client.
* Yan Zhou and  Nakul Rathod for adding call handling logic