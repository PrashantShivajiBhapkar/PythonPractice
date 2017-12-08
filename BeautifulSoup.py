from bs4 import BeautifulSoup
import urllib3

url = 'http://web.ics.purdue.edu/~gchopra/class/public/pages/webdesign/05_simple.html'
http = urllib3.PoolManager()
page = http.request('GET', url)
print(page.status)
soup = BeautifulSoup(page.data, 'lxml')
# Various Other Parsers:
# "html.parser", "lxml", "lxml-xml"-same as "xml", "html5lib"
# "lxlm" - best and fastest

print(type(soup))
print(soup.prettify())

print(soup.title)
print(soup.title.name)

print(soup.title.string)  # Returns obj of type <class 'bs4.element.NavigableString'>
# Can be converted into UNICODE
# unistr = unicode(soup.title.string)
# Can't edit BUT replace
soup.title.string.replace_with('Replaced String')
print(soup.title.string)
# To use this string outside of BeautifulSoup ALWAYS convert it into UNICODE,
# ELSE it will carry around a reference to the entire Beautiful Soup parse tree,
# even when you’re done using Beautiful Soup. This is a big waste of memory.
print(type(soup.title.string))

print(soup.title.parent)
print(soup.title.parent.name)  # Returns str obj
print(soup.p)  # Returns the firsl p tag
print(soup.a)
# Access attribut of a tag as a dict
print(soup.a['href'])

# Acccess the dict for a
print(soup.a.attrs)
# {'href': 'http://www.yahoo.com/'}

print(soup.find_all('a'))
print(type(soup.find_all('a')))

# Extract all URLs from the pages
for link in soup.find_all('a'):
    print(link.get('href'))  # returns str obj

# Extract all the text from the pages
print(soup.get_text())  # Returns str obj

print(soup.name)

# To get the contents between certain tags
print(soup.head)
print(soup.head.contents)

# Get child tags of some parent tag
print(soup.head)
print(soup.head.children)  # Returns list_iterator object of child tags
# NOTE: 'Children' goes only till ONE LEVEL
for child in soup.head.children:
    print(child)

# GOING DOWN
# Get chiildren at all levels
print(soup.head)
print(soup.head.descendants)  # Returns generator object descendants
for child in soup.head.descendants:
    print(child)  # Prints all the children recursively

print(len(list(soup.head.children)))
print(len(list(soup.head.descendants)))

# Get all the strings from the page WITHOU CLEANING white spaces/tabs/multiple new lines
for string in soup.strings:
    print(string)

# Get all the strings after cleaning
for string in soup.stripped_strings:
    print(string)  # Returns str obj
# strings consisting entirely of whitespace are ignored,
# and whitespace at the beginning and end of strings is removed.

# GOING UP
# Access parent
print(soup.head)
print(soup.title.parent)

# Parent of HTML tag is BeautiFul Obj itself
print(soup.html.parent)  # Prints the entire BeautifulSoup object
print(type(soup.html.parent))  # <class 'bs4.BeautifulSoup'>
print(type(soup))  # Equivalent to  print(type(soup.html.parent))
print(soup.parent)  # No parent of soup obj

# Recursively print all parents
print(soup.a)
for parent in soup.a.parents:  # generator object soup.a.parents
    if parent is None:
        print(parent)
    else:
        print(parent.name)

# GOING SIDEWAYS
# Siblings -> have same parent
siblingSoup = BeautifulSoup('<a><b>text1</b><c>text2</c></b></a>')
print(siblingSoup.prettify())
print(siblingSoup.b.next_sibling)
print(siblingSoup.c.previous_sibling)

# Iterate over previous or next siblings
print(soup.a.next_siblings)  # <generator object next_siblings
# for nextSibling in soup.a.next_siblings:
#     print(repr(nextSibling))

# GOING BACK AND FORTH
print(soup.a)
print(soup.a.next_element)

# Go throu next elements recursively
for element in soup.a.next_elements:
    print(repr(element))
# ---------------------------------------------------------------------------

# METHODS:
# Resume from KINDS OF FILTERS Onwards
