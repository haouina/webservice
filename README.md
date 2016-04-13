* Téléchargement de web.py afin de mettre en place le webservice RestFul:
  -> wget http://webpy.org/static/web.py-0.37.tar.gz

* Décompresser le repertoire: 
  -> tar -xvzf web.py-0.37.tar.gz

* Accès au repetoire
  -> cd web.py-0.37

* Installation de web.py
  -> python setup.py install

* Une fois installée il est possible de l'importer et coder le webservice

* Installation de Pytz

  -> easy_install --upgrade pytz

* Création de fichier config.py qui contient le timezone par défaut

* Une fois l'application est codée alors il faut la packager
  
  -> touch setup.py
  -> python setup.py sdist
  -> tar -xvzf webservice-0.1.tar.gz
  -> cd webservice-0.1 && python setup.py install
  -> python setup.py register
  -> python setup.py sdist upload

* Maintenant l'appilcation peut être installée depuis n'importe quel machine:
  
  -> pip install webservice
 
