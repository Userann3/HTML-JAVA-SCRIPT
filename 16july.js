// function check(n){
//     let vowel="aeiou"
//     if(vowel.includes=n){
//         console.log("it's a vowel")
//     }
// }
// check("a")

// function check(n){
//     if(n%2==0){
//         console.log("it's even")
//     }
//     else if(typeof(n)!="number"){
//         console.log("it's not a number")
//     }
//     else{
//         console.log("it's odd")
//         }
// }
// check(5)

let odd=[]
let even=[]

function check(n){
    for(let i=1; i<n; i++){
        if(i%2==0){
            even.push(i)
            }
            else{
                odd.push(i)
                }
    }
}

check(8)