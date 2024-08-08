#----------------------------------
# run.sh
#----------------------------------

set -o errexit
set -o verbose

rm -rf parser.out
rm -rf parserun.log

python3 vhdlply_test.py | tee parserun.log
