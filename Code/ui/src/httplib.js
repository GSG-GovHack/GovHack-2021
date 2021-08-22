import axios from 'axios';

const http = axios.create({
    baseURL: 'http://clover-api:8000',
    timeout: 1000,
});

export default http;