import { useState } from 'react';
import { CardInfo } from '../types';
import { getRandomCard } from '../api/tarotAPI';
import { Link } from 'react-router-dom';

const Random: React.FC = (): JSX.Element => {
  const [cardInfo, setCardInfo] = useState<CardInfo | null>(null);
  const [random, setRandom] = useState<number | null>(null);

  const handleRandomCard = async (): Promise<void> => {
    setRandom(Math.floor(Math.random() * 78) + 1);
    const response: CardInfo | undefined = await getRandomCard(random);

    if (response) {
      setCardInfo(response);
    }
  };

  return (
    <>
      <Link to="/" className="fixed top-2 left-2 p-4 text-white">
        Home
      </Link>
      <div className="z-10 flex flex-col items-center justify-center">
        {cardInfo && (
          <div className="flex gap-10">
            <div className="text-white leading-6 max-w-3xl">
              <p>{`Name: ${cardInfo.name}`}</p>
              <p>{`Arcana: ${cardInfo.arcana}`}</p>
              <p>{`Suit: ${cardInfo.suit}`}</p>
              <p>Fortune Telling:</p>
              <ul className="list-disc list-inside my-1">
                {cardInfo.fortune_telling.map((fortune: string, index: number) => (
                  <li key={index}>{fortune}</li>
                ))}
              </ul>
              <p>
                Keywords: <span className="text-yellow-300">{cardInfo.keywords.join(', ')}</span>
              </p>
              <p>Light Meaning: </p>
              <ul className="list-disc list-inside my-1">
                {cardInfo.meanings.light.map((meaning: string, index: number) => (
                  <li key={index}>{meaning}</li>
                ))}
              </ul>
              <p>Shadow Meaning: </p>
              <ul className="list-disc list-inside my-1">
                {cardInfo.meanings.shadow.map((meaning: string, index: number) => (
                  <li key={index}>{meaning}</li>
                ))}
              </ul>
              <p>{`Archetype: ${cardInfo.Archetype}`}</p>
              <p>{`Hebrew Alphabet: ${cardInfo['Hebrew Alphabet']}`}</p>
              <p>{`Numerology: ${cardInfo.Numerology}`}</p>
              <p>{`Elemental: ${cardInfo.Elemental}`}</p>
              <p>{`Mythical/Spiritual: ${cardInfo['Mythical/Spiritual']}`}</p>
            </div>
            <img
              src={`https://raw.githubusercontent.com/gptarot/gptarot.github.io/main/static/cards/${cardInfo.img}`}
              alt=""
            />
          </div>
        )}
        <button onClick={handleRandomCard} className="bg-white py-2 px-4 mt-4 rounded-md shadow-sm">
          Random Card
        </button>
      </div>
    </>
  );
};

export default Random;
