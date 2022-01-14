const signup = document.querySelector("#signup")
const popup = document.querySelector("#popup")
const close = document.querySelector("#close")
const popup1 = document.querySelector("#popup1")
const close1 = document.querySelector("#close1")
const email = document.querySelector("#email")
const login = document.querySelector("#login")
const close2 = document.querySelector("#close2")
const popup2 =  document.querySelector("#popup2")
const signup1 = document.querySelector("#signup1")
const login1 = document.querySelector("#login1")

// when user clicks sign up
signup.addEventListener("click", ()=>{
    if(popup.classList.contains("hidden")){
        popup.classList.remove("hidden")
    }    
})
close.addEventListener("click", ()=>{
    popup.classList.add("hidden")
})

// when user clicks on continue with email
email.addEventListener("click", ()=>{
    if(popup1.classList.contains("hidden")){
        popup.classList.add("hidden")
        popup1.classList.remove("hidden")
    }    
})
close1.addEventListener("click", ()=>{
    popup1.classList.add("hidden")
})

//when user clicks on login in the navbar
login.addEventListener("click", ()=>{
    if(popup2.classList.contains("hidden")){
        popup2.classList.remove("hidden")
    }
})
close2.addEventListener("click", ()=>{
    popup2.classList.add("hidden")
})

//when user clicks on signup in the login popup
signup1.addEventListener("click", ()=>{
    if(popup.classList.contains("hidden")){
        popup2.classList.add("hidden")
        popup.classList.remove("hidden")
    }    
})

//when user clicks on login in the sign up popup
login1.addEventListener("click",()=> {
   if(popup2.classList.contains("hidden")){
      popup.classList.add("hidden")
      popup2.classList.remove("hidden")
   }
})