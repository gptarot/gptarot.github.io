import { useState } from 'react';
import getPrediction from '../services/tarotService';
import Input from '../components/Input';
import { Prediction } from '../types';

const Home = () => {
  const [name, setName] = useState<string>('');
  const [dob, setDob] = useState<string>('');
  const [question, setQuestion] = useState<string>('');
  const [prediction, setPrediction] = useState<Prediction | null>(null);

  const handleSubmit = async (ev: React.FormEvent<HTMLFormElement>) => {
    ev.preventDefault();

    const response: Prediction = await getPrediction();

    if (response) {
      setPrediction(response);
    }
  };

  return (
    <div className="h-screen flex flex-col items-center justify-center bg-background bg-center">
      <form onSubmit={handleSubmit} className="flex flex-col gap-4">
        <Input
          id="name"
          label="Your name"
          onChange={(ev: React.ChangeEvent<HTMLInputElement>) => setName(ev.target.value)}
          value={name}
        />
        <Input
          id="dob"
          label="Your Day of Birth"
          onChange={(ev: React.ChangeEvent<HTMLInputElement>) => setDob(ev.target.value)}
          value={dob}
        />
        <Input
          id="question"
          label="Your Question"
          onChange={(ev: React.ChangeEvent<HTMLInputElement>) => setQuestion(ev.target.value)}
          value={question}
        />
        <div className="flex items-center justify-center">
          <button className="bg-white px-4 py-2 rounded-md">Submit</button>
        </div>
      </form>
      {prediction && <div className="bg-white p-4 rounded-md mt-10">{prediction.result}</div>}
    </div>
  );
};

export default Home;
