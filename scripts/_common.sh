#
# Common variables
#

# MediaGoblin version
VERSION=0.8.1

# Package name for MediaGoblin dependencies
DEPS_PKG_NAME="mediagoblin-deps"

#
# Common helpers
#

# Print a message to stderr and exit
# usage: die msg [retcode]
die() {
  printf "%s" "$1" 1>&2
  exit "${2:-1}"
}

# Execute a command as another user (mediagoblin by default)
# usage: exec_cmd cmd [user]
exec_cmd() {
  sudo su -c "$1" --shell /bin/bash -- ${2:-mediagoblin}
}

# Check system requirements
check_requirements() {
  [[ $(lsb_release -r | awk '{split($2,r,"."); print r[1]}') -ge 8 ]] \
    || die "GNU MediaGoblin ${VERSION} requires at least Debian Jessie."
  [[ -d /run/systemd/system ]] \
    || die "The application is only compatible with systemd yet."
}
