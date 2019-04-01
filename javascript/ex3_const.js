function home() {
    var homename = "my house";
    homename = "your house";
    console.log(homename);
}

home();

// 재선언 금지.
function home() {
    const homename = "my house";
    homename = "your house";
    console.log(homename);
}

home();

// 데이터 타입에 상관없이 재선언 불가
function home() {
    const homename = [1,2,3,3];
    homename = [1,2,3];
    console.log(homename);
}

// const를 기본으로 사용한다.
// 변경될 수 있는 변수는 let을 사용한다.
// var는 사용하지 않는다. 