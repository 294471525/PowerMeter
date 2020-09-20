<template>
    <div>
        <div class="NodeHeader" style="font-size: 30px; color: white">
            <el-button type="text" icon="el-icon-download" @click="dialogVisible = true" style="font-size: 30px" round>Download</el-button>
            Current Node {{nodeData.nodeId?nodeData.nodeId:2}}
            <el-dialog title="Please select a time range" :visible.sync="dialogVisible" width="30%" :before-close="handleClose">
                <div class="block" style="text-align:  center">
                    <el-date-picker
                            v-model="Time"
                            type="datetimerange"
                            align="right"
                            start-placeholder="StartTime"
                            end-placeholder="EndTime"
                            format="yyyy-MM-dd HH:mm:ss"
                            value-format="yyyy-MM-dd HH:mm:ss"
                            :default-time="['12:00:00', '08:00:00']"
                            style="width: 200px; align-content: center"
                    >
                    </el-date-picker>
                </div>
                <span slot="footer" class="dialog-footer">
                    <el-button @click="dialogVisible = false">CANCEL</el-button>
                    <el-button type="primary" @click="dialogVisible = false , downLoad()">CONFIRM</el-button>
                </span>
            </el-dialog>
        </div>
        <div ref="chart" style="width: 100%;height:320px;"></div>
    </div>

</template>

<script>
    import echarts from "echarts";
    import {getOption} from "../store/createOption.js"

    export default {
        name: "Gauge",
        data() {
            return {
                nodeData: {},
                dialogVisible:false,
                Time: [],
                id:4,
            }
        },
        methods: {
            getData() {
                const _this = this
                _this.$axios.get('/api/getData',{params:{
                    id:this.id
                    }}).then(function (res) {
                    _this.nodeData = JSON.parse(res.data.data)[0].fields;
                });
            },
            open() {
                console.log(this.startTime)
            },
            downLoad(){
                const _this = this
                _this.$axios.get('/api/downloadData', {params:{
                    startTime:this.Time[0],
                    endTime:this.Time[1],
                    id:this.id
                    }}).then(
                    res => {
                        if (res.status === 200) {
                            let filename = res.headers['content-disposition'].split(';')[1].replace('filename=', '');
                            let blob = new Blob([res.data], {type: "text/csv"});
                            let a = document.createElement('a');
                            a.download = filename;
                            a.href = URL.createObjectURL(blob);
                            a.click();
                            a.remove()
                        }
                    }
                )
            }
        },
        mounted() {
            const _this = this
            var myChart = echarts.init(this.$refs.chart);
            var option = getOption()

            setInterval(function () {
                _this.getData()
                option.series[0].data[0].value = _this.nodeData.power;
                option.series[1].data[0].value = _this.nodeData.current;
                option.series[2].data[0].value = _this.nodeData.voltage;
                myChart.setOption(option, true);
                window.onresize = function(){
                    myChart.resize();
                }
            }, 1000);
        }
    }
</script>

<style scoped>
    .NodeHeader {
        text-align: left;
        margin-left: 20px;
        margin-right: 20px;
    }
</style>