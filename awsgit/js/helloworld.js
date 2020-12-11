/* this is a  multi-lin
comment */
var number = 5; // declaring + assigning
var a; //declaring variable, uninitialized


var str1 = "this 'thing' is\n"+"very fascinating,\n\"that\" veries.";
a = str1[48];
//console.log(a);
var i = 1;
function fnc1 (num1,num2){
    var c = num1+num2;
    console.log(i,c);
    i++;
}

var ar1 = [[10,11],[20,21]];
ar1.push([[300,301],[310,311]]);
ar1.unshift([00,01]);
//console.log(ar1);

var a2 = [0,1,2,3,4,5];

function arn(arr,item){
    arr.push(item);
    item = arr.shift();
    return item;
}
var a3 = {
    224:{
        'height':14,
        'weight':14,
        'length':14
    }
}
function idch(id,prop){
    a3[id][prop]=null;
    return a3;
}
console.log(idch(224,'width'))