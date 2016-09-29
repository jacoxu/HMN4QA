#! /bin/sh

echo "Start to run the HMN4QA in background ..."
python main_run.py > /dev/null&
touch $!".pid"