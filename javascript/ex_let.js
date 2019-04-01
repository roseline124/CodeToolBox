// var는 function scoped 이고,
// let, const는 block-scoped이다.

// let, const : 이미 만들어진 변수 이름으로 재선언하면 에러가 난다.
// let은 선언 후, 나중에 값을 할당해도 된다.
// 하지만 const는 선언과 동시에 값을 할당해야 한다.

var name = "global var";

function home() {
    var localvar = "local var";
    for(var i=0; i<100; i++){
    }
    console.log(i); // function 안의 지역 변수를 먼저 찾는다. 
}


function home() {
    var localvar = "local var";
    for(let i=0; i<100; i++){ // let을 쓰면 for문 block 내에서만 사용 가능 
        console.log(i);
    }
}

function home() {
    if(true){
        let myif = "myif";
    }
    console.log(myif);
}