# Url Shortener

## Basic Shortener
-   Single page.
-   Input any URL, output a generated shortned version of the URL.
-   URL pattern : domain.com/go/SHORTNEDURL
-   Uses SQLite3.

# How to use
## Customisation 
In ./URLShortener/settings.py:

- SHORT_URL_LENGHT: how short you want your URL to be. *NOTE:* Not checking if the URL is generated twice.
- DOMAIN : replaces domain.com in the pattern, must include the port if not standard, 'localhost:8000' is default.


## Instalation
One line installers.

### Docker
```bash 
docker build -t urlshortener . \
  && touch db.sqlite3 \
  && docker run -dp 8000:8000 -v $(pwd)/db.sqlite3:/code/db.sqlite3 urlshortener
```
    
    
    
    
### virtualenv

```bash
virtualenv e && source e/bin/activate \
 && pip install -r requirements.txt \
 && python manage.py makemigrations \
 && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
```

