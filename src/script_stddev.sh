#!/bin/sh
mkdir -p ../installer_stddev/usr/share/stddev 2>/dev/null
cp  calculatormathlib.py ../installer_stddev/usr/share/stddev/calculatormathlib.py
cp  standard_deviation.py ../installer_stddev/usr/share/stddev/standard_deviation.py
chmod +x ../installer_stddev/usr/share/stddev/standard_deviation.py
mkdir -p ../installer_stddev/usr/local/bin 2>/dev/null
ln -sf /usr/share/stddev/standard_deviation.py ../installer_stddev/usr/local/bin/stddev #name of binary
chmod +x ../installer_stddev/DEBIAN/postrm

dpkg-deb --build ../installer_stddev/ ../stddev_installer.deb
