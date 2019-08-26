#!/bin/bash


SCRIPT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
loglist=`ls $1`
for i in $loglist
do
    cat $SCRIPT_ROOT/$1/$i |grep "average fps:"| grep "data_source_pack.cc" | awk '{print $2,$11,$13,$15,$17}' | awk -F "," '{print $1,$2,$3,$4}' >$SCRIPT_ROOT/$1/$i.txt
done
cd $SCRIPT_ROOT/$1
cat $i.txt | awk -F "." '{print $1}' >${i}_time
cat $i.txt | cut -f 2-6 -d "." >${i}_time1
sed -i 's/^/2019-08-20 &/g' ${i}_time

cat ${i}_time | while read line
do
    date -d "$line" +%s >>time_stamp.txt
done


