# GNU MediaGoblin for YunoHost

**GNU MediaGoblin**: http://mediagoblin.org/

**YunoHost**: https://yunohost.org/


This application is in development and rely on patched sources - e.g. for
the HTTP Authentication plugin to work properly. Use with caution, but feel
free to purpose ameliorations and report bugs!

## Requirements

It now requires *systemd* and at least Debian Jessie with the current testing
version of YunoHost.

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

## TODO

* Add backup/restore scripts
* ...
