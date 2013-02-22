#!/bin/sh
if [ $1 ]
  then if [ $2 ]
    then sphinx-build -b html -c source/ -D master_doc=$1 $2 build/fasthtml
  else echo "Usage: ./fastbuild.sh MasterFile source/Directory/To/Build"
  fi
else echo "Usage: ./fastbuild.sh MasterFile source/Directory/To/Build"
fi
