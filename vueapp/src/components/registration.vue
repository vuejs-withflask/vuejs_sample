<template>
    <div class ="registration">
   <h1>users</h1>
   <form v-on:submit="registration">
       <input type="text" v-model="newuser.name" placeholder="enter name">
        <br/>
        <input type="text" v-model="newuser.email" placeholder="enter email">
        <br/>
        <input type="text" v-model="newuser.password" placeholder="enter password">
        <br>
        <input type="submit" value="submit">

   </form>
    </div>
</template>

<script>
    export default {
        name: 'registration',
        data() {
            return {
                newuser: {},
            }
        },
        methods: {
        registration() {
                if(this.newuser.name != "" && this.newuser.password != "") {
                    console.log("username:",this.newuser.name,"password:",this.newuser.password)
                    this.$http.post("http://127.0.0.1:5000/register",{
                        "username": this.newuser.name,
                        "password":this.newuser.password}).then(response => {
                    console.log(response)
                    alert("user is created successfully")
                });
                } else {
                    console.log("------------>",this.users);
                }
         }
    }
    }
</script>

