sfl-generic-multisite-http
==========================

Dependencies
************


Shinken Modules
~~~~~~~~~~~~~~~

Plugins
~~~~~~~

check_http
----------

This pack will create services which need the following plugin:

::

  /usr/lib/nagios/plugins/check_http

or

::

  /usr/lib64/nagios/plugins/check_http


Network
~~~~~~~

This pack will create services which need the following protocol :

* TCP 80 and 443 from Poller to monitored client

Installation
************

Copy the pack folder in the packs folder defined in shinken.cfg (`cfg_dir=packs`)


How to use it
*************


Settings
~~~~~~~~

This is the list of settings which can be redefined in the host definition

_MULTISITE_USER
---------------

:type:              string
:description:       The Multisite admin user login. Default: nagiosadmin


_MULTISITE_PASSWORD
-------------------

:type:              string
:description:       The Multisite password admin login. Default: nagiosadmin


_MULTISITE_URL
-------------------

:type:              string
:description:       The Multisite URL. Default: /check_mk

_MULTISITEWARN
--------------

:type:              Integer
:description:       Warning threshold. Default: 3

_MULTISITECRIT
--------------

:type:              Integer
:description:       Warning threshold. Default: 5