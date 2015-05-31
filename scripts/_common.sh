#!/bin/bash

# Global variable
# ---------------

APP="mediagoblin"
VERSION=0.7.1
METAREV=1
COMMIT="12fac853a4489a9d10cf365de0f71e1404d4d9fe"


# Helpers
# -------

# Execute a command as another user ($APP by default)
# usage: exec_cmd CMD [USER]
exec_cmd() {
    user=$APP
    [[ $# -eq 2 ]] && user=$2
    sudo su -c "$1" --shell /bin/bash -- $user
}
