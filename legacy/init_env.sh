#!/bin/bash
echo 'root directoy' && pwd  && ls 
cd app 
echo '/app directoy' && pwd && ls 
airflow initdb