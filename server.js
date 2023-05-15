const http = require('http');

const server = http.createServer((req, res) => {
    if (req.method === 'GET') {
        const searchParams = new URLSearchParams(req.url.split('?')[1]);
        const data = searchParams.get('data');
        console.log(`Received GET request with data: ${data}`);
        console.log("")
    }
    res.end();
});

server.listen(3000, () => {
    console.log('Server is listening on port 3000');
});
