console.log("-------------------- To know what is the type of data ------------------")
var student_name="Aaditya";
console.log(typeof(student_name))

var eng_marks=44;
console.log(typeof(eng_marks))

var hindi_marks=80.5;
console.log(typeof(hindi_marks))

var maths_marks=34;
console.log(typeof(maths_marks))

var science_marks=true;
console.log(typeof(science_marks))


console.log("-------------------- Nothing ------------------")


var student_name="Aaditya";
console.log("Student Name: ",student_name)
var eng_marks=44;
console.log("English marks: ",eng_marks)

var hindi_marks=80;
console.log("Hindi marks: ",hindi_marks)

var maths_marks=34;
console.log("Maths marks: ",maths_marks)

var science_marks=80;
console.log("Science marks: ",science_marks)

var total=eng_marks+hindi_marks+science_marks+maths_marks
console.log("Total Marks: ",total)

var percent=238/400*100
console.log("Percentage: ",percent)



console.log("-------------------- Type casting ------------------")
// string to number
var a1="50"
console.log(parseInt(a1))
// number to string
var a2=20
console.log(a2.toString())
//  integer to float
var a3=30
console.log(parseFloat(a3))
// float to integer
var a4=30.5
console.log(parseInt(a4))
// null
var a = null;
console.log("Value of a is: ",a)
// undefined
var b;
console.log("Value of b is: ",b)