<template>
    <div>
        <el-container>
            <el-header>PowerMeter</el-header>
            <el-main><el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="ruleForm">
                <el-form-item label="username" prop="username">
                    <el-input v-model="ruleForm.name"></el-input>
                </el-form-item>
                <el-form-item label="password" prop="password">
                    <el-input v-model="ruleForm.name"></el-input>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="submitForm('ruleForm')">submit</el-button>
                    <el-button @click="resetForm('ruleForm')">reset</el-button>
                </el-form-item>
            </el-form>
            </el-main>
        </el-container>
    </div>
</template>

<script>
    export default {
        name: "Login",
        data() {
            return {
                ruleForm: {
                    name: '',
                    region: '',
                    date1: '',
                    date2: '',
                    delivery: false,
                    type: [],
                    resource: '',
                    desc: ''
                },
                rules: {
                    username: [
                        { required: true, message: 'Please enter username', trigger: 'blur' },
                    ],
                    password: [
                        { required: true, message: 'Please enter password', trigger: 'change' }
                    ],
                }
            };
        },
        methods: {
            submitForm(formName) {
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        alert('submit!');
                    } else {
                        console.log('error submit!!');
                        return false;
                    }
                });
            },
            resetForm(formName) {
                this.$refs[formName].resetFields();
            }
        }
    }
</script>

<style scoped>
    .ruleForm {
        max-width: 500px;
        margin:0 auto;
    }
</style>