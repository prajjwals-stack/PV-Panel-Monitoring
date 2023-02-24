<template>
    <div>
        <HeaderComp/>

        <div class="container">
            <div class="row">
                <div class="col-6 container1">
                    <div class="form">
                        
                        <div>
                            <div style="display:flex; justify-content:flex-start; align-item:center">
                            <label for="user">Name</label>
                            <input  id="user" type="text" v-model="name">

                            </div>
                            <div style="display:flex; justify-content:flex-start; align-item:center">
                                <input type="checkbox" v-model="Tv">
                                <label for="Tv" >Television</label>
                                <input v-if="Tv" type="number" v-model="tv_number">
                            </div>
                            <div style="display:flex; justify-content:flex-start; align-item:center">
                                <input type="checkbox" v-model="ac"> 
                                <label for="AC" >Air conditioner</label>
                                <input v-if="ac" type="number" v-model="ac_number">
                            </div>
                            <div style="display:flex; justify-content:flex-start; align-item:center">
                                <input type="checkbox" v-model="WashingMachine">
                                <label for="washing_machine" >Washing Machine</label>
                            </div>
                            <div style="display:flex; justify-content:flex-start; align-item:center">
                                <input type="checkbox" v-model="fridge">
                                <label for="Fridge" >Fridge</label>
                            </div>
                            <div style="display:flex; justify-content:flex-start; align-item:center">
                                <label for="">Area</label>
                                <input type="text" style="width:30px" v-model="length">
                                <label for="Fridge" >*</label>
                                <input type="text" style="width:30px" v-model="breadth">
                            </div>
                        </div>
                        <div>
                            <button v-on:click="submithandler">Submit</button>
                        </div>
                        
                       

                    </div>






                </div>
                <div class="col-6"></div>
            </div>
        </div>



        <FooterComp/>
        
    </div>
</template>
<script>
import HeaderComp from "../components/HeaderComp.vue"
import FooterComp from "../components/FooterComp.vue"



export default {
  name: 'HomeView',
  components: {
   HeaderComp,FooterComp
  },
  data(){
    return {
        name:"",
        Tv:false,
        tv_number:1,
        ac_number:1,
        ac:false,
        fridge:false,
        WashingMachine:false,
        length:0,
        breadth:0,

    }
},
    methods: {
         submithandler(){
            console.log(this.name,  this.Tv, this.ac, this.fridge, this.WashingMachine);

        }
    }

  
}

</script>
<style>
.container{
    margin-top:10vh;
}
.container .form{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

</style>