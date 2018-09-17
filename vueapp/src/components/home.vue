<template>
    <div class ="login">
        <h1> Login here</h1>
        <form>
            <div row class="box">
                <div row>
                <input id="username" v-model="input.name" type="text" placeholder="Enter username" value="">
                </div>
                <div row>
                    <input id="password" v-model="input.password" type="text" placeholder="Enter Password" value="">        
                </div>
                <div row>
                <button type="button" v-on:click="login()">Login</button>
                <router-link :to="{ name: 'listusers'}"><button type="button" >listusers</button></router-link>
                </div>
            </div>            
        </form>
    </div>
</template>

<script>
    export default {
        name: 'Login',
        data() {
            return {
                input: {}
            }
        },
        methods: {
            login() {
                if(this.input.name != "" && this.input.password != "") {
                    console.log("username:",this.input.name,"password:",this.input.password)
                    this.$http.post("http://127.0.0.1:5000/registration",{
                        "username": this.input.name,
                        "password":this.input.password}).then(response => {
                    console.log(response)
                    alert("user is created successfully")
                });
                } else {
                    console.log("------------>",this.users);
                }
            },

        }
    }
</script>
