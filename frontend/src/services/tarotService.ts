import axios from "axios";

const getPrediction = async () => {
    try {
        const response = await axios.get("https://backend-gptarot.vercel.app/api", {
            headers: { 'Content-Type': 'application/json' },
        });
        return response.data;
    } catch (error) {
        console.log(error);
    }
}

export default getPrediction;