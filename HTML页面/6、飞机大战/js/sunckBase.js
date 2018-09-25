//随机数
function randomNum(min,max) {
    return parseInt(Math.random() * (max - min) + min);
}


//检查是否发生碰撞方法
function pzjcFunc(obj1,obj2) {
    var obj1Left = obj1.offsetLeft;
    var obj1Width = obj1Left + obj1.offsetWidth;
    var obj1Top = obj1.offsetTop;
    var obj1Height = obj1Top + obj1.offsetHeight;

    var obj2Left = obj2.offsetLeft;
    var obj2Width = obj2Left + obj2.offsetWidth;
    var obj2Top = obj2.offsetTop;
    var obj2Height = obj2Top + obj2.offsetHeight;

    if(!(obj1Left > obj2Width || obj1Width < obj2Left || obj1Top > obj2Height || obj1Height <  obj2Top)){
        return true;
    } else {
        return false;
    }

}