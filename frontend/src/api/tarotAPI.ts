import axios from './axios';
import { AxiosResponse } from 'axios';
import { Prediction } from '../types';

const getPrediction = async (
  name: string,
  dob: string,
  question: string,
  pastCard: string,
  presentCard: string,
  futureCard: string,
): Promise<Prediction | undefined> => {
  const request = {
    name,
    dob,
    question,
    'past-card': {
      name: pastCard,
      isUpRight: true,
    },
    'present-card': {
      name: presentCard,
      isUpRight: true,
    },
    'future-card': {
      name: futureCard,
      isUpRight: true,
    },
  };
  try {
    const response: AxiosResponse<Prediction> = await axios.post('/api', request, {
      headers: { 'Content-Type': 'application/json' },
    });
    return response.data;
  } catch (error) {
    console.log(error);
    return undefined;
  }
};

export default getPrediction;
