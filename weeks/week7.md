# Custom Color List
This week we learned about the Python concept of a Dictionary.  A dictionary in Python is a collection of names and values that can be used for look-up.  It is a way of storing data, sometimes complex or hard to remember data, using an easy to remember name.

For our project, we stored hard to remember hex codes that represent colors.  If you remember from our HTML lessons, color values on the web and in many programming languages.  Even basic colors like white and black can be represented with hex values:
- white = #ffffff
- black = #000000
- red = #ff0000
- green = #00ff00
- blue = #0000ff

But something more complex might be #68BF3F which is represents this color:

 ![#68BF3F](../images/68bf3f.png)

 So we use a Python dictionary to give complex hex codes names we can remember:

 ```python
 colors = {
  'verylime': '#68BF3F',
  'reallypurple': '#7F3FBF',
  'weirdblue': '#3F7FBF',
  'redred': '#F40A39',
  'mustard': '#F4C50A'
}

screen.bgcolor(colors['verylime'])
```

