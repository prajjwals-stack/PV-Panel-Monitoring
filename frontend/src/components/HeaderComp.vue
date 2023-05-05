<template>
    <div class="header">
        <h4 class="companyLogo">SOLAR PANEL MONITORING</h4>
        
        <div class="bar">
            <p style="color:white"><a href="/home" style="color:white; text-decoration:none;">Home</a></p>
            <p style="color:white"><a href="/bidding" style="color:white; text-decoration:none;">Bidding</a></p>
            <p style="color:white"><a href="/Forecast" style="color:white; text-decoration:none;">Forecast</a></p>
            <p style="color:white"><a href="/Info" style="color:white; text-decoration:none;">Info</a></p>
        </div>


    </div>

</template>

<script>

export default{
    props:['user'],
    

methods: {
    handleClick(){
        localStorage.setItem('token',null);
        this.$router.push('/login');
     }
}
}

</script>



<style>
.header{
    position:fixed;
    top:0;
    background: #FFFFFF;
    left:0;
    width:100%;
    height:9%;
    text-align:center;
    display:flex;
    flex-direction:row;
    justify-content:space-between;
    align-items:last baseline;
    border-bottom: 1px solid rgb(115, 137, 152);
    background: black;
    color:white
}
.header .companyLogo{
    height:40px;
}
.header .bar{
    width:30%;
    display: flex;
    flex-direction:row;
    justify-content: space-around;
 
}
</style>