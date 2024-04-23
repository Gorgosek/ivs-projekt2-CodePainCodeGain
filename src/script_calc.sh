mkdir -p ../installer/usr/share/ivs_calc 2>/dev/null
cp  calculatormathlib.py ../installer/usr/share/ivs_calc/calculatormathlib.py
cp  calculator.py ../installer/usr/share/ivs_calc/calculator.py
chmod +x ../installer/usr/share/ivs_calc/calculator.py
mkdir -p ../installer/usr/local/bin 2>/dev/null
ln -sf /usr/share/ivs_calc/calculator.py ../installer/usr/local/bin/Calculator
mkdir ../installer/tmp 2>/dev/null
cp python_requirements.txt ../installer/tmp/python_requirements.txt
chmod +x ../installer/DEBIAN/postinst

dpkg-deb --build ../installer/ ../calc_installer.deb