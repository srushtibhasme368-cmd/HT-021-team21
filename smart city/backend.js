const express=require("express");
const {OAuth2Client}=require("google-auth-library");

const app=express();
app.use(express.json());
app.use(express.static(__dirname));

const users=[{username:"admin",password:"1234"}];

app.post("/login",(req,res)=>{
    const {username,password}=req.body;
    const user=users.find(u=>u.username===username && u.password===password);
    res.send(user ? "Login Success 🎉" : "Invalid credentials");
});

// GOOGLE AUTH
const client=new OAuth2Client("YOUR_GOOGLE_CLIENT_ID");

app.post("/google-login", async(req,res)=>{
    try{
        const ticket=await client.verifyIdToken({
            idToken:req.body.token,
            audience:"YOUR_GOOGLE_CLIENT_ID"
        });

        const payload=ticket.getPayload();
        res.send("Google Login Success : "+payload.email);
    }
    catch{
        res.send("Google Login Failed");
    }
});

app.listen(3000,()=>console.log("Server running on port 3000"));
