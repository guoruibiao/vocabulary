#!/usr/bin/bash
# 随机输出
judge_is_enter()
{
    IFS=
    read -n 1 key
    if [ "$key" = "" ]; then
        return 1
        #echo "This was really Enter, not space, tab or something else"
    fi
    return 2
}
source=./data/vocabularies.txt
total=`wc -l $source | awk '{print $1}'`

while [ 1 -le 100 ]
do
    #echo "RANDOM=" $RANDOM
    let "target=$RANDOM%$total"
    #echo "TARGET=" $target

    line=`cat $source | head -$target | tail -1`
    word=`echo $line | awk '{print $1}'`
    desc=`echo $line | awk '{print $2}'`
    echo $word
    needdesc=`judge_is_enter`
    if [ "$needdesc" == "1" ];then
        continue
    else
        echo $desc
    fi
done
