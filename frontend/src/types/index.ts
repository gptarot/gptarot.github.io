export interface Prediction {
  result: string;
}

export interface PredictionRequest {
  name: string;
  dob: string;
  question: string;
  pastCard: string;
  presentCard: string;
  futureCard: string;
}

export interface InputProps {
  id: string;
  onChange: (ev: React.ChangeEvent<HTMLInputElement>) => void;
  value: string;
  label: string;
  type?: string;
  error?: string;
}

export interface Cards {
  pastCard: string;
  presentCard: string;
  futureCard: string;
}
