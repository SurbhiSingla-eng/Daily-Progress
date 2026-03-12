// promise functions
const myPromise = new Promise((resolve, reject) => {
  if (/* operation successful */) {
    resolve('Success value'); 
  } 
  else {
    reject(new Error('Failure reason')); 
  }
});


// let: loacl scope, variable can not be redeclared
// var: global scope, variable can be redeclared 
// const: global scope, constant value
// decalring type of variable is not necesaary

//try catch
const jsonString = '{"name": "John" age: 30}'; // Malformed JSON (missing comma)

try {
  const data = JSON.parse(jsonString); // This might throw a SyntaxError
  console.log(data);
} catch (error) {
  console.error("JSON parsing error:", error.message); // Handle the error gracefully
}

console.log("The script continues to run."); // The program doesn't crash
