const form = document.querySelector("form");
nField = form.querySelector(".name"),
nInput = eField.querySelector("input"),
eField = form.querySelector(".email"),
eInput = eField.querySelector("input"),
pField = form.querySelector(".password"),
pInput = pField.querySelector("input");

form.onsubmit = (e)=>{
  e.preventDefault(); 
  (eInput.value == "") ? eField.classList.add("shake", "error") : checkName();
  (eInput.value == "") ? eField.classList.add("shake", "error") : checkEmail();
  (pInput.value == "") ? pField.classList.add("shake", "error") : checkPass();

  setTimeout(()=>{
    nField.classList.remove("shake");
    eField.classList.remove("shake");
    pField.classList.remove("shake");
  }, 500);

  nInput.onkeyup = ()=>{checkNme();} 
  eInput.onkeyup = ()=>{checkEmail();} 
  pInput.onkeyup = ()=>{checkPass();}

  function checkName(){ 
    let pattern = /[a-z]$/; 
    if(!nInput.value.match(pattern)){ 
      nField.classList.add("error");
      nField.classList.remove("valid");
      let errorTxt = nField.querySelector(".error-txt");
      (nInput.value != "") ? errorTxt.innerText = "Enter a valid name" : errorTxt.innerText = "Name can't be blank";
    }else{
      nField.classList.remove("error");
      nField.classList.add("valid");
    }
  }

  function checkEmail(){ 
    let pattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/; 
    if(!eInput.value.match(pattern)){ 
      eField.classList.add("error");
      eField.classList.remove("valid");
      let errorTxt = eField.querySelector(".error-txt");
      (eInput.value != "") ? errorTxt.innerText = "Enter a valid email address" : errorTxt.innerText = "Email can't be blank";
    }else{
      eField.classList.remove("error");
      eField.classList.add("valid");
    }
  }

  function checkPass(){
    if(pInput.value == ""){ 
      pField.classList.add("error");
      pField.classList.remove("valid");
    }else{
      pField.classList.remove("error");
      pField.classList.add("valid");
    }
  }

  if(!nField.classList.contains("error") && !eField.classList.contains("error") && !pField.classList.contains("error")){
    window.location.href = form.getAttribute("action");
  }
}