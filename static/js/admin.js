//var xmlHttp = new XMLHttpRequest();
//xmlHttp.open( "GET", "/checkPassword/yo", false );
//xmlHttp.send( null );
//console.log(xmlHttp.responseText)

/*
function getCookie(name) {
    const cookieList = document.cookie.split("; ")
    for (const cookie of cookieList) {
        const [key, value] = cookie.split("=")
        if (key === name) return value
    }
    return null
}

function addCookie(name, value) {

    document.cookie = name+"="+value+"; path=/"
}*/

function sendRequest(url){
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", url, false );
    xmlHttp.send( null );
    //console.log(xmlHttp.responseText)
    //console.log(url)
    return xmlHttp.responseText;
}

function loadPassAndNum(){
    inp=document.getElementById("inp")
    inp.value=Number(localStorage.getItem("value"))
    pas=document.getElementById("password")
    pas.value=localStorage.getItem("password")
    pas=document.getElementById("reason")
    pas.value=localStorage.getItem("reason")
}

function updateScore(homeroom, addition){
   form=document.getElementById("form")
   amount=document.getElementById("inp").value
   pas=document.getElementById("password").value
   reason=document.getElementById("reason").value
   if(reason==''){reason='No reason provided'}
   if(amount==''){alert('amount is required'); return;}
   console.log(pas)
   console.log(pas.length)
   //console.log("wtfwtfwtf1")
   if (pas.length!=0){
        //console.log("wtfwtfwtf2")
        if(sendRequest("/checkPassword/"+pas)=="True"){
            //console.log("wtfwtfwtf3")
             if(addition==true){
                 form.action="/add/"+homeroom+"/"+amount+"/"+pas+"/"+reason}
             else{
                 form.action="/add/"+homeroom+"/"+(-amount)+"/"+pas+"/"+reason}
             //console.log(form.action, 'passed')
             //console.log("/add/"+homeroom+"/"+amount+"/"+addition)
             //addCookie("value", amount)
             //addCookie("password", pas)
             localStorage.setItem("value", amount)
             localStorage.setItem("password", pas)
             localStorage.setItem("reason", reason)
             form.submit()}
        else{
           alert("Wrong password")}
   }
   else{
        alert("You need to enter a password")}
   //alert('forth alert')
}




//sendRequest("/checkPassword/"+'yo')


//console.log('acjfghjidfsuzgh')