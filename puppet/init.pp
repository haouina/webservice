# webservice class install the webservice.py

class webservice {

# install python packages
package { 'python':
  ensure => installed,
}

package { 'epel-release':
  ensure => installed,
}

package { 'python-setuptools':
  ensure => installed,
}

exec { 'install epel':
  command => 'rpm -ivh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm',
  path    => ['/bin'],
}

package { 'python-pip':
  ensure => installed,
}


# Copy the Web.py to /tmp
file { '/tmp/web.py-0.37.tar.gz':
  ensure => present,
  source => 'puppet:///modules/webservice/web.py-0.37.tar.gz'
}

# Extract the archive
exec { 'extract':
  cwd     => '/tmp',
  command => 'tar -xvzf web.py-0.37.tar.gz',
  require => File['/tmp/web.py-0.37.tar.gz'],
  path    => ['/bin'],
}

# Install web.py
exec { 'install web.py':
  cwd     => '/tmp/web.py-0.37',
  command => 'python setup.py install',
  path    => ['/usr/bin'],
}

exec { 'install pytz':
  cwd     => '/tmp/',
  command => 'easy_install pytz',
  path    => ['/usr/bin'],
}

# Executing script
exec { 'execute script':
  cwd     => '/tmp',
  command => 'pip install webservice',
  path    => ['/usr/bin/'],
}
}

