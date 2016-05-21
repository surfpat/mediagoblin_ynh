#
# Common variables
#

app="mediagoblin"

# MediaGoblin version
VERSION=0.9.0

# Package name for MediaGoblin dependencies
DEPS_PKG_NAME="mediagoblin-deps"

#
# Common helpers
#

# Source YunoHost helpers
. /usr/share/yunohost/helpers

# Execute a command as another user (mediagoblin by default)
# usage: exec_cmd cmd [user]
exec_cmd() {
  sudo su -c "$1" --shell /bin/bash -- ${2:-mediagoblin}
}

# Check system requirements
check_requirements() {
  [[ $(lsb_release -r | awk '{split($2,r,"."); print r[1]}') -ge 8 ]] \
    || ynh_die "GNU MediaGoblin ${VERSION} requires at least Debian Jessie."
  [[ -d /run/systemd/system ]] \
    || ynh_die "The application is only compatible with systemd yet."
}
