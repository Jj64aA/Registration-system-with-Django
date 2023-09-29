let form = document.getElementById("form");
let f_name = document.getElementById("f-name")
let u_number = document.getElementById("u-number")
let u_major = document.getElementById("u-major")
let p_number = document.getElementById("p-number")
let email = document.getElementById("email")
//------------------------------------------
let error = document.getElementById("error")
let pa = document.createElement("p") 
//------------------------------------------
form.addEventListener("submit",(e)=>{
   let messges = []
   let pattern  =  /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
   let pattern_u_number = /20[0-9]{2}39[0-9]{6}/ig;
   if( f_name.value === "" || f_name.value === null ){
      messges.push('Full Name is required')
   }
   if ( u_number.value.length > 12 || u_number.value.length <12){
      messges.push('University number invalid')
   }
   if ( p_number.value.length > 10 || p_number.value.length <10){
      messges.push('Phone number invalid')
   }
   if(pattern.test(email.value) === false){
      messges.push('Please enter a valid email address')
   }
   if(pattern_u_number.test(u_number.value) === false){
      messges.push('Please enter a valid University number')
   }

   if (messges.length > 0){
      console.log(messges)
      e.preventDefault()
      pa.innerHTML = messges.join(', ')
      pa.classList.add('p-3','mb-1')
      error.classList.add('text-danger', 'fw-bold', 'border', 'border-danger', 'p-2', 'mb-5');
      error.appendChild(pa)   
      setTimeout(()=>{
         window.location.reload();
      }, 8000);
   ;}
});



