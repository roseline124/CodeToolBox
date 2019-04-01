var list = document.querySelectorAll("li");
// event delegation

for(var i=0; i<list.length; i++){
    list[i].addEventListener("click", function(){
        console.log(i + "번째 리스트입니다.");
    }); // function이 갖고 있지 않은 i값은 callback 밖에 있는 변수 값을 참조하기 때문에
    // 가장 마지막 i를 출력 // i(클로저 변수)
}


// 해결 : var -> let 

for(let i=0; i<list.length; i++){
    list[i].addEventListener("click", function(){
        console.log(i + "번째 리스트입니다.");
    }); // function이 갖고 있지 않은 i값은 callback 밖에 있는 변수 값을 참조하기 때문에
    // 가장 마지막 i를 출력 // i(클로저 변수)
}