#!/bin/bash
#Author by henry.wen 
#check the application log if any keyword display.

BASEDIR=/usr/local/zabbix/script
FILEPATH=/usr/weblog/KAIFANGPINGTAI
IP=$1
TAG=${BASEDIR}/${IP}
TEMP=${BASEDIR}/${IP}_temp.log
START_NUM=`cat $TAG`
DATE=`date +%Y-%m-%d`
CDATE=`date -d '1 minutes ago' '+%Y-%m-%d'`

>${TEMP}

if [ ${DATE} != ${CDATE} ] ; then

   DATE=`echo ${CDATE}`
fi

FILENAME=jvm-app-0.log

echo "Grep the file and record the line"
MARKDATE=`date -d '1 minutes ago' '+%Y-%m-%d %I:%M'`
#MARKDATE=`date -d '1 minutes ago' '+%Y-%m-%d %H:%M'`

END_NUM=`grep -n "${MARKDATE}" ${FILEPATH}/${IP}/${DATE}/${FILENAME}|tail -1|awk -F: '{print $1}'`
CUR_NUM=`wc -l ${FILEPATH}/${IP}/${DATE}/${FILENAME}|awk '{print $1}'`
END_NUM=${END_NUM:-${CUR_NUM}}


#if [ -z  ${END_NUM} ]; then
#
#   END_NUM=`echo ${CUR_NUM}`
#
#if

#################################echo ${END_NUM}

if [ ${END_NUM} -lt ${START_NUM} ]; then
    START_NUM=0
elif [ ${END_NUM} -eq ${START_NUM} ] ; then
    #echo "the log file didn't have any updated"
    echo ${END_NUM} > ${TAG}
    exit 0;
fi

echo "Start scan between ${START_NUM} lines and ${END_NUM} jvm logs"

#perl -ne 'print "$. $_" if $. <= ${END_NUM} && $. >= ${START_NUM}  && /discard|Communications/' ${FILEPATH}/${DATE}/${FILENAME} >  ${
TEMP}  2>&1
perl -ne 'print $_ if $. <= '""${END_NUM}""' && $. >= '""${START_NUM}""' && /discard|Communications/'  ${FILEPATH}/${IP}/${DATE}/${FIL
ENAME}  > ${TEMP} 
#sed -n "/${START_NUM}/,/${END_NUM}/{/discard|Communications/p}"  ${FILEPATH}/${DATE}/${FILENAME}  > ${TEMP} 2>&1
ERRORNUM=`wc -l ${TEMP}|awk '{print $1}'`

if [ ${ERRORNUM}  -eq 0 ]; then
    echo "we don't found any exception on this server"
else

    echo "wefound_some_exceptions on this server ${IP} .pleas notify to relative person check"

fi

echo ${END_NUM} > ${TAG}