cd yggdrasil
python utils/install_from_requirements.py conda requirements.txt requirements_condaonly.txt
python setup.py develop
cd ../
yggconfig
python -c "import yggdrasil"
ygginfo
