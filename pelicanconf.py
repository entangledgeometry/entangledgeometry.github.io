AUTHOR = 'manish kumar'
SITENAME = 'Entangled Geometry'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'en'
# Path to my custom theme
THEME = 'theme'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
# Tell Pelican to copy the images folder to output/images/
STATIC_PATHS = ['images']

# Sidebar navigation links
# (Add any future sections or pages right here)
MENUITEMS = (
    ('Home', '/'),
    ('Math', '/category/math.html'),
    ('Archives', '/archives.html'),
)
