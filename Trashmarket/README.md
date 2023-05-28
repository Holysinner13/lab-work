# Trash market

## Specification
TheMarket is a marketing site where you can buy and sell any product in any category. Users can have a conversation about the product with the owner directly through the site in the product section. The seller uploads the details of the products and edits them at any time. Each user has a secure login password to identify themselves as a user.

Possible modules required for correct operation:
asgiref==3.6.0
Django==4.2.1
gunicorn==20.1.0
Pillow==9.5.0
psycopg2-binary==2.9.6
sqlparse==0.4.4
tzdata==2023.3
whitenoise==6.4.0

Вы можете установить все зависимости, выполнив следующую команду: `pip install -r requirements.txt`

At the end of the bot, you can use the following applications:
+ <u> chat </u> - chat app between users
+ <u> items </u> - product handling application
+ <u> mainpage </u> - app to display user ads
+ <u> system </u> - the main application for working with registrations