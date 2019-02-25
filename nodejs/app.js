// app.js
const http = require('http'); // 모듈 import한 후, http 변수에 담는다.

http.createServer((request, response) => { // http의 createServer 메서드를 사용하여 서버 만들기
  response.statusCode = 200;
  response.setHeader('Content-Type', 'text/plain');
  response.end('Hello World');
}).listen(3000); // 해당 서버에 들어오는 request는 3000번 포트를 통해 듣는다. 

console.log('Server running at http://127.0.0.1:3000/'); // console.log : 출력 