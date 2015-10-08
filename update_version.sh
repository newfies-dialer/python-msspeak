#
# Usage:
#   ./update_version.sh 0.1.1
#

git flow release start v$1
sed -i -e "s/__version__ = '.*'/__version__ = '$1'/g" msspeak/__init__.py
sed -i -e "s/version='.*'/version='$1'/g" setup.py
#rm -rf docs/html
#python setup.py develop
#make docs
#git commit docs msspeak/__init__.py -m "Update to version v$1"
git commit -a -m "Update to version v$1"
git flow release finish v$1
python setup.py sdist
twine upload dist/python-msspeak-$1.tar.gz upload
git push origin develop; git push origin master; git push --tags
