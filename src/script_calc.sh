mkdir -p ../installer/usr/share/ivs-calc 2>/dev/null
cp  calculatormathlib.py ../installer/usr/share/ivs-calc/calculatormathlib.py
cp  calculator.py ../installer/usr/share/ivs-calc/calculator.py
chmod +x ../installer/usr/share/ivs-calc/calculator.py
mkdir -p ../installer/usr/local/bin 2>/dev/null
ln -sf /usr/share/ivs-calc/calculator.py ../installer/usr/local/bin/ivs-calc
mkdir ../installer/tmp 2>/dev/null
cp python_requirements.txt ../installer/tmp/python_requirements.txt
chmod +x ../installer/DEBIAN/postinst

dpkg-deb --build ../installer/ ../ivs-calc_installer.deb
