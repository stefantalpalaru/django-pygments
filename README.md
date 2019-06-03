## description

django-pygments is a Django app that provides a template tag and two filters for doing syntax highlighting with [Pygments][1].

## dependencies

- [Pygments][1]

## installation

- add django\_pygments to your project directory and to INSTALLED\_APPS in your settings.py
- if you want to see the integrated demo page, add a urls.py entry and copy/link the media files in the proper dir

## usage

- enclose your code snippet in a pre tag with the non-standard "lang" attribute set to a supported language like this:
```html
<pre lang="python">....</pre>
```
- see the view and demo template for examples on how to use the "pygmentify" and "pygmentify\_inline" filters (the later is rather useful for RSS feeds) or the "pygment" tag
- While using the "pygment" template tag, you can pass keyword arguments that you would pass to Pygments HtmlFormatter class constructor by passing them as with keyword arguments along with the pygment tag. Look at demo template for examples. There is one caveat with this feature still. You can only pass Python values as argument values (like Strings wrapped within quotes or True or False boolean values, etc.). It doesn't support Django template/context variables as arguments yet.

## notes

- the custom HTML formatter class displays each line as an ordered list element, thus implementing line numbering without interfering with copy/pasting
- to see a list of supported languages, look at the "lexer\_names" variable in utils.py

## license

3-clause BSD

## credits

- main author - Ștefan Talpalaru <stefantalpalaru@yahoo.com>
- site - https://github.com/stefantalpalaru/django-pygments


[1]: http://pygments.org/

