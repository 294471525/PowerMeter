<template>
    <div>
        <el-container style="height: 100%; border: 1px solid #eee">
            <el-container>
                <el-header style="text-align: right; font-size: 20px; padding: 0">
                    <el-menu :default-active="activeIndex2" class="header-menu" mode="horizontal"  @select="handleSelect" background-color="#30323D" text-color="#fff" active-text-color="#ffd04b">
                        <el-menu-item index="1" style="font-size:20px" @click="toGauge" >Dashboard</el-menu-item>
                        <el-menu-item index="4" style="font-size:20px" @click="toGraph" >Graph</el-menu-item>
                        <el-submenu index="2" style="font-size:20px">
                            <template slot="title" style="font-size:20px">Node List</template>
                            <template v-for = "list in NodeList" style="font-size:20px">
                                <el-menu-item v-bind:index="2-list.pk" :key="list.id">Node{{list.pk}} : {{list.fields.name}}</el-menu-item>
                            </template>
                        </el-submenu>
                        <el-menu-item index="3" style="font-size:20px" @click="toSetting">Setting</el-menu-item>
                    </el-menu>
                </el-header>
                <el-main>
                    <router-view></router-view>
                </el-main>
            </el-container>
        </el-container>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                NodeList:[],
                fullscreenLoading: false
            }
        },
        methods:{
             nowSize(val,initWidth=1440){
                 var windowWidth = document.documentElement.clientWidth;
            return val * (windowWidth/initWidth);
            },
            addNode(){
                this.fullscreenLoading = true;
                setTimeout(() => {
                    this.fullscreenLoading = false;
                    alert("Time out, add node fail")
                }, 2000);
            },
            getNodeList(){
                const _this = this
                _this.$axios.get('/api/nodeList').then(function (res) {
                    _this.NodeList = JSON.parse(res.data.nodeList);
                });
            },
            toSetting(){
                this.$router.push("/setting")
            },
            toGauge(){
                this.$router.push("/gauge")
            },
            toGraph(){
                this.$router.push("/data")
            }


        },
        created() {
            this.getNodeList()
        }
    };
</script>

<style >
    .el-container .el-header {
        line-height: 60px;
        padding: 0;
        width: 100%;
        background-color: #006E90;

    }

    .header-menu {
        width: 100%;
    }

    .el-menu--horizontal>.el-submenu .el-submenu__title {
        height: 60px;
        line-height: 60px;
        border-bottom: 2px solid transparent;
        color: #fff;
        font-size: 20px;
    }
    .el-main{
        background-color: #28666E;
    }

</style>
