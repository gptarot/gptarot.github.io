import React from 'react';
import { HashRouter, Routes, Route } from 'react-router-dom';
import Home from '../pages/Home';
import Random from '../pages/Random';

const Router: React.FC = (): JSX.Element => {
  return (
    <HashRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="random" element={<Random />} />
      </Routes>
    </HashRouter>
  );
};

export default Router;
