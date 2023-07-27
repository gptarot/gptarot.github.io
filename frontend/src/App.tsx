import { useState } from "react"
import Input from "./components/Input"
import getPrediction from "./services/tarotService"

function App() {
  const [name, setName] = useState("")
  const [dob, setDob] = useState("")
  const [prediction, setPrediction] = useState({
    result: null,
  })

  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const handleSubmit = async (ev: any) => {
    console.log(ev)
    ev.preventDefault();

    const res = await getPrediction();

    if (res) {
      setPrediction(res);
    }
  }

  return (
    <div className="h-screen flex flex-col items-center justify-center bg-background bg-center">
      <form onSubmit={handleSubmit} className="flex flex-col gap-4">
        <Input 
          id="name" 
          label="Your name" 
          onChange={
            // eslint-disable-next-line @typescript-eslint/no-explicit-any
            (ev: any) => setName(ev.target.value)
          } 
          value={name}></Input>
        <Input 
          id="dob" 
          label="Your Day of Birth" 
          onChange={
            // eslint-disable-next-line @typescript-eslint/no-explicit-any
            (ev: any) => setDob(ev.target.value)} 
          value={dob}></Input>
        <div className="flex items-center justify-center">
          <button className="bg-white px-4 py-2 rounded-md">Submit</button>
        </div>
      </form>
      {prediction.result && <div className="bg-white p-4 rounded-md mt-10">{prediction.result}</div>}
    </div>
  )
}

export default App
