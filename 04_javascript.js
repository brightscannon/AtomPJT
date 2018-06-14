// 한줄주석
/*
여러줄 주석 작성
*/

console.log("data");


// 식별자
// 상수 : SNAKE_KASE (대문자 스네이크 케이스)
// 변수명 : camelCase(카멜케이스)
// 모듈 : PascalCase(파스칼케이스)


// name = 'minwoo';
// console.log(name);
// var name = "minwoo"

// var a = 1.1;
// var b - 2;
// console.log(a+b,typeof a);


// 연산자
// +,-,*,/,%,++,--
var number = 5;
var result = number++;
console.log(number, result);


var number = 5;
var result = ++number;
console.log(number, result);

//데이터타입
var a = 1; //number
var b = 1.9; //number
var c = "data"; //string
var d = [1,2,3]; //object
var e = {a:1, b:2}; //object
var f = true; // boolean
console.log(typeof a, typeof b, typeof c, typeof d, typeof e, typeof f);

// null. undefined. NaN
// null : 값이 없음을 지정
// undefined : 값이 지정되지 않음
// NaN : 존재하지 않는 데이터 형태

var a = null;
condole.log(a);
var b;
console.log(b); // 에러 : 값이 지정되지 않음
var c = 0/0;
console.log(c); //에러 : 존재하지않는형태

// 비교연산자
