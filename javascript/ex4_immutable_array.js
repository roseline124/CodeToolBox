function home() { 
    const list = ["apple", "orange", "watermelon"];
    list = "냥"; // error
    list.push("banana"); // 정상적으로 작동. 
    console.log(list);
}

// const를 사용해도 배열과 오브젝트의 값을 변경하는 것은 가능하다.

home();

// immutable array는 어떻게 만들까?
// 뒤로가기, 앞으로 가기 구현할 때 
// 불변 array 
// 복제해서 수정 가능하지만 원본은 그대로 저장된다. 
// list2는 const 타입이 아니다. list, list2 둘다 typeof로 확인해보면 object타입(배열)이지만
// list는 수정 불가능하고, list2는 수정 가능하다.
const list = ["apple", "orange", "watermelon"];
list2 = [].concat(list, "banana");
console.log(list, list2)
console.log(list === list2)
