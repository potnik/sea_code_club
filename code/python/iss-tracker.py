#!/bin/python3

import json
import turtle
import urllib.request
import time

astros_url = 'http://api.open-notify.org/astros.json'
iss_now_url = 'http://api.open-notify.org/iss-now.json'
iss_pass_url = 'http://api.open-notify.org/iss-pass.json?lat=45&lon=-93.3'

def api_call(url):
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    return result

# Who's in space now?
result = api_call(astros_url)
print('People in space: ', result['number'])
print()
people = result['people']
for p in people:
  print(p['name'], ' in ', p['craft'])
print()

# ISS Now
result = api_call(iss_now_url)
location = result['iss_position']
lat = float(location['latitude'])
long = float(location['longitude'])

#Map
screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('../../images/map.gif')
screen.register_shape('../../images/space-station.gif')

#ISS
iss = turtle.Turtle()
iss.speed(0)
iss.shape('../../images/space-station.gif')
iss.penup()
iss.pencolor('yellow')
iss.goto(long, lat)

#Home
home_long = -93.329554
home_lat = 45.001354

home = turtle.Turtle()
home.hideturtle()
home.color('yellow')
home.penup()
home.goto(home_long, home_lat)
home.pendown()
home.dot(5)

result = api_call(iss_pass_url)
over = result['response'][1]['risetime']
style = ('Arial', 4, 'bold')
home.write(time.ctime(over), font=style)

iss.pendown()
i=1
while True:
  result = api_call(iss_now_url)
  location = result['iss_position']
  lat = float(location['latitude'])
  long = float(location['longitude'])
  iss.goto(long, lat)
  print(i, time.ctime(), 'latitude: ', lat, ' longitude: ', long )
  time.sleep(60)
  i=i+1
  