DIR="$( cd "$( dirname -- "$0" )" && pwd )"
echo $DIR

cd $DIR

# ulimit -n 50000
nohup gunicorn --config=./CaveOfSpongeBob/gunicorn_conf.py CaveOfSpongeBob.wsgi &> /dev/null &
