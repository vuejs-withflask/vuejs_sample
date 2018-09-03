<template>
    <div class ="users">
   <h1>users</h1>
   <form v-on:submit="adduser">
       <input type="text" v-model="newuser.name" placeholder="enter name">
       <br/>
        <input type="text" v-model="newuser.email" placeholder="enter email">
        <br/>
        <input type="submit" value="submit">

   </form>
   <ul>
       <li v-for="user in users">
           <input type="checkbox" class="toggle" v-model="user.contacted">
           <span :class="{contacted:user.contacted}">
           {{user.name}}:{{user.email}}<button v-on:click="deleteuser(user)">x</button>
            </span>
            </li>

   </ul>
    </div>
</template>

<script>
export default {
  name: "users",
  data() {
    return {
      newuser: {},
      users: []
    };
  },
  methods: {
    adduser: function(e) {
      this.users.push({
        name: this.newuser.name,
        email: this.newuser.email,
        contacted: false
      });
    },
    deleteuser: function(user) {
      this.users.splice(this.users.indexOf(user), 1);
    }
  },
  created: function() {
      var self = this;
    this.$http
      .get("https://jsonplaceholder.typicode.com/users")
      .then(response => {
        this.users = response.data;
      });
  }
};
</script>
<style scoped>
.contacted {
  text-decoration: line-through;
}
</style>
