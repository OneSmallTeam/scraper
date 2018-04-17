#!/bin/bash
# 进入虚拟环境
source venv/bin/activate

# 循环并发所有爬虫
for (( c=1; c<=100; c++ ))
do
{
    scrapy crawl spider -a rule_id=${c} > log/${c}.log
}&
{
    sleep 20s
    echo "Welcome $c times"
}
done