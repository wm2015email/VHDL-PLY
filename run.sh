#----------------------------------
# run.sh
#----------------------------------

set -o errexit
set -o verbose

rm -rf __pycache__
rm -rf parsetab.py
rm -rf parser.out
rm -rf parserun.log

python3 vhdlply_test.py | tee parserun.log
