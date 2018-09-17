<template>
    <div class ="list_users">
        <h1> List of users</h1>
        <ul>
            <li v-for="user in users">
                <tr>{{user.username}}</tr>
                <!-- {{user.username}}:{{user.password}} -->
            </li>
        </ul>
    </div>
</template>

<script>
    export default {
        name: 'list_users',
        data() {
            return {
                input: {},
                users:[],
            }
        },
        methods: {
            // list_user(){
            //     const auth = {
            //      headers: {'X-access-token':localStorage.getItem('access_key')} }
            //     console.log(headers)
            //     this.$http.get("http://127.0.0.1:5000/listusers",auth).then(
            //         response => {
            //         this.users = response.data;
            //         console.log(response.data)
            //         this.users.push(response.data)
            //         })
            // }
        },

    created: function() {
    console.log("--------------------------------------------")
     const auth = {
                 headers: {'X-access-token':localStorage.getItem('access_key')} }
    this.$http
      .get("http://127.0.0.1:5000/listusers",auth)
      .then(response => {
        this.users = response.data;
        console.log(this.users)
      });
  }
    }
</script>

