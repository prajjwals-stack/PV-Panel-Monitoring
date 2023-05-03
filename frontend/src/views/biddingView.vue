<template style="height:100vh">
    <div>
        <HeaderComp />
        <div style="margin-top:10vh; display:flex; justify-content:flex-start; flex-direction:column">

        <div style="display:flex; justify-content:flex-start; flex-direction:row"><input type="Number" v-model="Units_required" placeholder="Enter amount of energy required(units)"><span><button v-on:click="Open_bid">Open Bid</button></span></div>
        <table class="table table-bordered">
            <thead>
                <tr>
                    <td>Bid Creator</td>
                    <td>Required Units</td>
                    <td>Sellers/Bidders</td>

                </tr>
            </thead>
            <tbody>
                <tr v-for="x in list" :key="x">
                    <td>{{ x["user"] }}</td>
                    <td>{{ x["energy"] }} 
                        <p><input type="number" v-model="Price_per_unit" placeholder="Pricing per units"><button v-on:click="CreateBid(x['uuid'])">Create Bid</button></p>
                    </td>
                    <table class="table table-bordered">
                        <thead>
                            <tr>
                                <td>
                                    Bidder Name
                                </td>
                                <td>Pricing</td>
                                <td>Accept</td>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="y in x['bids']" :key="y">
                                <td>{{ y["bidder__name"] }}</td>
                                <td>{{ y["pricing_rate"] }}</td>
                                <td> <button v-on:click="accept(x['uuid'],x['user'],x['energy'],y['bidder__name'],y['pricing_rate'] )">Accept</button></td>
                            </tr>
                        </tbody>

                    </table>
                </tr>
            </tbody>
        </table>
       
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
        }
    },
    mounted(){
        this.bids()
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
        }

    }
}
</script>