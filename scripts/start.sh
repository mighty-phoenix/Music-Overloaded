#TO INSTALL REQUIREMENTS
sudo apt remove python-django
sudo pip3 uninstall django
sudo -H pip3 install -r $(pwd)/requirements.txt
#TO REPLACE LOCAL SERVER SETTINGS
echo 'Enter name of MySQL Database:'
read name
echo 'Enter your MySQL username:'
read user
echo -n 'Enter your MySQL password:'
read -s password
sed -i "s|dbal|${name}|g" $(pwd)/website/settings.py
sed -i "s|rootlove|${user}|g" $(pwd)/website/settings.py
sed -i "s|blossom|${password}|g" $(pwd)/website/settings.py
python3 $(pwd)/manage.py makemigrations
python3 $(pwd)/manage.py migrate
python3 $(pwd)/manage.py runserver




