import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import { fetchData } from './test';

function App() {
  const [count, setCount] = useState(0)
  const [data, setData] = useState({
    result: ''
  });

  useEffect(() => {
    const handleFetchData = async () => {
      const res = await fetchData();

      if (res) {
        setData(res);
      }
    }
    handleFetchData();
  }, [])

  return (
    <>
      <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <p>{data?.result}</p>
      <p>This is my voice one day learning Eng Breaking</p>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>Hello World</p>
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
      <p className='text-red-600'>Hello World</p>
    </>
  )
}

export default App
