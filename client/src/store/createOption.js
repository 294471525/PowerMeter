import echarts from "echarts";

var windowWidth = document.documentElement.clientWidth;
function nowSize(val,initWidth=1080){
    console.log(windowWidth)
    console.log(val * (windowWidth/initWidth))
    return val * (windowWidth/initWidth);
}


export function getOption() {
    var ftSize = nowSize(15)
    var titleSize = nowSize(30)
    var option = {
        tooltip: {
            formatter: "{a} <br/>{c} {b}",
            textStyle:{
                fontSize: nowSize(30)
            }
        },
        toolbox: {
            show: true,
            feature: {
                restore: {show: true},
                saveAsImage: {show: false}
            }
        },
        series: [
            {
                name: 'Power',
                type: 'gauge',
                z: 3,
                min: 0,
                max: 3000,
                splitNumber: 15,
                radius: '80%',
                axisLine: {
                    lineStyle: {
                        width: nowSize(20),
                        color: [
                            [1,new echarts.graphic.LinearGradient(0, 0, 1, 0, [
                                {
                                    offset: 0.1,
                                    color: "#FFC600"
                                },
                                {
                                    offset: 0.6,
                                    color: "#30D27C"
                                },
                                {
                                    offset: 1,
                                    color: "#0B95FF"
                                }
                            ])
                            ]
                        ]
                    },

                },
                axisLabel:{
                    textStyle:{
                        fontSize:ftSize,
                        color:"#ffff",
                        fontWeight:'bolder'
                    }
                },
                axisTick: {
                    length: nowSize(15),
                    lineStyle: {
                        color: 'auto'
                    }
                },
                splitLine: {
                    length: nowSize(30),
                    lineStyle: {
                        color: 'auto'
                    }
                },
                title: {
                    textStyle: {
                        fontWeight: 'bolder',
                        fontSize: titleSize,
                        fontStyle: 'italic',
                        color:'#ffff'
                    }
                },

                detail: {
                    textStyle: {
                        fontWeight: 'bolder',
                        fontSize:30,
                        color:'#ffff'

                    }
                },
                data: [{value: 0, name: 'Power/W'}]
            },
            {
                name: 'current',
                type: 'gauge',
                center: ['20%', '55%'],
                radius: '50%',
                min: 0,
                max: 20,
                endAngle: 45,
                splitNumber: 10,
                axisLine: {
                    lineStyle: {
                        width: nowSize(15),
                        color: [
                            [1,new echarts.graphic.LinearGradient(0, 0, 1, 0, [
                                {
                                    offset: 0.1,
                                    color: "#FFC600"
                                },
                                {
                                    offset: 0.6,
                                    color: "#30D27C"
                                },
                                {
                                    offset: 1,
                                    color: "#0B95FF"
                                }
                            ])
                            ]
                        ]
                    }
                },
                axisLabel:{
                    textStyle:{
                        fontSize:ftSize,
                        color:"#ffff",
                        fontWeight:'bolder'
                    }
                },
                axisTick: {
                    length: nowSize(12),
                    lineStyle: {
                        color: 'auto'
                    }
                },
                splitLine: {
                    length: nowSize(20),
                    lineStyle: {
                        color: 'auto'
                    }
                },
                pointer: {
                    width: nowSize(5)
                },
                title: {
                    offsetCenter: [0, '-30%'],
                    color:"#ffff",
                    fontSize:nowSize(20),
                    fontWeight:'bolder'
                },
                detail: {
                    textStyle: {
                        fontWeight: 'bolder',
                        color:'#ffff',
                        fontSize:20
                    }
                },
                data: [{value: 0, name: 'Current/A'}]
            },
            {
                name: 'Voltage',
                type: 'gauge',
                center: ['80%', '55%'],
                radius: '50%',
                min: 0,
                max: 400,
                startAngle: 135,
                endAngle: -35,
                splitNumber: 10,
                axisLine: {
                    lineStyle: {
                        width: nowSize(15),
                        color: [
                            [1,new echarts.graphic.LinearGradient(0, 0, 1, 0, [
                                {
                                    offset: 0.1,
                                    color: "#FFC600"
                                },
                                {
                                    offset: 0.6,
                                    color: "#30D27C"
                                },
                                {
                                    offset: 1,
                                    color: "#0B95FF"
                                }
                            ])
                            ]
                        ]
                    }
                },

                axisTick: {
                    splitNumber: 5,
                    length: nowSize(12),
                    lineStyle: {
                        color: 'auto'
                    }
                },
                axisLabel:{
                    textStyle:{
                        fontSize:ftSize,
                        color:"#ffff",
                        fontWeight:'bolder'
                    }
                },

                splitLine: {
                    length: ftSize,
                    lineStyle: {
                        color: 'auto'
                    }
                },
                pointer: {
                    width: nowSize(2)
                },
                title: {
                    offsetCenter: [0, '-30%'],
                    color:"#ffff",//
                    textStyle:{
                        fontWeight: "bolder",
                        fontSize:nowSize(20)
                    }
                },
                detail: {
                    textStyle: {
                        fontWeight: 'bolder',
                        color:'#ffff',
                        fontSize:20
                    }
                },
                data: [{value: 0, name: 'Voltage/V'}]
            },

        ]
    };
    return option
}