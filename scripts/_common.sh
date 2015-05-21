#!/bin/bash

# Global variable
# ---------------

APP="mediagoblin"
VERSION=0.7.1~git
METAREV=1
COMMIT="9fa1e602b40d1e531335bf903dc7b15632818cf0"


# Helpers
# -------

# Execute a command as another user ($APP by default)
# usage: exec_cmd CMD [USER]
exec_cmd() {
    user=$APP
    [[ $# -eq 2 ]] && user=$2
    sudo su -c "$1" --shell /bin/bash -- $user
}
