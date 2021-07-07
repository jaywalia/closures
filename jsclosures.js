
// language specs : https://tc39.es/ecma262/
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures
// https://dmitripavlutin.com/simple-explanation-of-javascript-closures/
// https://amnsingh.medium.com/lexical-environment-the-hidden-part-to-understand-closures-71d60efac0e0
// https://medium.com/javascript-scene/master-the-javascript-interview-what-is-a-closure-b2f0d2152b36
// https://blog.bitsrc.io/a-beginners-guide-to-closures-in-javascript-97d372284dda


//-----------------------------------------
// 1. scope
// The scope is a space policy that rules the accessibility of variables.
// syntax is like C, Java
// but it is a functional language
// meaning functions can be passed around
/*
console.log("1. scope");

function counter(init) {
  let count = init;
  console.log(count);
}

counter(100);
// console.log(count);
//Uncaught ReferenceError: count is not defined

// Advantage : lets us use the same variable name in different functions

function groceryClerk(customerServed) {
	let customers = customerServed;
  console.log(customers);
}

function bankTeller(customerServed) {
	let customers = customerServed;
  console.log(customers);
}

groceryClerk(50);
bankTeller(17);

//-----------------------------------------
// 2. Nested Scopes
console.log("2. Nested Scope");


function outerF() {
	let outerCount = 10;
  
  function innerF() {
  	console.log("inner:" + outerCount);
  }
  
  innerF();
  outerCount = 100;
  innerF();
  console.log("outer:" + outerCount)
}

outerF();
*/

//-----------------------------------------
// 3. Lexical Scope
//The lexical scope consists of outer scopes determined statically.
// It’s called lexical (or static) because the engine determines (at lexing time) the nesting of scopes just by looking at the JavaScript source code, without executing it.
/*
console.log("3. Lexical Scope");

const level_0 = 0

function f_1() {
	const level_1 = 1;
  console.log(level_1, level_0);
  
  function f_2() {
  	const level_2 = 2;
    console.log(level_2, level_1, level_0);
    
    function f_3() {
    	const level_3 = 3;
      console.log(level_3, level_2, 
      level_1, level_0);
    }
    
    // call level 3 function
    f_3();
  }
  // call level 2 function
  f_2();
}

// call level 1 function
f_1();
*/
//-----------------------------------------
// 4. Closure
// The closure is a function that accesses its lexical scope even executed outside of its lexical scope.
// A closure is the combination of a function and the lexical environment within which that function was declared. 

console.log("4. Closure");
console.log("changed. 2...")

/*
function c_1() {

// define all the functions i need
  function c_2() {
  	console.log(c_var_1);
  }
  
  //
  let c_var_1 = 1;
  c_2();
  
}

c_1();
*/

// let's return the inner function
/*
function c_outer() {
	let c_outer_var = "c_outer_var: 100";
  
  function c_inner() {
  	console.log(c_outer_var);
  }
  
  //return c_inner(); <- don't do this
  return c_inner;
}

const c_inner_handle = c_outer();
//c_outer_var ???

c_inner_handle();

*/
// another example

function counter(start, owner) {
	let _owner = owner;
	let _start = start;
  
  // return an object, that has functions 
  return {
  	increase: () => {_start++; console.log(owner + ":" + _start)},
    decrease: () => {_start--; console.log(owner + ":" + _start)},
    current: () => console.log(owner + ":" + _start),
    reset: () => {_start = 0; console.log(owner + ":" + _start)}
  }
}
// objects (state + functions)
let gar_counter = counter(200, "gar");
let cbb_counter = counter(500, "cbb");

gar_counter.increase();
gar_counter.increase();
gar_counter.reset();
gar_counter.increase();
gar_counter.current();

cbb_counter.increase();
cbb_counter.decrease();

var garCounter = new Counter();
garCounter.increase();

var cbbCounter = new Counter();
cbbCounter.increase();











