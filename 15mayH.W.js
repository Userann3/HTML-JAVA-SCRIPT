
let grade=Number(prompt("Enter Your Percentage"));


if (grade>=90 && grade<101)
    {
        document.write("You get A Grade");
    }

else if (grade>=80 && grade<90 )
    {
        document.write("You get B Grade");
    }
else if (grade>=70 && grade<80 )
    {
        document.write("You get C Grade");
    }
else if (grade>=60 && grade<70 )
    {
        document.write("You get D Grade");
    }
else if (grade>=50 && grade<60 )
    {
        document.write("You get E Grade");
    }

else if (grade<50 && grade>=0)
{
    document.write("You Failed");
}