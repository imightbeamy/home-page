#!/bin/bash

varify_step() {
    if [ $? = 0 ] ; then
        echo "Success!"
    else
        echo "Error during $1, exiting."
        exit 1
    fi
}

upload() {
    echo -n "Deploying $1..."
    scp  $1 $USERNAME@amyciavolino.com:~/public_html
    varify_step "$1 upload"
}

upload_dir() {
    echo -n "Deploying $1..."
    scp -r  $1 $USERNAME@amyciavolino.com:~/public_html
    varify_step "$1 upload"
}

########## Option parsing

while getopts "su:a" OPTION ; do
  case $OPTION in
    u)  USERNAME=$OPTARG
        ;;
    a)  UPLOAD_ASSETS=1
        ;;
    s)  SKIP_VIEWS=1
        ;;
    ?)  echo "Illegal option: -$OPTARG"
        exit 1
        ;;
  esac
done

########## Render and Preview

echo -n "Rendering...  "
python ./render.py
varify_step "render"

if [ -z $SKIP_VIEWS ] ; then
    echo "Opening preview..."
    open index.html
fi

echo -n "Continue? [Y/n] "
read
if [ "$REPLY" != "Y" ] ; then
    echo "Quitting"
    exit
fi

########## Upload Files

if [ -z $USERNAME ] ; then
    echo -n "username: "
    read USERNAME
fi

echo "Starting Uploads... "
upload index.html
upload projects.html
upload portfolio.html
upload .htaccess

if [ -n "$UPLOAD_ASSETS" ] ; then
    upload_dir assets
fi


########## Done!

echo "Done!"
if [ -z $SKIP_VIEWS ] ; then
    open link.webloc
fi
