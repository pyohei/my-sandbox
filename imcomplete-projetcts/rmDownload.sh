#!bin/sh

DOWNLOADS=$HOME/Downloads

DATE=`date`
LOG_DIR=$HOME/log/removed_downloads
LOG_FILE=removed_2014.txt

if [ ! -d ${LOG_DIR} ]
then
    mkdir -p $LOG_DIR
    echo "made directory" >> $LOG_DIR/$LOG_FILE
fi

if [ `ls -l | wc -l` -eq 0 ]
then
    echo $DATE >> $LOG_DIR/$LOG_FILE
    echo "NOFILE" >>$LOG_DIR/$LOG_FILE
    exit
fi

#for D_FILE_PASS in $DOWNLOADS/*
#do
#    D_FILE=`basename ${D_FILE_PASS}`
#    echo $D_FILE
#    mv "$D_FILE" `echo $D_FILE | tr '' '_' `
#done

echo >> $LOG_DIR/$LOG_FILE
echo $DATE >> $LOG_DIR/$LOG_FILE

for FILE in `ls $DOWNLOADS`
do
    echo $FILE >> $LOG_DIR/$LOG_FILE
    if test -f $FILE
    then
        rm $DOWNLOADS/$FILE 2>> $LOG_DIR/$LOG_FILE
    else
        rm -r $DOWNLOADS/$FILE 2>> $LOG_DIR/$LOG_FILE
        rm -d $DOWNLOADS/$FILE 2>> $LOG_DIR/$LOG_FILE
    fi
    #echo $DOWNLOADS/$FILE
done