# Sea Code Club
## Notes and Code for Code Club at School of Engineering and Arts

### Helpful Links

[Trinket.io](https://trinket.io)

[Code Club Projects](https://projects.raspberrypi.org/en/codeclub?utm_source=code-club-projects-site)

[Code Club Docs](https://drive.google.com/drive/folders/10xL0Nd-Lq8ghj1qSG4T40s97sVIBI_Tb)

[W3Schools - HTML&CSS Resources](https://www.w3schools.com/)

[HTML Colors](https://www.w3schools.com/colors/colors_names.asp)

### Week 1
Thanks for coming to our first Code Club meeting.  I started Code Club to give students a chance to move beyond Scratch and other graphical coding environments.  In Code Club, you will be typing code -- so much typing...

This week we got set up with our Trinket.io accounts and started to look at basic HTML tags.  You were given an HTML Cheatsheet as a shortcut to learning the different tags.  If you lost yours, or want an electronic copy, you can find it and other resources in the Code Club Files folder.  Find the link to this in the group welcome message.

The most important takeaways from this week are about the nature of tags and the structure of an HTML document:
Most every HTML tag has an opening tag and a closing tag: `<html> </html>` . The one exception we looked is the line break `<br>` tag.
Tags are nested and must appear in a certain order:

```html
<html>
    <head>
        <title> Title </title>
    </head>
    <body>
        <p>Body Text</p>
    </body>
</html>
```

Everything must go between the `<html> </html>` tags and everything you want to display on your page must go between the `<body> </body>` tags

### Week 2

For week 2 we spent more time walking through the [Happy Birthday](https://projects.raspberrypi.org/en/projects/happy-birthday) lesson.
We spent a lot of time reviewing basic tags and page structure.  By now, you should have a basic webpage.  It is important that you understand the basic web tags so we can move forward in coming weeks:
 ```html
 <html></html>
 <head></head>
 <title></title>
 <body></body>
 <h1></h1>
 <p></p>
 <b></b>
 <i></i>
 <u></u>
 <br>
 ```
Towards the end of the session, we started to look at adding style to our page with CSS.
 ```css
 body {
    background: white;
  }
  p {
    color: black;  
  }
 ```
 Remember:  Coding is very precise.  Tags need to be nested and closed properly.  CSS is particular about punctuation.