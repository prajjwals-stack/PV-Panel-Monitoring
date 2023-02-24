<template>
  <div class="main">
    <HeaderComp/>
    <div class="container">
      <div class="row">
        <!-- <div class="col-6"><weather/></div> -->
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


export default {
  name: 'HomeView',
  components: {
   HeaderComp,FooterComp,BarChart,weather
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
