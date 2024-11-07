hid=document.getElementById("hid")
//id of update

uhi=document.querySelector('#uhi')


uhn=document.querySelector('#uhn')

//id of name
uin=document.querySelector('#uin')

//id of email
uie=document.querySelector('#uie')

//id of contact
uic=document.querySelector('#uic')
console.log(uic);

console.log("hello world")
function getid(id){
    hid.value=id
    
    console.log(hid.value)
}
function getdata(id,name,email,phno){
    console.log(id,name,email,phno);
    uin.value=name
    uie.value=email
    uic.value=phno
    uhi.value=id
    console.log(uhi.value);
    
}
// function getdata(id,name,email,phno){
//     console.log(id,name,email,phno);
//     uin.value=name
//     uie.value=email
//     uic.value=phno
//     uhi.value=id

    
// }