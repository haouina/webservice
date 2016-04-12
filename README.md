# Téléchargement de web.py afin de mettre en place le webservice RestFul:

wget http://webpy.org/static/web.py-0.37.tar.gz

# Décompresser le repertoire:

tar -xvzf web.py-0.37.tar.gz

# Accès au repetoire 

cd web.py-0.37

# Installation de web.py

python setup.py install


* Une fois installée il est possible de l'importer et coder le webservice  

# Installation de Pytz

easy_install --upgrade pytz

# Création de fichier config.py qui contient le timezone par défaut

# La commande web est une alias qui permet d'exécuter le script webservice.py

alias web='python /root/scripts-python/webservice.py'

