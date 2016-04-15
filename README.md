Python Site Generator
=====================

I needed a simple static site generator that would let me write static sites using templates.

How to use it
-------------

1. Make a `_source` directory and a `buildlist.txt` file
2. Write your site in `_source` and use whatever Jinja constructs you want.
3. Add files and directories to `_source`
4. Run `python pysitegen.py`

Example
-------

Site file structure

```
site
|- _source
   |- index.html
   |- base.html
   |- static
      |- image.png
|- pysitegen.py
|- buildlist.txt
```

base.html
```
<html>
  <head>
    <title>{% block title %}Example Site{% endbloc %}</title>
  </head>
  <body>
    {% block body %}{% endblock %}
  </body>
</html>
```

index.html
```
{% extends 'base.html' %}

{% block title %}Hello World!{% endblock %}

{% block body %}
<h1>Hello World!</h1>
<img src="static/image.png" />
<p>I am an example static site</p>
{% endblock %}
```

buildlist.txt
```
index.html
static
```

Then we build the site:
```
$ python pysitegen.py
Rendering index.html...
Copying static/image.png...
```

The site is rendered into `_site` and we have the following directory structure:

```
site
|- _source
   |- index.html
   |- base.html
   |- static
      |- image.png
|- _site
   |- index.html
   |- static
      |- image.png
|- pysitegen.py
|- buildlist.txt
```

And the new `index.html` has the following contents:

```
<html>
  <head>
    <title>Hello World!</title>
  </head>
  <body>
    
<h1>Hello World!</h1>
<img src="static/image.png" />
<p>I am an example static site</p>

  </body>
</html>
```

There you go! Copy the contents of `_site` into a directory and push it to github sites!
