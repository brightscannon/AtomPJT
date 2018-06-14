// 한줄주석
/*
여러줄 주석 작성
*/

console.log("data science js");


// 식별자
// 상수 : SNAKE_KASE (대문자 스네이크 케이스)
// 변수명 : camelCase(카멜케이스)
// 모듈 : PascalCase(파스칼케이스)
// 파이썬의 식별자 특수기호 : _
// 자바스크립트는 : $, _
// _name : private var, func
// $target : selector를 변수로 사용할때


// name = 'minwoo';
// console.log(name);
// var name = "minwoo"

// var a = 1.1;
// var b - 2;
// console.log(a+b,typeof a);


// 연산자
// +,-,*,/,%,++,--
/*
var number = 5;
var result = number++;
console.log(number, result);


var number = 5;
var result = ++number;
console.log(number, result);
*/
//데이터타입
/*
var a = 1; //number
var b = 1.9; //number
var c = "data"; //string
var d = [1,2,3]; //object
var e = {a:1, b:2}; //object
var f = true; // boolean
console.log(typeof a, typeof b, typeof c, typeof d, typeof e, typeof f);
*/
// null. undefined. NaN
// null : 값이 없음을 지정
// undefined : 값이 지정되지 않음
// NaN : 존재하지 않는 데이터 형태

/*
var a = null;
condole.log(a);
var b;
console.log(b); // 에러 : 값이 지정되지 않음
var c = 0/0;
console.log(c); //에러 : 존재하지않는형태
*/

// 비교연산자
// !=, ==, >, <, >-, <=, !==, ===
// 결론적으로 이야기하면 ===를 쓰는게 좋다. 이유는 데이터형식도 따져야하기때문

// 데이터 값만 비교
// console.log(1 == 1);
// console.log(1 == '1');

// 데이터 값과 타입을 모두 비교
// console.log(1 === '1');

// NaN
// 비교연산을 사용하지 못한다.
// ==> 비교연산시 NaN이 나타나면 무조건 False를 반환
// console.log(NaN === NaN);

//할당연산자
// +=,-=,*=,/=,%= ...

// var a = 1;
// a+=2;
// console.log(a);

//논리연산자
// &&(and), ||(or)
// console.log(true && false);
// console.log(true || false);

// 조건문
// if(false){
//   console.log("hello");
// }else if(true){
//   console.log("dss");
// }else{
//   console.log("world");
// }

// false로 간주되는 데이터
// null, undefined, NaN, 0, ""

// true로 간주되는 데이터
// [], {}

//  문제 1. 점수를 입력하면 학점이 출력되는 코드를 작성하기.
// var point = 61;
// ToDo : if, else if, else
// 결과값 A,B,C,D,F로 나오면 된다

// if(point >= 90){
//   console.log("A");
// }else if(point >= 80){
//   console.log("B");
// }else if(point >= 70){
//   console.log("C");
// }else if(point >= 60){
//   console.log("D");
// }else{
//   console.log("F");
// }

// 반복문
// while, for, do while
/*
var a = 10;
while(true){
  a++;
  if(a === 12){
    continue;
  }
  if(a>15){
    break;
  }
  console.log(a);
}
*/
/*
for (var i=0; i<5; i+=2){
  console.log(i);
}
*/

// 배열

var arr = ['a','b','c','d','e'];
console.log(arr[2]);
console.log(arr.length);
arr.push('f'); //맨뒤에 자료 삽입
console.log(arr);
arr.unshift('z'); //맨앞에 자료 삽입
console.log(arr);
var result = arr.pop(); //뒷자료 한개 빼기
console.log(arr,result);

var result = arr.splice(2,3); //2번째에서 3개 자르기
console.log(arr,result);

// 객체 - object
var obj = {};
obj.name = "bright";
obj['familyName'] = "kim";
console.log(obj);

for(var key in obj){
  console.log(key, obj[key])
}


console.log("===Module===")
// OOP:추상화,캡슐화
var Module = Module || {};
(function(_Module){

  var _name = 'bright';

  _Module.getName = function(){
    return _name;
  };

  _Module.setName = function(name){
    _name = name;
  };

})(Module);

console.log(Module.getName());
