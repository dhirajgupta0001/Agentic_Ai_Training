// import { useState } from 'react'
// import reactLogo from './assets/react.svg'
// import viteLogo from './assets/vite.svg'
// import heroImg from './assets/hero.png'
// import './App.css'
// import Chatbot from './components/Chatbot'

// function App() {
//   const [count, setCount] = useState(0)

//   return (
//     <>
//       <section className='flex flex-col justify-center w-full min-h-screen'>
//         <div className='header w-full h-auto py-3 bg-blue-900'>
//            <h3 className='text-teal-600 font-bold text-7xl'> Building Agentic AI</h3> 
//         </div>
//         <div>
//           <Chatbot />
//         </div>
//       </section>
//     </>
//   )
// }

// export default App
// import { BrowserRouter, Routes, Route } from "react-router-dom";
// import Header from "./components/header";
// import Container from "./components/container";
// import Home from "./pages/Home";
// import AgenticAI from "./pages/AgenticAI";
// import Marketplace from "./pages/Marketplace";
// import Settings from "./pages/Settings";

// function App() {
//   return (
//     // <div className="min-h-screen bg-[#030B2F]">

//     //   <Header />

//     //   <Container />

//     // </div>
//     <BrowserRouter>

//       <div className="min-h-screen bg-[#020817]">

//         <Header />
//         <Container />

//         <Routes>
//           <Route path="/" element={<Home />} />
//           <Route path="/agentic-ai" element={<AgenticAI />} />
//           <Route path="/marketplace" element={<Marketplace />} />
//           <Route path="/settings" element={<Settings />} />
//         </Routes>

//       </div>

//     </BrowserRouter>
//   );
// }

// export default App;

import { BrowserRouter, Routes, Route } from "react-router-dom";

import Header from "./components/header";
import Container from "./components/container"
import Home from "./pages/Home";
import AgenticAI from "./pages/AgenticAI";
import Marketplace from "./pages/Marketplace";
import Settings from "./pages/Settings";
import AboutMe from "./pages/AboutMe";

function App() {
  //<Container />
  return (
    <BrowserRouter>
      <div className="min-h-screen bg-gray-50 font-sans">
        <Header />
        
        <Routes>
          <Route path="/" element={<Home />} />

          <Route path="/agentic-ai" element={<AgenticAI />} />

          <Route
            path="/marketplace"
            element={<Marketplace />}
          />

          <Route
            path="/settings"
            element={<Settings />}
          />

          <Route
            path="/aboutme"
            element={<AboutMe />}
          />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
