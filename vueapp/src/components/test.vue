<template>
    <div class ="test">
        <h1>{{title}}</h1>
        <p>{{user.first_name}}</p>
        <p v-text="user.first_name"></p>
        <p v-if="showname">{{user.last_name}}</p>
        <p v-else>Nobody</p>
        <ul>
            <li v-for="item in items">{{item.title}}</li>
        </ul>
        <button v-on:click= "greet">say greeting</button>
        <input type="text" v-on:keyup="presskey">
        <br>
        <hr/>
        <label>first_name:</label><input type="text" v-model="user.first_name">
        <br/>
        <label>last_name:</label><input type="text" v-model="user.last_name">
        <h3>{{fullname}}</h3>
    </div>
</template>

<script>
export default {
    name:'test',
    data(){
        return{
            title:"hello world",
        user:{
            first_name:"venkatesh",
            last_name :"chary"
        },
        showname:false,
        items:[
            {title:"item one"},
            {title:"item two"},
            {title:"item three"}
        ]
        }
    },
    methods:{
        greet :function(grreting){
            alert("hello")
        },
        presskey:function(presskey){
            console.log(presskey.target.value)
        }
    },
    computed:{
        fullname:function(){
            return this.user.first_name+' '+this.user.last_name
        }
    }
}
</script>
<style scoped>

</style>
