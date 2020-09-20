<template>
    <div style="height: 600px">
        <div>
            <el-table :data="nodeList"  style="width: 100%; font-size:20px;" :row-style="RowStyle" >
                <el-table-column  label="NodeId"  prop="pk"> </el-table-column>
                <el-table-column label="Name" prop="fields.name">
                    <template slot-scope="scope"> <el-input v-model="scope.row.fields.name" style="font-size: 20px"></el-input></template>
                </el-table-column>
                <el-table-column align="right">
                    <template slot-scope="scope">
                        <el-button size="mini" @click="changeName(scope.$index, scope.row)" style="font-size: 20px">Edit</el-button>
                    </template>
                </el-table-column>
            </el-table>
        </div>

        <div class = "buttons-bottom" style =  "margin-top:20px;">
            <el-button type="info" round style="font-size: 20px">ADD NODE</el-button>
            <el-button type="danger" round style="font-size: 20px; margin-left: 30px">REMOVE NODE </el-button>
        </div>

    </div>
</template>

<script>
    export default {
        name: "setting",
        data(){
            return{
                nodeList:[],
                dialogVisible:false,

            }
        },
        methods:{
            getNodeList(){
                const _this = this
                _this.$axios.get('/api/nodeList').then(function (res) {
                    console.log(JSON.parse(res.data.nodeList));
                    _this.nodeList = JSON.parse(res.data.nodeList);
                });
            },
            RowStyle({ row, rowIndex }) {
                row
                rowIndex
                return 'background-color: pink'
            },
            changeName(index, newName){
                console.log(newName)
            }

        },
        created() {
            this.getNodeList()
        }

    }
</script>

<style >
    .buttons-bottom{
        position:fixed;
        bottom:50px;
        left: 20px;
    }
    .buttons-bottom .el-button{
        font-size: 20px;
        margin-left: 30px;
        padding-left: 20px;
    }
    .el-table{
        height: 500px;
    }
</style>