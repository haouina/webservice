## MISE EN PLACE DE WEBSERVICE

* Téléchargement de web.py afin de mettre en place le webservice RestFul:
  -> wget http://webpy.org/static/web.py-0.37.tar.gz

* Décompresser le repertoire: 
  -> tar -xvzf web.py-0.37.tar.gz

* Accès au repetoire
  -> cd web.py-0.37

* Installation de web.py
  -> python setup.py install

* Une fois installée il est possible de l'importer. 

* Installation de Pytz

  -> easy_install pytz

* Création de fichier config.py qui contient le timezone par défaut

* Une fois l'application est codée alors il faut la packager
  
  -> touch setup.py

      #!/usr/bin/python2.7

      from setuptools import setup

      setup(
       name='webservice', version='0.3', scripts=['webservice.py','config.py']
      )
   

  -> python setup.py sdist (Packager l'application)

  -> tar -xvzf webservice-0.3.tar.gz

  -> cd webservice-0.3 && python setup.py install

  -> python setup.py register

  -> python setup.py sdist upload

* Maintenant l'appilcation peut être installée depuis n'importe quel machine:
  
  -> pip install webservice

* Une fois installée elle peut être appeler avec webservice.py 
 
* Le répetoire dist contient l'application packagée

* J'ai fait un test de webservice en m'inspirant d'un article sur le Net: https://fijiaaron.wordpress.com/2011/09/15/testing-rest-web-services-with-python/ 
  
  et le nom de script est "test.py" 



## DEPLOIEMENT AVEC PUPPET

* J'ai mis les fichiers site.pp et init.pp concernant l'automatisation avec puppet

      class webservice {

          # execute 'Yum update'
          exec { 'yum-update':                # exec resource named 'yum-update'
                 command => '/usr/bin/yum -y -q update'  # command this resource will run
          }

          # install python package
          package { 'python':
                    require => Exec['yum-update'],        # require 'yum-update' before installing
                    ensure => installed,
          }

          package { 'epel-release':
                    require => Exec['yum-update'],        # require 'yum-update' before installing
                    ensure => installed,
          }

          package { 'python-setuptools':
                    require => Exec['yum-update'],        # require 'yum-update' before installing
                    ensure => installed,
          }

          exec { 'install epel':
                 cwd => "/tmp/", 
                 command => "rpm -ivh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm",
                 path => ['/bin'],  
          }

          package { 'python-pip':
                    require => Exec['yum-update'],        # require 'yum-update' before installing
                    ensure => installed,
          }


          # Copy the Web.py to /tmp
          file { '/tmp/web.py-0.37.tar.gz':
                 ensure => present,
                 source => "puppet:///modules/webservice/web.py-0.37.tar.gz"
          }

          # Extract the archive
          exec { 'extract':
                 cwd => "/tmp",
                 command => "tar -xvzf web.py-0.37.tar.gz",
                 require => File['/tmp/web.py-0.37.tar.gz'],
                 path => ['/bin'],
          }

          # Install web.py
          exec { 'install web.py':
                 cwd => "/tmp/web.py-0.37",
                 command => "python setup.py install",
                 path => ['/usr/bin'],
          }

          exec { 'install pytz':
                 cwd => "/tmp/",
                 command => "easy_install pytz",
                 path => ['/usr/bin'],
          }

          # Executing script
          exec { 'execute script':
                 cwd => "/tmp",
                 command => "pip install webservice",
                 path => ['/usr/bin/'],
         }

        }

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

  -> nano PUPPET_DIR_MODULE/spec/classes/python_spec.rb (Source https://nikokiuru.com/2014/10/create-puppet-module-test-case-less-than-5-minutes/)
     (modification) https://engineering.opendns.com/2014/11/13/testing-puppet-modules-vagrant-serverspec/   
  
  -> Un exemple de Test:

      require 'spec_helper'

        describe 'webservice', :type => 'class' do
        context 'install python-pip' do
            it { should be_installed }
        end
  
        context 'install python' do
            it { should be_installed }
        end
  
        context 'install python-setuptools' do
            it { should be_installed }
        end
      end

  
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
