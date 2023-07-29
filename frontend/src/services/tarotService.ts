import { AxiosResponse } from 'axios';
import axios from './axios';
import { Prediction } from '../types';

const getPrediction = async (
  name: string,
  dob: string,
  question: string,
  pastCard: string,
  presentCard: string,
  futureCard: string,
): Promise<Prediction | undefined> => {
  try {
    const response: AxiosResponse<Prediction> = await axios.post(
      '/api',
      {
        name,
        dob,
        question,
        'past-card': {
          name: pastCard,
          isUpright: true,
        },
        'present-card': {
          name: presentCard,
          isUpright: true,
        },
        'future-card': {
          name: futureCard,
          isUpright: true,
        },
      },
      {
        headers: { 'Content-Type': 'application/json' },
      },
    );
    return response.data;
  } catch (error) {
    console.log(error);
    return undefined;
  }
};

export default getPrediction;
