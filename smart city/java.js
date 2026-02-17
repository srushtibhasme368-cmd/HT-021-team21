function slide(){
    document.querySelector(".panel").classList.toggle("slide");
}

// NORMAL LOGIN
document.getElementById("loginForm").addEventListener("submit", async(e)=>{
    e.preventDefault();

    const data={
        username:username.value,
        password:password.value
    };

    const res=await fetch("/login",{
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify(data)
    });

    alert(await res.text());
});

// GOOGLE LOGIN
function handleCredentialResponse(response){
    fetch("/google-login",{
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({token:response.credential})
    })
    .then(res=>res.text())
    .then(msg=>alert(msg));
}
