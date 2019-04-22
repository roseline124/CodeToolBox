var word = '제로초'

while (true){
    var answer = prompt(word) // prompt : 입력받는 함수 
    if (word[word.length-1] === answer[0]){ // 마지막 인덱스 : 문자 길이 -1
        alert("딩동댕")
        word = answer;
    } else {
        alert("땡")
    }
}

// alert, prompt, console.log 등은 브라우저가 만들어준 함수이다. 

