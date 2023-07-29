import { useState } from 'react';
import { CardInfo } from '../types';
import { getRandomCard } from '../api/tarotAPI';

const Random: React.FC = (): JSX.Element => {
  const [cardInfo, setCardInfo] = useState<CardInfo | null>(null);

  const handleRandomCard = async (): Promise<void> => {
    const response: CardInfo | undefined = await getRandomCard();

    if (response) {
      setCardInfo(response);
    }
  };

  return (
    <div className="z-10">
      <button onClick={handleRandomCard} className="bg-white py-2 px-4 rounded-md shadow-sm">
        Random Card
      </button>
      <div className="px-4 py-2 mt-4">
        <p className="text-white">Hello World</p>
      </div>
      {cardInfo && <p>Random Successfully</p>}
    </div>
  );
};

export default Random;
