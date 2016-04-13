#!/bin/bash

DIR='/etc/puppetlabs/code/modules/webservice'

puppet parser validate $DIR/manifests
puppet apply --noop --modulepath $DIR $DIR/manifests/init.pp
