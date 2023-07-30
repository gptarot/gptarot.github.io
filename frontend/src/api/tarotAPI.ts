import axios from './axios';
import { AxiosResponse } from 'axios';
import { CardInfo, Prediction } from '../types';

export const getPrediction = async (
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

export const getRandomCard = async (random: number | null): Promise<CardInfo | undefined> => {
  if (random === null) return undefined;
  try {
    const response: AxiosResponse<CardInfo> = await axios.get(
      `https://raw.githubusercontent.com/gptarot/gptarot.github.io/main/static/card-info/${random}.json`,
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
