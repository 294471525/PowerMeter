module.exports = {
    devServer: {
        proxy: {
            '/api': {
                target: 'http://192.168.0.101:8000',
                ws: true,
                changeOrigin: true
            }
        }
    }
};