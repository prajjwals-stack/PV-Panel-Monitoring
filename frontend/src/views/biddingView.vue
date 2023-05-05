<template style="height:100vh">
    <div>
        <HeaderComp />
        <div style="margin-top:10vh; display:flex; justify-content:flex-start; flex-direction:column">

        <div style="display:flex; justify-content:flex-start; flex-direction:row"><input style="border:1px solid black; border-radius:5px; margin:0 5px 0 40px" type="Number" v-model="Units_required" placeholder="Enter amount of energy required(units)"><span><button class="btn btn-outline-success" v-on:click="Open_bid">Open Bid</button></span></div>
        
        <div style="margin:40px; border-radius:10px">
            <table class="table table-bordered">
                <thead style="background:rgb(34, 138, 235); color:white">
                    <tr>
                        <td>BID CREATOR</td>
                        <td>REQUIRED UNITS</td>
                        <td>SELLERS/BIDDER</td>

                    </tr>
                </thead>
                <tbody>
                    <tr v-for="x in list" :key="x">
                        <td>{{ x["user"].toUpperCase() }}</td>
                        <td>{{ x["energy"] }} UNITS
                            <p v-if="Id!==x['uuid']"><input type="number" style="border:1px solid black; border-radius:5px; margin:0 5px 0 5px" v-model="Price_per_unit" placeholder="Pricing per units"><button class="btn btn-outline-success" v-on:click="CreateBid(x['uuid'])">Create Bid</button></p>
                        </td>
                        <table class="table">
                            <thead >
                                <tr>
                                    <td>
                                        BIDDER NAME
                                    </td>
                                    <td>PRICING</td>
                                    <td>ACCEPT</td>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="y in x['bids']" :key="y">
                                    <td>{{ y["bidder__name"] }}</td>
                                    <td>{{ y["pricing_rate"] }}</td>
                                    <td v-if="Id==x['uuid']"> <button class="btn btn-outline-success" v-on:click="accept(x['uuid'],x['user'],x['energy'],y['bidder__name'],y['pricing_rate'] )">Accept</button></td>
                                </tr>
                            </tbody>

                        </table>
                    </tr>
                </tbody>
            </table>

        </div>
        
       
    </div>


        <FooterComp/>
    </div>
</template>

<script>

import HeaderComp from "../components/HeaderComp.vue"
import FooterComp from "../components/FooterComp.vue"
import axios from 'axios'


export default{
    components: {
   HeaderComp,FooterComp
    },
    data(){
        return {
            list:undefined,
            Price_per_unit:undefined,
            Units_required:undefined,
            Id:undefined,
        }
    },
    mounted(){
        this.bids()
        this.get_id()
    },
    methods:{
        async bids(){
            await axios.get('http://localhost:8000/all_bids')
            .then(res=>{
                console.log(res.data)
                this.list=res.data
            }).catch(err=>{
                console.log(err)
            })
        },
        
        async CreateBid(uuid){
            await axios.post('http://localhost:8000/create_bid',{
                "Pricing":this.Price_per_unit,
                "Bid_creator_id":uuid
            })
            .then(res=>{
                console.log(res);
                location.reload();
            }).catch(err=>{
                console.log(err)
            })

        },
        async accept(id,user,energy,bidder,price){
            await axios.post('accept',{
                "userid":id,
                "user":user,
                "Energy":energy,
                "Bidder":bidder,
                "price":price
            }).then(res=>{
                console.log(res)
                location.reload()
            }).catch(err=>{
                console.log(err)
            })
        },
        async Open_bid(){
            await axios.post('biding',{
                'Energy':this.Units_required
            })
            .then(res=>{
                console.log(res)
                location.reload();
            })
                
            .catch(err=>{
                console.log(err)})
        },
        async get_id(){
            await axios.get('get_id')
            .then(res=>{this.Id = res.data})
            .catch(err=>{console.log(err)})
        }

    }
}
</script>