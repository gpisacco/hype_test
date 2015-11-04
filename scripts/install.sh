#!/bin/bash
cd /var/data/hype
# virtualenv creation
mkdir local
cd local
virtualenv env
source env/bin/activate
pip install -r ../requirements.txt

cd ../web
bower install

# let www-data user access the site
sudo chown -R  www-data /var/data/hype

cd ../scripts

#postgres production configuration
sudo -u postgres psql -c "CREATE DATABASE hype_prod;"
sudo -u postgres psql -c "CREATE USER hype WITH PASSWORD 'passw0rd';"
sudo -u postgres psql -d hype_prod -c "CREATE SCHEMA lbs2 AUTHORIZATION hype;"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE hype_prod TO hype;"
sudo -u postgres psql -d hype_prod -c "ALTER DEFAULT PRIVILEGES IN SCHEMA lbs2 GRANT ALL PRIVILEGES ON tables TO hype;"
sudo -u postgres psql -d hype_prod -a -f schema.sql
sudo -u postgres psql -d hype_prod -c " GRANT SELECT, USAGE  ON ALL SEQUENCES IN SCHEMA lbs2 TO hype;"

#postgres test configuration
sudo -u postgres dropdb hype_test
sudo -u postgres psql -c "CREATE DATABASE hype_test;"
sudo -u postgres psql -c "CREATE USER hype_test WITH PASSWORD 'passw0rd';"
sudo -u postgres psql -d hype_test -c "CREATE SCHEMA lbs2 AUTHORIZATION hype_test;"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE hype_test TO hype_test;"
sudo -u postgres psql -d hype_test -c "ALTER DEFAULT PRIVILEGES IN SCHEMA lbs2 GRANT ALL PRIVILEGES ON tables TO hype_test;"
sudo -u postgres psql -d hype_test -a -f scripts/schema.sql
sudo -u postgres psql -d hype_test -c " GRANT SELECT, USAGE  ON ALL SEQUENCES IN SCHEMA lbs2 TO hype_test;"

# nginx config
sudo cp hype /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default

# nginx config
sudo cp hype.ini /etc/uwsgi/apps-enabled/
sleep 10
sudo service postgresql start
sudo service uwsgi start
sudo service nginx start
tail -f /var/log/lastlog #ugly way to avoid configuring supervidord
