mkdir -p ../installer/usr/share/calc 2>/dev/null
cp  calculatormathlib.py ../installer/usr/share/calc/calculatormathlib.py
cp  calculator.py ../installer/usr/share/calc/calculator.py && chmod +x ../installer/usr/share/calc/calculator.py
mkdir -p ../installer/usr/local/bin 2>/dev/null
ln -sf /usr/share/calc/calculator.py ../installer/usr/local/bin/Calculator
mkdir ../installer/tmp 2>/dev/null
cp python_requirements.txt ../installer/tmp/python_requirements.txt
chmod +x ../installer/DEBIAN/postinst
dpkg-deb --build ../installer/ ../installer/calc_installer.deb
