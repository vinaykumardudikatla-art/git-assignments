//express application to sevre the html file
const express = require('express');
const app = express();

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.set('view engine', 'ejs');

const URL = process.env.BACKEND_URL || 'http://localhost:5000';

app.get('/api/data', async (req, res) => {
    try {
        const response = await fetch(`${URL}/getdata`);
        const data = await response.json();
        res.json(data);
    } catch (error) {
        console.error('Error fetching data from backend:', error);
        res.status(500).json({ error: 'Failed to fetch data from backend' });
    }
});
app.post('/api/register', async (req, res) => {
    try {
        const response = await fetch(`${URL}/register`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username: req.body.username, password: req.body.password })
        });
        const data = await response.json();
        res.json(data);
    } catch (error) {
        console.error('Error posting data to backend:', error);
        res.status(500).json({ error: 'Failed to post data to backend' });
    }
});
app.get('/', (req, res) => {
    res.render('index');
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
}); 