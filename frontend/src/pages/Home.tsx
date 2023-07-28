import { useState } from 'react';
import getPrediction from '../services/tarotService';
import Input from '../components/Input';

const Home = () => {
  const [name, setName] = useState('');
  const [dob, setDob] = useState('');
  const [question, setQuestion] = useState('');
  const [prediction, setPrediction] = useState({
    result: null,
  });

  const handleSubmit = async (ev: any) => {
    ev.preventDefault();

    const res = await getPrediction();

    if (res) {
      setPrediction(res);
    }
  };

  return (
    <div className="h-screen flex flex-col items-center justify-center bg-background bg-center">
      <form onSubmit={handleSubmit} className="flex flex-col gap-4">
        <Input id="name" label="Your name" onChange={(ev: any) => setName(ev.target.value)} value={name} />
        <Input id="dob" label="Your Day of Birth" onChange={(ev: any) => setDob(ev.target.value)} value={dob} />
        <Input
          id="question"
          label="Your Question"
          onChange={(ev: any) => setQuestion(ev.target.value)}
          value={question}
        />
        <div className="flex items-center justify-center">
          <button className="bg-white px-4 py-2 rounded-md">Submit</button>
        </div>
      </form>
      {prediction.result && <div className="bg-white p-4 rounded-md mt-10">{prediction.result}</div>}
    </div>
  );
};

export default Home;
