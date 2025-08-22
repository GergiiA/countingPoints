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
}




if (getCookie("value")!=null){
inp=document.getElementById("inp")
inp.value=Number(getCookie("value"))
}

if (getCookie("password")!=null){
pas=document.getElementById("password")
pas.value=getCookie("password")
}


function updateScore(homeroom, addition){
   form=document.getElementById("form")
   amount=document.getElementById("inp").value
   pas=document.getElementById("password").value
   form.action="/add/"+homeroom+"/"+amount+"/"+addition+"/"+pas
   //console.log(form.action)
   //console.log("/add/"+homeroom+"/"+amount+"/"+addition)
   addCookie("value", amount)
   addCookie("password", pas)
   form.submit()
}


