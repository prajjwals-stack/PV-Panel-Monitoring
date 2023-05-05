<template>
  <div class="main">
    <HeaderComp/>
    <div class="container">
      <div class="row">
        <div v-if="value" style="display:flex; flex-direction:row">
          <div style="width:200px; height:100px; background:rgb(34, 138, 235); color:white; display:flex; justify-content:center; align-items:center; border-radius:10px; margin:20px; border:2px solid black"> 
            <div >
              <p style="margin:5px">Energy Used:</p>
              <p style="margin:5px">{{ Energy }} watts per hour</p>
            </div>
            
          </div>
          <div style="width:200px; height:100px; background:rgb(34, 138, 235); color:white; display:flex; justify-content:center; align-items:center; border-radius:10px; margin:20px; border:2px solid black"> 
            <div >
              <p style="margin:5px">Daily operational hours:</p>
              <p style="margin:5px">{{ Operational_hours }} hours</p>
            </div>
            
          </div>
          <div style="width:200px; height:100px; background:rgb(34, 138, 235); color:white; display:flex; justify-content:center; align-items:center; border-radius:10px; margin:20px; border:2px solid black"> 
            <div >
              <p style="margin:5px">Energy Used(daily):</p>
              <p style="margin:5px">{{ Energy/1000*5 }} units</p>
            </div>
            
          </div>
          <div style="width:200px; height:100px; background:rgb(34, 138, 235); color:white; display:flex; justify-content:center; align-items:center; border-radius:10px; margin:20px; border:2px solid black"> 
            <div >
              <p style="margin:5px">Monthly power consumption:</p>
              <p style="margin:5px">{{ Energy/1000*5*30 }} units</p>
            </div>
            
          </div>
          <div style="width:200px; height:100px; background:rgb(34, 138, 235); color:white; display:flex; justify-content:center; align-items:center; border-radius:10px; margin:20px; border:2px solid black"> 
            <div >
              <p style="margin:5px">Monthly savings:</p>
              <p style="margin:5px">{{ Energy/1000*5*30*terrif }} rupees</p>
            </div>
            
          </div>
        </div>
        <div class="col-12 Charts"  >
          <BarChart/>
          
        </div>
        
      </div>
    </div>
    



    <FooterComp/>
    
  </div>
</template>

<script>
// @ is an alias to /src
import HeaderComp from "../components/HeaderComp.vue"
import FooterComp from "../components/FooterComp.vue"
import BarChart from "../components/WeeklyChart.vue"
import weather from "../components/WeatherChart.vue"
import axios from 'axios'


export default {
  name: 'HomeView',
  data(){
    return{
      Energy:undefined,
      terrif:undefined,
      Operational_hours:undefined,
      value:undefined
    }
  },
  components: {
   HeaderComp,FooterComp,BarChart,weather
  },
  mounted(){
    this.func()
  },
  methods:{
    async func(){
      await axios.get('get_solar_data')
      .then(res=>{
        console.log(res)
        this.Energy = res.data["total_watts"]
        this.terrif=res.data['terrif_cost']
        this.Operational_hours=res.data['operational_hours']
        this.value=true
      })
      .catch(err=>{
        console.log(err)
        this.value=false
      })
    }
  }
}
</script>
<style scoped>
body{
  overflow: hidden;
}
.main{
  display: block;
  margin-top:10vh;
  margin-bottom: 10vh;
  padding:0;
  overflow: hidden;
}

.main .container{
  
  display: block;
  overflow: hidden;
}

.main .container .Charts .button_container{
  width:100%;
  border:2px solid black
}
.main .container .charts .button_container{
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  /* align-items: center; */
}

</style>
