function test () {
   while : ; do
   sleep 1s
 if [ $1 -lt 100 ]; then
     echo "ok"
 else
    return
    fi
    done
}


test 1

