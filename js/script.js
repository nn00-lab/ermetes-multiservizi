(function(){

"use strict";



/*
====================================
CONFIGURAZIONE
====================================
*/


const WEBHOOK_URL = ""; 
// Inserire qui webhook n8n / CRM quando pronto



/*
====================================
TRACKING GOOGLE
====================================
*/


window.dataLayer = window.dataLayer || [];


function track(event,data={}){

window.dataLayer.push({

event:event,

...data

});

}





track(
"page_view",
{
page:location.pathname
}
);





/*
====================================
FORM
====================================
*/


const form =
document.getElementById("leadForm");



if(!form){

return;

}




const submitButton =
form.querySelector("button[type='submit']");




/*
====================================
ANTI SPAM HONEYPOT
====================================
*/


const honeypot =
document.createElement("input");


honeypot.type="text";

honeypot.name="website";

honeypot.style.display="none";


form.appendChild(honeypot);





/*
====================================
SUBMIT
====================================
*/


form.addEventListener(
"submit",
async function(e){


e.preventDefault();





if(honeypot.value){

return;

}





submitButton.disabled=true;


submitButton.innerHTML=
"Invio in corso...";





const formData =
new FormData(form);




const lead = {


nome:
formData.get("nome"),


telefono:
formData.get("telefono"),


email:
formData.get("email"),


servizio:
formData.get("servizio"),


messaggio:
formData.get("messaggio"),



pagina:
window.location.href,


data:
new Date().toISOString()


};







track(
"generate_lead",
lead
);







try {



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
JSON.stringify(lead)


}


);


}






showSuccess();






}

catch(error){


console.error(error);



alert(
"Si è verificato un errore. Riprova oppure chiamaci direttamente."
);



submitButton.disabled=false;


submitButton.innerHTML=
"Richiedi preventivo gratuito";



}



});







/*
====================================
SUCCESS MESSAGE
====================================
*/


function showSuccess(){



form.innerHTML=`

<div class="success-box">

<h3>
Richiesta inviata ✔
</h3>


<p>

Grazie per aver contattato Ermetes.
Ti ricontatteremo al più presto per valutare il tuo intervento.

</p>


<a class="btn btn--cta"
href="tel:+393513110662">

Chiama Ermetes

</a>


</div>

`;



track(
"lead_success"
);


}







/*
====================================
CTA TRACKING
====================================
*/


document
.querySelectorAll(".btn")
.forEach(btn=>{


btn.addEventListener(
"click",
()=>{


track(
"cta_click",
{

label:
btn.innerText.trim()

}

);


});


});





})();