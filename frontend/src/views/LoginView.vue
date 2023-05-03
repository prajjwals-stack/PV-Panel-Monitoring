<template>
    <div>
    <Header_comp/>
    
    <div class="error-div">
        <div v-if="state.framedata==401" class="alert alert-danger error" role="alert">
        {{state.error}}
        </div>
        <div v-if="state.framedata==456" class="alert alert-danger error" role="alert">
        {{state.error}}
        </div>

    </div>
    <div class="box">
        
        <div class="form-container">
            
                <form v-on:submit.prevent="submitHandler">
                    <h4 >Login</h4>
                    
                        
                                <div class="form-group">
                                    <label>Username</label>
                                    <input type="text" class=" form-control form-control-sm " v-model="state.username"   />
                                    <span v-if="v$.username.$error">
                                        {{ v$.username.$errors[0].$message }}
                                    </span>
                                </div>

                                <div class="form-group">
                                    <label>Password</label>
                                    <input type="password" class="form-control form-control-sm" v-model="state.password"/>
                                    <span v-if="v$.password.$error">
                                        {{ v$.password.$errors[0].$message }}
                                    </span>
                                </div>

                                <button type="submit" class="btn btn-primary btn-sm btn-block">
                                    Sign In
                                </button>

                                
                        
                    <div class="signup-div">
                        <p class="text-center mb-0 pb-0">Don’t have an account?</p>
                        <p class="forgot-password text-center ">
                            <router-link to="/register">Sign Up</router-link>
                        </p>
                    
                    </div>
                </form>
           
         </div>    
        
    </div>



    





    <Footer_comp/>
</div>
</template>

<script>
import Header_comp from "../components/HeaderComp.vue"
import Footer_comp from "../components/FooterComp.vue"
import useValidate from '@vuelidate/core';
import { required } from '@vuelidate/validators';
import {reactive, computed} from 'vue';
import axios from 'axios';
axios.defaults.withCredentials = true;






export default{
    
    components: {
    Header_comp,
    Footer_comp
    },
    
    setup(){
        const state=reactive(
            {
            
            username:"",
            password:"",
            framedata:0,
            error:""

        });
        const rules = computed(() => {
            return{
        
            username:{ required },
            password:{ required },
            
            }

        });
        const v$ = useValidate(rules, state);
        return { state, v$ };
    },
    props:['user'],
    
    methods: { 
        async submitHandler(){
            const isFormCorrect =await this.v$.$validate()
            if(!isFormCorrect)return
            const form= new FormData()
            form.append("username",this.state.username)
            form.append("password",this.state.password)
            await axios.post('login',form).then(
                    (res)=>{
                        
                        localStorage.setItem('token',res.data["access_token"]);
                        window.location = "/home";

                       }
                ).catch(
                    err=>{
                        // this.state.framedata=err.response.status;
                        // this.state.error=err.response.data.detail;
                        // console.log(this.state.framedata)
                        console.log(err)
                    }
                )
               
        },
        
        
         },
        
    }

</script>


<style >
body{
    background-color:#DEEBF7 ;
    
}
.error-div{
    margin:6vh;
    display: flex;
    justify-content: center;
    align-items: center;
    
}
.error-div .error{
    border-radius: 45px;
    width:50%

}
.box{
    margin-top: 100px;
    display:flex;
    justify-content:center;
    
    
}
.box .form-container{
    position:fixed;
    width:350px;
    background-color:#FFFFFF;
    display:flex;
    justify-content:center;
    border-radius:5px ;
    padding-top:10px;
    

}
.box .form-container form{
    width:75%;
}
.box .form-container form h4{
    padding:5px;
}
.box .form-container form button{
    margin-top:15px;
    border-radius:5px ;
}
.box .form-container form .form-group{
    padding:0%;
    margin-bottom:5px;
}
.box .form-container form .signup-div{
    margin-bottom:0%;
    padding-bottom: 0%;
}
.box .form-container form .signup-div .forget-password{
    margin-bottom:0%;
    padding-bottom: 0%;
}
.box .form-container form .form-group input{
    border-radius:5px ;
}
.box .form-container form .form-group label{
    padding:0%;
    margin:0%;
    display:flex;
    justify-content:flex-start;
    
}


</style>
