(function(){

"use strict";



/* ================= CONFIG ================= */


const WEBHOOK_URL = "";



window.dataLayer = window.dataLayer || [];


function track(event,data={}){

window.dataLayer.push({

event,

...data

});

}





/* ================= SESSION DATA ================= */



const params = new URLSearchParams(location.search);



const leadId = crypto.randomUUID
?
crypto.randomUUID()
:
Date.now()+"-"+Math.random();



const meta = {


lead_uuid:leadId,

landing_url:location.href,

referrer:document.referrer || "direct",


utm_source:params.get("utm_source") || "",

utm_medium:params.get("utm_medium") || "",

utm_campaign:params.get("utm_campaign") || "",

utm_content:params.get("utm_content") || "",


gclid:params.get("gclid") || "",

fbclid:params.get("fbclid") || "",


device:
/Mobi/i.test(navigator.userAgent)
?
"mobile"
:
"desktop",


started_at:new Date().toISOString()


};




Object.entries(meta).forEach(([key,value])=>{


const el=document.getElementById(key);


if(el){

el.value=value;

}


});



track(
"page_view",
meta
);








/* ================= CTA TRACKING ================= */



document
.querySelectorAll("[data-track]")
.forEach(btn=>{


btn.addEventListener("click",()=>{


track(

"cta_click",

{

label:btn.dataset.track,

lead_uuid:leadId

}

);


});


});







/* ================= WIZARD ================= */


const form=document.getElementById("leadForm");


if(!form) return;



const panels=[

...form.querySelectorAll(".step-panel")

];


const total=panels.length;



let step=1;



const answers={

cliente:"",

servizio:""

};



const progress=document.getElementById("progressBar");


const btnNext=document.getElementById("btnNext");


const btnBack=document.getElementById("btnBack");


const btnSubmit=document.getElementById("btnSubmit");





function render(){


panels.forEach(panel=>{


panel.hidden =
Number(panel.dataset.step)!==step;


});



progress.style.width =
(step/total*100)+"%";



btnBack.hidden =
step===1;


btnNext.hidden =
step===total;


btnSubmit.hidden =
step!==total;



track(

"wizard_step",

{

step,

lead_uuid:leadId

}

);


}






function error(id,msg){


const el=document.getElementById("err-"+id);


if(el){

el.textContent=msg || "";

}


}





function validate(){



if(step===1){


if(!answers.cliente){

return false;

}


}



if(step===2){


if(!answers.servizio){

return false;

}


}




if(step===3){


const value=
document.getElementById("descrizione")
.value.trim();



if(!value){

error(
"descrizione",
"Inserisci una descrizione"
);


return false;

}

}




if(step===4){


const value=
document.getElementById("indirizzo")
.value.trim();



if(!value){

error(
"indirizzo",
"Inserisci la località"
);


return false;

}

}





if(step===6){


const nome=
document.getElementById("nome")
.value.trim();



const telefono=
document.getElementById("telefono")
.value.trim();



const privacy=
document.getElementById("privacy")
.checked;



if(!nome){

error("nome","Inserisci nome");

return false;

}



if(!telefono){

error(
"telefono",
"Inserisci telefono"
);

return false;

}



if(!privacy){

error(
"privacy",
"Accetta la privacy"
);

return false;

}


}



return true;


}








/* ================= SCELTE ================= */


document
.querySelectorAll(".choice")
.forEach(button=>{


button.addEventListener("click",()=>{


const field=
button.dataset.field;



answers[field]=
button.dataset.value;



button.parentElement
.querySelectorAll(".choice")
.forEach(b=>

b.classList.remove("is-selected")

);



button.classList.add("is-selected");



setTimeout(()=>{

btnNext.click();

},200);



});


});







btnNext.addEventListener("click",()=>{


if(!validate()) return;



if(step<total){

step++;

render();

}



});






btnBack.addEventListener("click",()=>{


if(step>1){

step--;

render();

}


});









/* ================= INVIO LEAD ================= */



form.addEventListener(
"submit",
async function(e){


e.preventDefault();



if(!validate()) return;



btnSubmit.disabled=true;


btnSubmit.innerText=
"Invio in corso...";





const payload={


...meta,


cliente:
answers.cliente,


servizio:
answers.servizio,


descrizione:
document.getElementById("descrizione").value,


indirizzo:
document.getElementById("indirizzo").value,


nome:
document.getElementById("nome").value,


telefono:
document.getElementById("telefono").value,


email:
document.getElementById("email").value,


azienda:
"Ermetes Società Cooperativa Sociale",


created:
new Date().toISOString()


};





/* ANTI BOT */


if(
document.getElementById("website").value
){

showSuccess();

return;

}







try{


if(WEBHOOK_URL){


await fetch(

WEBHOOK_URL,

{


method:"POST",


headers:{

"Content-Type":
"application/json"

},


body:
JSON.stringify(payload)


}


);


}





track(

"generate_lead",

payload

);



showSuccess();




}

catch(error){



track(

"lead_error",

{

message:error.message

}

);



alert(

"Errore invio. Contattaci telefonicamente."

);



btnSubmit.disabled=false;


btnSubmit.innerText=
"Ricevi preventivo gratuito";



}




});


 



function showSuccess(){


form.hidden=true;


document
.querySelector(".progress")
.hidden=true;



document
.getElementById("successPanel")
.hidden=false;



track(

"lead_success",

{

lead_uuid:leadId

}

);



}








/* ================= SCROLL TRACK ================= */


let max=0;



window.addEventListener(
"scroll",
()=>{


const percent=Math.round(

window.scrollY /

(
document.body.scrollHeight -
window.innerHeight
)

*100

);



if(percent>max){

max=percent;



if(max%25===0){


track(

"scroll_depth",

{

percent:max,

lead_uuid:leadId

}

);


}



}


},

{

passive:true

}

);








render();



})();