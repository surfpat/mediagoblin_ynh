GNU MediaGoblin for YunoHost
============================

**GNU MediaGoblin**: http://mediagoblin.org/

**YunoHost**: https://yunohost.org/


This application is in development and rely on patched sources - e.g. for
the HTTP Authentication plugin to work properly. Use with caution, but feel
free to purpose ameliorations and report bugs!


Features
--------

The supported and activated Media types are:
  * **image**
  * **video**
  * **audio**
  * **pdf** - if you want support for converting libreoffice supported
  documents as well, you will have to install *unoconv* and *libreoffice*.

The transcoding is done in a separate thread thanks to Celery.

The authentication is transparently managed by SSOwat which is made
available in GNU MediaGoblin by the *httpauth* beta plugin and some patches
to the source code.
