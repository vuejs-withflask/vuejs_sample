<template>
    <div class ="login">
    <h1>login</h1>
   <form v-on:submit="login">
       <input type="text" v-model="newuser.name" placeholder="enter name">
        <br/>
        <input type="text" v-model="newuser.password" placeholder="enter password">
        <br>
        <input type="submit" value="login">

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
        login() {
                if(this.newuser.name != "" && this.newuser.password != "") {
                    console.log("username:",this.newuser.name,"password:",this.newuser.password)
                    this.$http.post("http://127.0.0.1:5000/login",{
                        "username": this.newuser.name,
                        "password":this.newuser.password}).then(response => {
                    console.log(response)
                    localStorage.setItem('access_key',response.data['token'])
                    console.log("token:",localStorage.getItem('access_key'))
                    // this.$router.push('/logged')
                });
                } else {
                    console.log("------------>",this.users);
                }
         }
    }
    }
</script>

