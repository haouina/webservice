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

# Executing script
exec { 'execute script':
        cwd => "/tmp",
        command => "pip install webservice",
        path => ['/usr/bin/'],
    }

}
 
