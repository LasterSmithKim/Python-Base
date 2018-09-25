
var mainScreen = document.getElementById("mainScreen")

//让背景运动
var jsBg1 = document.getElementById("bg1")
var jsBg2 = document.getElementById("bg2")

var timerBg = setInterval(function(){
    jsBg1.style.top = jsBg1.offsetTop + 1 +"px"
    jsBg2.style.top = jsBg2.offsetTop + 1 +"px"

    if (jsBg1.offsetTop >= 768){
        jsBg1.style.top = "-768px"
    }
    if (jsBg2.offsetTop >= 768){
        jsBg2.style.top = "-768px"
    }
},10)


//让飞机运动-拖拽效果
var airplane = document.getElementById("airplane")
//给飞机添加鼠标按下事件
airplane.addEventListener("mousedown",function(e){
    var ev = e || window.event
        basex = ev.pageX
        basey = ev.pageY
    console.log(basex,basey)
        movex = 0
        movey = 0


    //给主屏幕添加鼠标移动事件
    mainScreen.addEventListener("mouseover",function(e){
        var en = e || windows.event
        movex = en.pageX - basex
        basex = en.pageX
        movey = en.pageY - basey
        basey = en.pageY
        airplane.style.left = airplane.offsetLeft + movex + "px"
        airplane.style.top = airplane.offsetTop + movey + "px"
    },false)
},false)


//发射子弹

var timerBullent = setInterval(function(){
    //创建子弹
    var bullent = document.createElement("div")
    mainScreen.appendChild(bullent)
    bullent.className = "bullent"
    bullent.style.left = airplane.offsetLeft + 52 + "px"
    bullent.style.top = airplane.offsetTop -10 + "px"
    //让子弹飞
    var timerBullentFly = setInterval(function(){
        bullent.style.top = bullent.offsetTop - 10 + "px"
        if (bullent.offsetTop <= -20) {
            clearInterval(timerBullentFly)
            mainScreen.removeChild(bullent)
        }
    },50)
    bullent.timer = timerBullentFly //创建一个属性
},2000)


//敌人来袭

var timerenemy = setInterval(function(){
    //创建敌人
    var enemy = document.createElement("div")
    mainScreen.appendChild(enemy)
    enemy.className = "enemy"
    enemy.style.left = randomNum(0,472) + "px"
    enemy.style.top = "0px"
    //让敌人飞
    var timerenemyFly = setInterval(function(){
        enemy.style.top = enemy.offsetTop + 10 + "px"
        if (enemy.offsetTop >= 768) {
            clearInterval(timerenemyFly)
            mainScreen.removeChild(enemy)
        }
        enemy.timer = timerenemyFly //创建一个属性
    },20)
},500)

//子弹和敌人 碰撞检测定时器
var timerPZJC = setInterval(function () {
    var allEnemy = document.getElementsByClassName("enemy")
    var allBullents = document.getElementsByClassName("bullent")
    for (var i = 0 ; i < allBullents.length ; i++){
        for (var j = 0 ; j < allEnemy.length ; j++){
            var b = allBullents[i]
            var e = allEnemy[j]
            if(pzjcFunc(b,e)){
                clearInterval(b.timer)
                clearInterval(e.timer)
                mainScreen.removeChild(b)
                mainScreen.removeChild(e)
                break
            }
        }
    }
},100)


//自己飞机 死亡检测
var timerDie = setInterval(function () {
    var allEnemy = document.getElementsByClassName("enemy")
    for (var i = 0 ; i <allEnemy.length ; i++){
        if (pzjcFunc(allEnemy[i],airplane)){
            for (var j = 0 ; j<100; j++){
                clearInterval(j)

            }
        }
    }
},100)






