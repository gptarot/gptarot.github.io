import React from 'react';
import { Child } from '../../types';

const DefaultLayout: React.FC<Child> = ({ children }) => {
  return (
    <div className="bg-[#21212c] h-screen flex flex-col items-center justify-center relative">
      <div className="absolute inset-0 bg-background bg-center opacity-20" />
      {children}
    </div>
  );
};

export default DefaultLayout;
