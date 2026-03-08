function openPage(){
    window.location.href="sample.html"
}

function checkInput(){
    let inputValue=document.getElementById("e-mail").value;
    let button=document.getElementById("startnow");
    if(e-mail.trim!=""){
        button.disabled=false;
    }
    else{
        button.disabled=true;
    }
}