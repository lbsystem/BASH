function test(i){
    setInterval(()=>{
     if (i<35){
       console.log("ok")  
       i++
       console.log(i)
     }
      else {
          return
      } 
    },1000)
}
test(0)

