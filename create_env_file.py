import argparse
import os
from lib.templatetags.custom_filters import nz

parser = argparse.ArgumentParser()
parser.add_argument('--app-id', help='application id issued by AAD')
parser.add_argument('--secret-key', help='')
parser.add_argument('--google-api-key', help='')
parser.add_argument('--dev-db-host', help='')
parser.add_argument('--dev-db-port', help='')
parser.add_argument('--dev-db-name', help='')
parser.add_argument('--dev-db-user', help='')
parser.add_argument('--dev-db-password', help='')
parser.add_argument('--prod-db-host', help='')
parser.add_argument('--prod-db-port', help='')
parser.add_argument('--prod-db-name', help='')
parser.add_argument('--prod-db-user', help='')
parser.add_argument('--prod-db-password', help='')
parser.add_argument('--email-host', help='')
parser.add_argument('--email-user', help='')
parser.add_argument('--email-password', help='')
parser.add_argument('--email-port', help='')
parser.add_argument('--email-use-tls', help='')
args = parser.parse_args()

print(args.dev_db_host)
new_file = os.path.join(".env")
with open(new_file, 'w') as write_file:
    write_file.write("SECRET_KEY = {}\n".format(nz(args.secret_key, "")))
    write_file.write("GOOGLE_API_KEY = {}\n".format(nz(args.google_api_key, "")))
    write_file.write("\n")
    write_file.write("DEV_DB_HOST = {}\n".format(nz(args.dev_db_host, "")))
    write_file.write("DEV_DB_PORT = {}\n".format(nz(args.dev_db_port, "")))
    write_file.write("DEV_DB_NAME = {}\n".format(nz(args.dev_db_name, "")))
    write_file.write("DEV_DB_USER = {}\n".format(nz(args.dev_db_user, "")))
    write_file.write("DEV_DB_PASSWORD = {}\n".format(nz(args.dev_db_password, "")))
    write_file.write("\n")
    write_file.write("PROD_DB_HOST = {}\n".format(nz(args.prod_db_host, "")))
    write_file.write("PROD_DB_PORT = {}\n".format(nz(args.prod_db_port, "")))
    write_file.write("PROD_DB_NAME = {}\n".format(nz(args.prod_db_name, "")))
    write_file.write("PROD_DB_USER = {}\n".format(nz(args.prod_db_user, "")))
    write_file.write("PROD_DB_PASSWORD = {}\n".format(nz(args.prod_db_password, "")))
    write_file.write("\n")
    write_file.write("EMAIL_HOST = {}\n".format(nz(args.email_host, "")))
    write_file.write("EMAIL_HOST_USER = {}\n".format(nz(args.email_user, "")))
    write_file.write("EMAIL_HOST_PASSWORD = {}\n".format(nz(args.email_password, "")))
    write_file.write("EMAIL_PORT = {}\n".format(nz(args.email_port, "")))
    write_file.write("EMAIL_USE_TLS = {}\n".format(nz(args.email_use_tls, "")))
    write_file.write("\n")

