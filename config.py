

import os

_basedir = os.path.abspath(os.path.dirname(__file__))

# LOG
LOGFILE = os.path.join(_basedir, 'logs/flask.log')


# MYSQL
MYSQLHOST     = '127.0.0.1'
MYSQLPORT     = 3306
MYSQLDB       = 'actual16'
MYSQLUSER     = 'root'
MYSQLPASS     = '123456'
MYSQLCHARSET  = 'utf8'


# MAIL
MAIL_SERVER   = 'smtp.163.com'
MAIL_PORT     = 25
MAIL_USE_TLS  = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME', '')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', '')