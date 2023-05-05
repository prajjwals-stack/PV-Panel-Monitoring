<template>
    <div>
    <Header_comp/>
    <div class="error-div">
        <div v-if="state.framedata==401" class="alert alert-danger error" role="alert">
        {{state.error}}
        </div>
    </div>
    <div class="box">
        <div class="form-container">
            
                <form @submit.prevent="submitHandler">
                    <h4 >Sign Up</h4>
                    
                                <div class="form-group">
                                    <label>Email address</label>
                                    <input type="email" class=" form-control form-control-sm"  v-model="state.email" />
                                    <span v-if="v$.email.$error">
                                        {{ v$.email.$errors[0].$message }}
                                    </span>
                                </div>

                                <div class="form-group">
                                    <label>Name</label>
                                    <input type="text" class=" form-control form-control-sm" v-model="state.username" />
                                    <span v-if="v$.username.$error">
                                        {{ v$.username.$errors[0].$message }}
                                    </span>
                                </div>
                                <div class="form-group">
                                    <label>Mobile Number</label>
                                    <input type="number" class=" form-control form-control-sm"  v-model="state.number" />
                                    <span v-if="v$.number.$error">
                                        {{ v$.number.$errors[0].$message }}
                                    </span>
                                </div>
                                

                                <div class="form-group">
                                    <label>Password</label>
                                    <input type="password" class="form-control form-control-sm" v-model="state.password"/>
                                    <span v-if="v$.password.$error">
                                        {{ v$.password.$errors[0].$message }}
                                    </span>

                                   
                                </div>
                                <div class="form-group">
                                    <label> Confirm Password</label>
                                    <input type="password" class="form-control form-control-sm" v-model="state.confirm" />
                                    <span v-if="v$.confirm.$error">
                                        {{ v$.confirm.$errors[0].$message }}
                                    </span>
                                </div>

                                <button type="submit" class="btn btn-primary btn-sm btn-block">
                                    Sign In
                                </button>
                                <div class="login-div">
                                    <p class="text-center mb-0 pb-0">Already have an account?</p>
                                    <p class="forgot-password text-center">
                                        <router-link to="/">Log In</router-link>
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
import { required, email, minLength, sameAs } from '@vuelidate/validators'
import {reactive, computed} from 'vue';
import axios from 'axios';
axios.defaults.withCredentials = true;

export default{
    components: {
    Header_comp,
    Footer_comp,
    
    },
    setup(){
        const state=reactive(
            {
            email:"",
            username:"",
            number:"",
            password:"",
            confirm:"",
            framedata:0,
            error:""

        });
        const rules = computed(() => {
            return{
            email:{ required, email },
            username:{ required },
            number:{ required },
            password:{ required ,minLength:minLength(8)},
            confirm:{ required , sameAs:sameAs(state.password)}
            }

        });
        const v$ = useValidate(rules, state);
        return { state, v$ };
    
    },
    methods: {
        async submitHandler(){
            const isFormCorrect =await this.v$.$validate()
            if(!isFormCorrect)return
           await axios.post('signup',{
                email: this.state.email,
                username: this.state.username,
                password:this.state.password,
            })
            .then(()=>{
                this.$router.push('/')
            }).catch((err)=>{
                this.state.framedata=err.response.status;
                this.state.error=err.response.data.detail;
                console.log(this.state.framedata)
              
                
            })
                
            
            

            
        }

    }
    

}
</script>

<style scoped >
body{
    overflow: scroll;
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
    margin-top: 50px;
    display:flex;
    justify-content:center;
    
}
.box .form-container{
    width:400px;
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
.box .form-container form .login-div{
    margin-bottom:0%;
    padding-bottom: 0%;
}
.box .form-container form .login-div .forget-password{
    margin-bottom:0%;
    padding-bottom: 0%;
}
.box .form-container form .form-group input{
    border-radius:5px ;
    background-color:#FFFFFF;
}
.box .form-container form .form-group label{
    padding:0%;
    margin:0%;
    display:flex;
    justify-content:flex-start;
    
}




</style>