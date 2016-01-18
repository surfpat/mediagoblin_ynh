# GNU MediaGoblin for YunoHost

[MediaGoblin](http://mediagoblin.org/) is a free software media publishing platform
that anyone can run.

## Requirements

It now requires at least Debian Jessie with *systemd* and the current testing
version of [YunoHost](https://yunohost.org/) (>= 2.3.6).

## Features

The supported and activated Media types are:
  * **image**
  * **video**
  * **audio**
  * **pdf** - if you want support for converting libreoffice supported
    documents as well, you will have to install *unoconv* and *libreoffice*.

The transcoding is done in a separate thread thanks to Celery.

The authentication is transparently managed by SSOwat which is made
available in GNU MediaGoblin by the *ynhauth* beta plugin and some patches
to the source code.

It is also possible to enable registration using *basic_auth* plugin too which
will rely on the MediaGoblin internal authentication - and not YunoHost one.
Both authentication mechanism will be available in that case. Please note
that YunoHost users will have to log in through the SSO and not the ediaGoblin
login page.

## Installation

From the command-line:

    $ sudo yunohost app install https://github.com/jeromelebleu/mediagoblin_ynh

From the Web administration:
  * Go to *Applications*
  * Click on *Install*
  * Scroll to the bottom of the page and put https://github.com/jeromelebleu/mediagoblin_ynh
    under **Install custom app**

## TODO

* Add backup/restore scripts
