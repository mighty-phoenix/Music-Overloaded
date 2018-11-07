#TO INSTALL REQUIREMENTS
sudo -H pip3 install -r $(pwd)/requirements.txt
#TO REPLACE LOCAL SERVER SETTINGS
echo 'Enter name to give to MySQL Database:'
read name
echo 'Enter your MySQL username:'
read user
echo -n 'Enter your MySQL password:'
read -s password
sed -i "s|db|${name}|g" $(pwd)/website/settings.py
sed -i "s|root|${user}|g" $(pwd)/website/settings.py
sed -i "s|blossom|${password}|g" $(pwd)/website/settings.py
sudo python3 $(pwd)/manage.py makemigrations
sudo python3 $(pwd)/manage.py migrate
sudo python3 $(pwd)/manage.py runserver




