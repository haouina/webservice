## MISE EN PLACE DE WEBSERVICE

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

  -> easy_install pytz

* Création de fichier config.py qui contient le timezone par défaut

* Une fois l'application est codée alors il faut la packager
  
  -> touch setup.py

  -> python setup.py sdist (Packager l'application)

  -> tar -xvzf webservice-0.1.tar.gz

  -> cd webservice-0.1 && python setup.py install

  -> python setup.py register

  -> python setup.py sdist upload

* Maintenant l'appilcation peut être installée depuis n'importe quel machine:
  
  -> pip install webservice

* Une fois installée elle peut être appeler avec webservice.py 
 
* Le répetoire dist contient l'application packagée


## DEPLOIEMENT AVEC PUPPET

* J'ai mis les fichiers site.pp et init.pp concernant l'automatisation avec puppet

* J'ai fait un test unitaire pour puppet "python_spec.rb" je suis entrain de me former à propos des tests unitaires et d'intégration
  
  -> nano Gemfile

      source 'https://rubygems.org'
      puppetversion = ENV.key?('PUPPET_VERSION') ? "= #{ENV['PUPPET_VERSION']}" : ['>= 2.7']
      gem 'puppet', puppetversion
      gem 'puppetlabs_spec_helper', '>= 0.1.0'
      gem 'rspec', '>=3.1.0'
      gem 'rspec-puppet'
  
  -> bundle install

  -> rspec-puppet-init
  
  -> echo "require 'puppetlabs_spec_helper/rake_tasks'" >> Rakefile

  -> nano PUPPET_DIR_MODULE/spec/classes/python_spec.rb

  -> bundle exec rake spec

* J'ai fait aussi un "smoke test" via test.sh
 

## ENVIRONNEMENT DE TEST AVEC DOCKER

* J'ai créer un fichier dockerfile afin de préparer l'environnement de Test et je l'ai mis sur github.

  -> touch dockerfile

      FROM appcontainers/centos:6

      RUN yum update -y
      RUN yum install -y python python-setuptools python-pip
      RUN yum install -y wget
      RUN wget http://webpy.org/static/web.py-0.37.tar.gz
      RUN yum install -y tar.x86_64
      RUN tar xvzf web.py-0.37.tar.gz
      RUN cd web.py-0.37 && python setup.py install
      RUN easy_install pytz
      RUN pip install webservice

      EXPOSE  8080

      CMD ["/usr/bin/webservice.py"]

 
  -> docker build -t appcontainers/centos:6 .

  -> docker run -t -i -p 14000:8080 appcontainers/centos:6 (Exposer le port 8080 et le rediriger vers le port 14000 de Host)
