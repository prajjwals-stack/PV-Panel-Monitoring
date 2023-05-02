<template style="height:100vh">
    <div>
        <HeaderComp />
        <div style="margin-top:10vh; width:100%; display:flex; justify-content:flex-start; flex-direction:row">

       
        <div v-for="x in list" :key="x" >
            <p>bid</p>
            <div>
                <p><span>Username: </span>{{ x["user"] }}</p>
                <p><span>Amount of Energy required(units): </span>{{ x["energy"] }} units</p>
                <p>BIDS</p>
                <div style="border:1px solid red">
                    <div v-for="y in x['bids']" :key="y">
                        <p><span>Bidder Name: </span> {{ y["bidder__name"] }}</p>
                        <p><span>Pricing(per unit):</span>{{ y["pricing_rate"] }}</p>
                    </div>
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


export default{
    components: {
   HeaderComp,FooterComp
    },
    data(){
        return {
            list:undefined,
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
        }

    }
}
</script>