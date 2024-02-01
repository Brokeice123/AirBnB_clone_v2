# Puppet automation for deploying of web_static

# Install nginx
package { 'nginx':
  ensure => 'present',
}

# Define directory structure
file { ['/data', '/data/web_static', '/data/web_static/releases', '/data/web_static/shared', '/data/web_static/releases/test']:
  ensure => directory,
}

# Create fake HTML file
file { ['/data/web_static/releases/test/index.html']:
  ensure  => file,
  content => 'Hello World!',
}

# Create symbolic link
file { ['/data/web_static/current']:
  ensure  => link,
  target  => '/data/web_static/releases/test',
  require => File['/data/web_static/releases/test'],
}

# Ownership

file { ['/data/']:
  owner     => 'ubuntu',
  group     => 'ubuntu',
  recursive => true,
}

# Update Nginx configuration
file { ['/etc/nginx/sites-available/default']:
  ensure  => file,
  content => '
    server {
        listen 80;
        listen [::]:80 default_server;
        add_header X-Served-By $hostname;
        root   /var/www/html;
        index  index.html index.htm index.nginx-debian.html;

        location /hbnb_static {
            alias /data/web_static/current;
            index index.html index.htm;
        }

        location /redirect_me {
            return 301 https://www.github.com/Shadkoech/;
        }

        error_page 404 /404.html;
        location /404 {
          root /etc/nginx/html;
          internal;
        }
    }
  ',
  require => Package['nginx'],
}

# Restart Nginx
service { 'nginx':
  ensure    => running,
  subscribe => File['/etc/nginx/sites-available/default'],
}
