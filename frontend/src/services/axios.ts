import axios from 'axios';

export default axios.create({
  baseURL: 'https://gptarot-api-production.up.railway.app/',
});
