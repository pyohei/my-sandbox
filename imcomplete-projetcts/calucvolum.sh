#!/bin/bash

# calculation of directry volum
# created in 2014/07/20

NOW=`date '+%Y%m%d%H%M%S'`
FILENAME=diskVolume.txt

echo >>$FILENAME
echo ============START==============>>$FILENAME
echo $NOW >>$FILENAME
echo ------MY_PC_VOLUEM-------->>$FILENAME

# check function confirming numeric
IsNumeric() {
    if [ $# -ne 1 ]; then
        return 1
    fi

    expr "$1" + 1 >/dev/null 2>&1
    if [ $? -ge 2 ]; then
        return 1
    fi

    return 0
}


DISK=`df -lk`
#echo $DISK
MAX_SIZE=`echo "$DISK" | sed -n '2p' | awk '{print $2}'`
NOW_SIZE=`echo "$DISK" | sed -n '2p' | awk '{print $3}'`
REST_SIZE=`echo "$DISK" | sed -n '2p' | awk '{print $4}'`
USEING_RATE=`echo "$DISK" | sed -n '2p' | awk '{print $5}'`
echo "MAX_SIZE"$'\t'$'\t'${MAX_SIZE}>>$FILENAME
echo "NOW_SIZE"$'\t'$'\t'${NOW_SIZE}>>$FILENAME
echo "REST_SIZE"$'\t'$'\t'${REST_SIZE}>>$FILENAME
echo "USEING_RATE"$'\t'$'\t'${USEING_RATE}>>$FILENAME
echo >>$FILENAME

echo ------DIRECTORY_SIZES-------->>$FILENAME
echo "DIR_NAME"$'\t'$'\t'"VOLUME"$'\t'$'\t'"DIR_RATE">>$FILENAME

for DIRS in `ls ~/`
do
#    echo du -s ~/${DIRS}
    VOLUME=`du -ks ~/${DIRS} 2>/dev/null | awk '{print $1}'`
    if ! IsNumeric $VOLUME
    then
        continue
    fi
    DIR_RATE=`expr ${VOLUME} \* 10000 / ${MAX_SIZE}`
    DIR_RATE=`echo "scale=2; $DIR_RATE / 100" | bc `
    echo ${DIRS}$'\t'$'\t'${VOLUME}$'\t'$'\t'${DIR_RATE}>>$FILENAME
done
#

echo ============END==============>>$FILENAME

