function test () {
   while : ; do
   sleep 1s
 if [ $1 -lt 100 ]; then
     echo "ok"
     i=$((i+1))
     echo $i
 else
    return
    fi
    done
}



test 1

