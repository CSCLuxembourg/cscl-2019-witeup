#! /bin/sh


wget https://raw.githubusercontent.com/cscluxembourg/vestatech/master/challenges/sergei/Sergei.png
pipx install Stegano
stegano-lsb reveal -i Sergei.png
stegano-lsb-set reveal -i Sergei.png -g fibonacci -s 9
