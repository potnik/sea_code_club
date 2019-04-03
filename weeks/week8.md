# Week 8 - ISS Tracker
This week we covered a few new concepts while building a basic tracker for the International Space Station (ISS).  These new concepts are spelled out in our imports section:
```python
import turtle
import urllib.request
import json
import time
```
First, we used the python turtle package in a different way than the turtle race of weeks 4 and 5.

For this exercise, we used the turtle.Screen() function to create our map 
```python
#Map
screen = turtle.Screen()

# this next line sets the size and is based on the map graphic we are using
screen.setup(720, 360)

# now we set the coordinates for longitude and latitude
screen.setworldcoordinates(-180, -90, 180, 90)

# the map graphic (from NASA!) we are using
screen.bgpic('map.gif')

# finally, we need to tell python we are using the iss.gif graphic
screen.register_shape('iss.gif')
```
The next two things we worked with for the first time are Web APIs and JSON messages.  These are two very important concepts in programming.

API stands for **Application Programming Interface**. 
An API can take many forms and it allows a developer to interact with an appliction or computer operating system (OS). 

Web APIs are a specific type.  They use a web URL to communicate with the other system and return information.  In our program, we are calling three separate APIs to get information about the ISS.

In my version of the code, I broke these three out in separate variables so it was easier to understand what information they return:
```python
astros_url = 'http://api.open-notify.org/astros.json'
iss_now_url = 'http://api.open-notify.org/iss-now.json'
iss_pass_url = 'http://api.open-notify.org/iss-pass.json'

# the iss_pass_url will also need "query parameters" in the form of longitude and latitude.  We will pass these with variables, but the resulting url will be http://api-open-notify.org/iss-pass.json?lat=45&lon=-93.3
```
When we call the first url, it returns a JSON message listing all the astronauts currently in space:
```JSON
{"message": "success",
 "number": 6, 
 "people": [
   {"craft": "ISS", "name": "Oleg Kononenko"},
   {"craft": "ISS", "name": "David Saint-Jacques"}, 
   {"craft": "ISS", "name": "Anne McClain"}, 
   {"craft": "ISS", "name": "Alexey Ovchinin"}, 
   {"craft": "ISS", "name": "Nick Hague"}, 
   {"craft": "ISS", "name": "Christina Koch"}
  ]
}
```
We can **parse** this message to get the information we want out of it:
```python
# define the url
url = 'http://api.open-notify.org/astros.json'

# call they url using the request function of the urllib module
response = urllib.request.urlopen(url)

# use the json module to load the response into a python dictionary called result so we can parse out the attribute values we want
result = json.loads(response.read())
```
Once we load the API response into the result variable, we can pick out (parse) just the things we want:
```python
# here we are getting the value for 'number' from the json response
print('People in Space: ', result['number'])

# there is more than one person in the people list, so we have to go through it one at a time (iterate)
people = result['people']

for p in people:
  print(p['name'], ' in ', p['craft'])
```
Remember Python Dictionaries from our Color Picker?  That is what we are doing with the JSON response--turning it into a Python Dictionary and then listing the values we want.

Finally, we use the **time** module to convert the time we are given in number format to a time and date we can understand:
```python
import time
time.ctime(1554255640)
'Tue Apr 02 20:40:40 2019'
```