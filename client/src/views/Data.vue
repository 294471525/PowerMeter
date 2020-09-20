<template>
    <div>
        <div class="wrapper">
            <div ref="chart" style="width: 400px;height:320px; font-size: 20px"></div>
            <div class="data-wrapper">
                <el-button type="info" plain @click="setVoltage">VOLTAGE
                    <div style="font-size: 20px">{{nodeData.voltage}}</div> </el-button>
                <el-button type="info" plain @click="setCurrent">CURRENT
                    <div style="font-size: 20px">{{nodeData.current}}</div></el-button>
                <el-button type="info" plain @click="setPower">POWER
                    <div style="font-size: 20px">{{nodeData.power}}</div></el-button>
            </div>
        </div>
    </div>

</template>

<script>
    import echarts from 'echarts';

    export default {

        name: "Data",
        data() {
            return {
                nodeData: {},
                chartData: 0,
                flag:0,
                chartTitle:"Voltage"
            }

        },
        methods: {
             getData() {
                const _this = this
                _this.$axios.get('/api/getData',{params:{
                        id:this.id
                    }}).then(function (res) {
                    _this.nodeData = JSON.parse(res.data.data)[0].fields;
                    if(_this.flag === 0){
                        _this.chartData = _this.nodeData["voltage"]
                        _this.chartTitle = "Voltage"
                    }else if(_this.flag === 1){
                        _this.chartData = _this.nodeData["current"]
                        _this.chartTitle = "Current"

                    }else{
                        _this.chartData = _this.nodeData["power"]
                        _this.chartTitle = "Power"

                    }
                });
            },
            setVoltage(){
                const _this = this;
                _this.flag = 0
            },
            setPower(){
                const _this = this;
                _this.flag = 2
            },
            setCurrent(){
                const _this = this
                _this.flag = 1
            }

        },

        mounted() {
            var myChart = echarts.init(this.$refs.chart);
            const _this = this;

            function randomData() {
                now = new Date(+now + 1000);
                var valueName = now.getFullYear() + '/' + (now.getMonth() + 1) + '/' + now.getDate() + ' ' + (now.getHours() >= 10 ? now.getHours() : '0' + now.getHours()) + ':' + (now.getMinutes() >= 10 ? now.getMinutes() : '0' + now.getMinutes())+ ':' + (now.getSeconds() >= 10 ? now.getSeconds() : '0' + now.getSeconds());
                value = _this.chartData;
                return {
                    name: now.toString(),
                    value: [
                        valueName,
                        Math.round(value)
                    ]
                };
            }

            var data = [];
            var now = +new Date('2020-09-02 00:00:00');
            var n_now = new Date(now);
            var n_day = n_now.getDate();

            var c_now = new Date();
            var c_day = c_now.getDate();
            var c_month = c_now.getMonth() + 1;
            var c_year = c_now.getFullYear();



            var value = _this.nodeData;

            if (n_day !== c_day) {
                now = +new Date(c_year + '-' + c_month + '-' + c_day + ' ' + '00:00:00');
            }

            var num = Math.floor((+new Date() - now) / 60000) <= 1 ? 1 : Math.floor((+new Date() - now) / 60000);


            for (var i = 0; i < num; i++) {
                data.push(randomData());
            }

            var option = {
                title: {
                    text: _this.chartTitle,
                    textStyle:{
                        fontSize:20,
                        color:"#B5B682"

                    },
                },
                tooltip: {
                    trigger: 'axis',
                    formatter: function (params) {
                        params = params[0];
                        var date = new Date(params.name);
                        return date.getHours() + ':' + date.getMinutes() + ' ' + date.getDate() + '/' + (date.getMonth() + 1) + '/' + date.getFullYear() + ' : ' + params.value[1];
                    },
                    axisPointer: {
                        animation: false
                    }
                },
                xAxis: {
                    type: 'time',
                    splitLine: {
                        show: false
                    },
                    axisLabel: {
                        show: true,
                        textStyle: {
                            color: '#B5B682',
                            fontSize:'20'
                        }
                    },
                    axisLine:{
                        lineStyle:{
                            color: "#B5B682",
                            width:3
                        }
                    }

                },
                yAxis: {
                    type: 'value',
                    boundaryGap: ['0', '10%'],
                    formatter: function (value, index) {
                        index
                        return value.toFixed(2);
                    },
                    splitLine: {
                        show: false
                    },
                    axisLabel: {
                        show: true,
                        textStyle: {
                            color: '#B5B682',
                            fontSize:'20'
                        }
                    },
                    axisLine:{
                        lineStyle:{
                            color: "#B5B682",
                            width:3
                        }
                    }
                },
                series: [{
                    name: 'powerData',
                    type: 'line',
                    showSymbol: false,
                    hoverAnimation: false,
                    data: data,
                    smooth:true,
                    itemStyle : {
                        width:3,
                        color:{
                            type: 'linear',
                            x: 0,
                            y: 0,
                            x2: 0,
                            y2: 1,
                            colorStops: [{
                                offset: 0, color: '#1CD8D2'
                            }, {
                                offset: 1, color: '#ffffff'
                            }],
                            global: false
                        }
                    },
                    lineStyle:{
                        color: {
                            type: 'linear',
                            x: 0,
                            y: 0,
                            x2: 1,
                            y2: 1,
                            colorStops: [{
                                offset: 0, color: '#ffffff'
                            },{
                                offset: 0.5, color: '#5865FF'
                            }, {
                                offset: 1, color: '#ffffff'
                            }],
                            global: false
                        }
                    },
                    areaStyle: {}

                }]
            };
            setInterval(function () {
                if ((new Date(now)).getDate() !== c_day) {
                    window.history.go(0)
                }
                data.shift();
                data.push(randomData());
                option.title.text = _this.chartTitle
                myChart.setOption(option);
                _this.getData()
            }, 1000);
        },
        created() {
             this.getData();
        }


    }
</script>

<style scoped>
    .wrapper {
        display: grid;
        grid-template-columns: 2fr 1fr;
        grid-gap: 1rem;
    }
    .el-button {
        margin-left: 10px;
        text-align: left;
        font-size: 20px;
        width: 180px;
    }

    .data-wrapper {
        display: grid;
        grid-template-rows:repeat(3, 1fr) ;
        grid-gap: 20px;
    }


</style>

<style>
    .el-button div{
        display: inline-block;
        margin-left: 10px;
        font-size: 30px;
    }
</style>