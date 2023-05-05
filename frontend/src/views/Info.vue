<template>
    <div style="height:100vh; overflow-y:hidden">
        <HeaderComp/>
        
        <div class="container">
            <div>
                <button v-if="!Output" class="btn btn-outline-success" >Update Database</button>
                <button v-if="Output" class="btn btn-outline-success" v-on:click="Update">Update Database</button>
            </div>
            
            <div class="row">
                <div class="col-6 container1">
                    <div class="form" style="height:80vh; ">
                        <table class="table table-bordered" >
                            <thead style="background:rgb(34, 138, 235); color:white">
                                <tr>
                                    <td>Select</td>
                                    <td>Appliances</td>
                                    <td>Options</td>
                                </tr>
                            </thead>
                            <tbody >
                                <tr>
                                    <th scope="row"><input type="checkbox" v-model="Tv"></th>
                                    <td> Television</td>
                                    <td v-if="Tv">
                                        <div class="input-group mb-0.5" style="display:flex; align-items:baseline">
                                            <p style="margin-right:10px;">Number of TV</p>
                                            <select class="custom-select" id="inputGroupSelect03" v-model="tv_number">
                                                <option value="1">1</option>
                                                <option value="2">2</option>
                                                <option value="3">3</option>
                                            </select>
                                            </div>
                                            <div class="input-group mb-0.5" style="display:flex; align-items:baseline">
                                                <p style="margin-right:10px;">Size of TV</p>
                                            <select class="custom-select" id="inputGroupSelect03" v-model="tv_size">
                                               
                                                <option value="41">32 inch</option>
                                                <option value="58">43 inch</option>
                                                <option value="88">55 inch</option>
                                            </select>
                                            </div>

                                    
                                    </td>
                                </tr>
                                <tr>
                                    <th scope="row"><input type="checkbox" v-model="ac"></th>
                                    <td>Air Conditioners</td>
                                    <td v-if="ac">
                                        <div class="input-group mb-0.5"  style="display:flex; align-items:baseline">
                                            <p style="margin-right:10px;" >Number of AC</p>
                                            <select class="custom-select" id="inputGroupSelect03" v-model="ac_number">
                                                
                                                <option value="1">1</option>
                                                <option value="2">2</option>
                                                <option value="3">3</option>
                                            </select>
                                            </div>
                                            <div class="input-group mb-0.5" style="display:flex; align-items:baseline">
                                                <p style="margin-right:10px;">Size of AC</p>
                                            <select class="custom-select" id="inputGroupSelect03" v-model="ac_size">
                                               
                                                <option value="1000">1.0 tons</option>
                                                <option value="1500">1.5 tons</option>
                                                <option value="2000">2.0 tons</option>
                                            </select>
                                            </div>
                                     </td>
                                </tr>
                                <tr>
                                    <th scope="row"> <input type="checkbox" v-model="WashingMachine"></th>
                                    <td>Washing Machines</td>
                                    <td v-if="WashingMachine">
                                        <div class="input-group mb-0.5"  style="display:flex; align-items:baseline">
                                            <p style="margin-right:10px;" >Number</p>
                                            <select class="custom-select" id="inputGroupSelect03" v-model="wm_number">
                                                
                                                <option value="1">1</option>
                                                <option value="2">2</option>
                                                <option value="3">3</option>
                                            </select>
                                            </div>
                                            <div class="input-group mb-0.5" style="display:flex; align-items:baseline">
                                                <p style="margin-right:10px;">Type</p>
                                            <select class="custom-select" id="inputGroupSelect03" v-model="wm_size">
                                               
                                                <option value="350">semi automatic</option>
                                                <option value="850">fully automatic</option>
                                        
                                            </select>
                                            </div>
                                            
                                            
                                            
                                            
                                            </td>
                                </tr>
                               
                                <tr>
                                    <th scope="row"> <input type="checkbox" v-model="fridge"></th>
                                    <td>Referigerator</td>
                                    <td v-if="fridge">
                                        <div class="input-group mb-0.5">
                                            <select class="custom-select" id="inputGroupSelect03" v-model="fridge_number">
                                                <option selected > Choose...</option>
                                                <option value="1">1</option>
                                                <option value="2">2</option>
                                                <option value="3">3</option>
                                            </select>
                                            </div></td>
                                </tr>
                                <tr>
                                    <td></td>
                                    <td>Daily Operational Hours ( Hours ) </td>
                                    <td><input type="number" v-model="operational_hours"></td>
                                </tr>
                                <tr>
                                    <td></td>
                                    <td>Electricity Tariff (Any currency) </td>
                                    <td><input type="number" v-model="terrif_cost"></td>
                                </tr>
                            </tbody>
                        </table>
                        <div>
                            <button v-on:click="submithandler" class="btn btn-primary">Submit</button>
                        </div>
                        
                       

                    </div>






                </div>
                <div class="col-6" style="margin-top:20px">
                  
                    <div v-if="Output">
                        
                        <table class="table table-bordered">
                            <thead style="background:rgb(34, 138, 235); color:white">
                                <tr>
                                    <th scope="col">#</th>
                                    <th scope="col">Device</th>
                                    <th scope="col">Numbers</th>
                                    <th scope="col">Wattage</th>
                                </tr>             
                            </thead>
                            <tbody>
                                <tr>
                                    <th scope="col">1</th>
                                    <th scope="col">Air Conditioners</th>
                                    <th scope="col">{{ ac_number }}</th>
                                    <th scope="col">{{ ac_total  }}</th>
                                </tr> 
                                <tr>
                                    <th scope="col">2</th>
                                    <th scope="col">Television</th>
                                    <th scope="col">{{ tv_number }}</th>
                                    <th scope="col">{{ tv_total  }}</th>
                                </tr> 
                                <tr>
                                    <th scope="col">3</th>
                                    <th scope="col">Washing Machine</th>
                                    <th scope="col">{{ wm_number }}</th>
                                    <th scope="col">{{ wm_total  }}</th>
                                </tr> 
                                <tr>
                                    <th scope="col">4</th>
                                    <th scope="col">Referigerator</th>
                                    <th scope="col">{{ fridge_number }}</th>
                                    <th scope="col">{{ fridge_total  }}</th>
                                </tr> 
                                

                            </tbody>
                            <tfoot>
                                <tr>
                                    <th scope="col">*</th>
                                    <th scope="col">Total</th>
                                    <th scope="col">{{  }}</th>
                                    <th scope="col">{{ total  }}</th>
                                </tr> 

                            </tfoot>
                        </table>
                        <p>Since your total maximum usage is around <b>{{ total }}</b>  so we would suggest you a ongrid solar panel of <b>{{ suggestion }}</b>  
                            watts.The total initial upfront cost would be around  <b>{{price}}</b>.
                        </p>
                        <table class="table">
                            <tr>
                                <th>Monthly Unit Consumed =</th>
                                <th>{{(total/1000)*operational_hours*30 }} units</th>
                            </tr>
                            <tr>
                                <th>Monthly Electricity Bill = </th>
                                <th>{{(total/1000)*operational_hours*30*terrif_cost }} rupees</th>
                            </tr>
                        </table>
                        <p> Total money saved in 5 years is {{ (total/1000)*operational_hours*30*terrif_cost*12*5 }}
                        </p>

                    </div>
                    
                </div>
            </div>
        </div>



        <FooterComp/>
        
    </div>
</template>
<script>
import HeaderComp from "../components/HeaderComp.vue"
import FooterComp from "../components/FooterComp.vue"
import axios from 'axios'


export default {
  name: 'HomeView',
  components: {
   HeaderComp,FooterComp
  },
  data(){
    return {
        name:"",
        Tv:false,
        tv_number:0,
        tv_size:32,
        ac_number:0,
        ac_size:1,
        wm_number:0,
        wm_size:1,
        fridge_number:0,
        ac:false,
        fridge:false,
        WashingMachine:false,
        length:0,
        breadth:0,
        tv_number2:0,
        Output:false,
        total:0,
        tv_total:0,
        ac_total:0,
        fridge_total:0,
        wm_total:0,
        suggestion:0,
        price:0,
        operational_hours:0,
        terrif_cost:0,
    }
},
    methods: {
         async Update(){
            await axios.post('update_db',{
                "total_watts":this.total,
                "terrif_cost":this.terrif_cost,
                "operational_hours":this.operational_hours
            })
            .then(res=>{
                console.log(res)
            })
            .catch(err=>console.log(err))

            },
         submithandler(){
            console.log(this.name,  this.Tv, this.ac, this.fridge, this.WashingMachine);
            console.log(this.tv_number,  this.ac_size, this.wm_size, this.fridge_number,this.tv_size);
            let tv_wattage=0;
            let ac_wattage=0;
            let fridge_wattage=0;
            let wm_wattage=0;
            let total=0;
            if(this.Tv){
                tv_wattage=this.tv_number* this.tv_size;
                this.tv_total=tv_wattage
            }
            if(this.ac){
                ac_wattage=this.ac_number * this.ac_size;
                this.ac_total=ac_wattage
            }
            if(this.WashingMachine){
                wm_wattage=this.wm_number*this.wm_size;
                this.wm_total=wm_wattage
            }
            if(this.fridge){
                fridge_wattage=this.fridge_number*400;
                this.fridge_total=fridge_wattage
            }
            total=tv_wattage+ac_wattage+wm_wattage+fridge_wattage;
            this.total=total;
            this.Output=true;
            if(total<1000){
                this.suggestion=1000
                this.price=60000

            }
            else if(total>=1000 && total<2000){
                this.suggestion=2000
                this.price=120000
            }
            else if(total>=2000 && total<3000){
                this.suggestion=3000
                this.price=180000
            }
            else if(total>=3000 && total<5000){
                this.suggestion=5000
                this.price=300000
            }
            else if(total>=5000 && total<7500){
                this.suggestion=7500
                this.price=400000
            }
            else{
                this.suggestion=10000
                this.price=600000
            }

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