This project is WIP status.  
But I can't guarantee about this re-open.  

# Terminal Hopper

Move directory easily as hopper.

## Usages

You write below codes in your .bash*.  

```
# Funtion name is ok with your favarit name!
pp() {
    PP_PROJECT=/YOUR-PATH-TO-THIS-PROJECT/project-jumper
    PRE_COUNT=0
    if [ -e $PP_PROJECT/.cache/projects.log ]; then
        PRE_COUNT=`grep -c '' $PP_PROJECT/.cache/projects.log`
    fi
    $PP_PROJECT/pjump.sh $*
    CUR_COUNT=0
    if [ -e $PP_PROJECT/.cache/projects.log ]; then
        CUR_COUNT=`grep -c '' $PP_PROJECT/.cache/projects.log`
    fi
    if [ $CUR_COUNT -gt $PRE_COUNT ]; then
        MOVING_DIR=`tail -n1 $PP_PROJECT/.cache/projects.log`
        cd $MOVING_DIR
    fi
}
```
