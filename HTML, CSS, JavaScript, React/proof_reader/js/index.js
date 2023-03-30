let file1, file2;

let input1 = document.getElementById("file1_input");
let input2 = document.getElementById("file2_input");
let display1 = document.getElementById("display1");
let display2 = document.getElementById("display2");

input1.onchange = function ()
{
    file1 = input1.files[0];
    sessionStorage.setItem("file1", file1);
}

input2.onchange = function()
{
    file2 = input2.files[0];
    sessionStorage.setItem("file2", file2);
}

function fileHandler()
{
    console.log(file1);
    console.log(file2);
}

window.onload = function()
{
    // file1 = sessionStorage.getItem("file1") || 0;
    // file2 = sessionStorage.getItem("file2") || 0;
}