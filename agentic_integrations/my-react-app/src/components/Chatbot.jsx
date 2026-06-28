// const Chatbot = () => {
//   return (
//     <div className="w-[800px] h-[600px] bg-slate-900 rounded-2xl border border-slate-700 flex flex-col">

//       {/* Header */}
//       <div className="p-5 border-b border-slate-700">
//         <h2 className="text-white font-bold text-xl">
//           AI Assistant
//         </h2>

//         <p className="text-green-400 text-sm">
//           🟢 Online
//         </p>
//       </div>

//       {/* Messages */}
//       <div className="flex-1 p-5 overflow-y-auto">

//         <div className="bg-slate-700 text-white p-3 rounded-xl w-fit">
//           Hello! How can I help you today?
//         </div>

//         <div className="flex justify-end mt-5">
//           <div className="bg-cyan-500 text-white p-3 rounded-xl w-fit">
//             Create a responsive chatbot UI.
//           </div>
//         </div>

//       </div>

//       {/* Input */}
//       <div className="p-5 border-t border-slate-700 flex gap-3">

//         <input
//           type="text"
//           placeholder="Type a message..."
//           className="flex-1 bg-slate-800 text-white rounded-lg px-4 py-3 outline-none"
//         />

//         <button className="bg-cyan-500 px-5 rounded-lg text-white">
//           Send
//         </button>

//       </div>
//     </div>
//   );
// };

// export default Chatbot;

// import ReactMarkdown from "react-markdown";
// import { useState } from "react";

// const Chatbot = () => {
//   const [input, setInput] = useState("");

//   const [messages, setMessages] = useState([
//     {
//       sender: "bot",
//       text: "Ask Anything",
//     },
//   ]);

//   const sendMessage = async () => {
//     if (!input.trim()) return;

//     const userMessage = {
//       sender: "user",
//       text: input,
//     };

//     // Show user message immediately
//     setMessages((prev) => [...prev, userMessage]);

//     const currentInput = input;
//     setInput("");

//     try {
//       const response = await fetch("http://localhost:8000/chat", {
//         method: "POST",
//         headers: {
//           "Content-Type": "application/json",
//         },
//         body: JSON.stringify({
//           message: currentInput,
//         }),
//       });

//       const data = await response.json();

//       const botMessage = {
//         sender: "bot",
//         text: data.response,
//       };

//       setMessages((prev) => [...prev, botMessage]);
//     } catch (error) {
//       setMessages((prev) => [
//         ...prev,
//         {
//           sender: "bot",
//           text: "Unable to connect to the server.",
//         },
//       ]);
//     }
//   };

//   return (
//     <div className="w-[800px] h-[600px] bg-white rounded-2xl shadow-[0_8px_30px_rgb(0,0,0,0.08)] border border-gray-100 flex flex-col font-sans">

//       {/* Header */}
//       <div className="p-8 border-b border-gray-100 flex flex-col justify-center">
//         <h2 className="text-gray-900 font-bold text-[32px] tracking-tight leading-tight">
//           Hi, Dhiraj
//         </h2>
//         <h3 className="text-gray-500 font-bold text-[32px] tracking-tight leading-tight mt-1">
//           What can I help you with?
//         </h3>
//       </div>

//       {/* Messages */}
//       <div className="flex-1 p-8 overflow-y-auto bg-gray-50/50">
//         {messages.map((msg, index) => (
//           <div
//             key={index}
//             className={`mb-6 flex ${
//               msg.sender === "user"
//                 ? "justify-end"
//                 : "justify-start"
//             }`}
//           >
//             <div
//               className={`p-4 rounded-2xl max-w-[75%] text-[15px] leading-relaxed shadow-sm ${
//                 msg.sender === "user"
//                   ? "bg-[#1A1A1A] text-white rounded-br-sm"
//                   : "bg-white border border-gray-200 text-gray-800 rounded-bl-sm"
//               }`}
//             >
//               {msg.text}
//             </div>
//           </div>
//         ))}
//       </div>

//       {/* Input */}
//       <div className="p-8 bg-white rounded-b-2xl">
//         <div className="flex gap-3 items-center border border-gray-300 rounded-2xl px-2 py-2 focus-within:border-gray-500 focus-within:ring-1 focus-within:ring-gray-500 transition-all shadow-sm">
//           <input
//             type="text"
//             value={input}
//             placeholder="Ask a question or make a request..."
//             onChange={(e) => setInput(e.target.value)}
//             onKeyDown={(e) => {
//               if (e.key === "Enter") {
//                 sendMessage();
//               }
//             }}
//             className="flex-1 bg-transparent text-gray-800 px-4 py-2 outline-none placeholder-gray-400 text-[15px]"
//           />

//           <button
//             onClick={sendMessage}
//             className="bg-[#D4ED31] hover:bg-[#c4dc2e] text-[#131313] font-semibold px-6 py-3 rounded-xl transition-colors flex items-center justify-center shadow-sm"
//           >
//             Send
//           </button>
//         </div>
//       </div>
//     </div>
//   );
// };

// export default Chatbot;

import { useState } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

const Chatbot = () => {
  const [input, setInput] = useState("");

  const [messages, setMessages] = useState([
    {
      sender: "bot",
      text: "Ask Anything",
    },
  ]);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = {
      sender: "user",
      text: input,
    };

    setMessages((prev) => [...prev, userMessage]);

    const currentInput = input;
    setInput("");

    try {
      const response = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          message: currentInput,
        }),
      });

      const data = await response.json();

      const botMessage = {
        sender: "bot",
        text: data.response,
      };

      setMessages((prev) => [...prev, botMessage]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        {
          sender: "bot",
          text: "❌ Unable to connect to the server.",
        },
      ]);
    }
  };

  return (
    <div className="w-[800px] h-[600px] bg-white rounded-2xl shadow-[0_8px_30px_rgb(0,0,0,0.08)] border border-gray-100 flex flex-col font-sans">
      
      {/* Header */}
      <div className="p-8 border-b border-gray-100">
        <h2 className="text-gray-900 font-bold text-[32px] tracking-tight">
          Hi, Dhiraj
        </h2>

        <h3 className="text-gray-500 font-bold text-[32px] tracking-tight">
          What can I help you with?
        </h3>
      </div>

      {/* Messages */}
      <div className="flex-1 p-8 overflow-y-auto bg-gray-50/50">
        {messages.map((msg, index) => (
          <div
            key={index}
            className={`mb-6 flex ${
              msg.sender === "user"
                ? "justify-end"
                : "justify-start"
            }`}
          >
            <div
              className={`p-4 rounded-2xl max-w-[75%] text-[15px] leading-relaxed shadow-sm ${
                msg.sender === "user"
                  ? "bg-[#1A1A1A] text-white rounded-br-sm"
                  : "bg-white border border-gray-200 text-gray-800 rounded-bl-sm"
              }`}
            >
              {msg.sender === "bot" ? (
                <div className="prose prose-sm max-w-none prose-headings:mb-2 prose-p:mb-2 prose-ul:mb-2 prose-li:mb-1">
                  <ReactMarkdown 
                  remarkPlugins={[remarkGfm]}
                  components={{
                    h1: ({ children }) => (
                      <h1 className="text-2xl font-bold mb-4 mt-6">
                        {children}
                      </h1>
                    ),
                
                    h2: ({ children }) => (
                      <h2 className="text-xl font-semibold mb-3 mt-5">
                        {children}
                      </h2>
                    ),
                
                    p: ({ children }) => (
                      <p className="mb-4 leading-7">
                        {children}
                      </p>
                    ),
                
                    ul: ({ children }) => (
                      <ul className="list-disc pl-6 mb-4 space-y-2">
                        {children}
                      </ul>
                    ),
                
                    ol: ({ children }) => (
                      <ol className="list-decimal pl-6 mb-4 space-y-2">
                        {children}
                      </ol>
                    ),
                
                    pre: ({ children }) => (
                      <pre className="bg-gray-100 p-4 rounded-lg overflow-x-auto mb-4">
                        {children}
                      </pre>
                    ),
                  }}
                  >
                    {msg.text}
                  </ReactMarkdown>
                </div>
              ) : (
                msg.text
              )}
            </div>
          </div>
        ))}
      </div>

      {/* Input */}
      <div className="p-8 bg-white rounded-b-2xl">
        <div className="flex gap-3 items-center border border-gray-300 rounded-2xl px-2 py-2 focus-within:border-gray-500 focus-within:ring-1 focus-within:ring-gray-500 transition-all shadow-sm">
          
          <input
            type="text"
            value={input}
            placeholder="Ask a question or make a request..."
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                sendMessage();
              }
            }}
            className="flex-1 bg-transparent text-gray-800 px-4 py-2 outline-none placeholder-gray-400 text-[15px]"
          />

          <button
            onClick={sendMessage}
            className="bg-[#D4ED31] hover:bg-[#c4dc2e] text-[#131313] font-semibold px-6 py-3 rounded-xl transition-colors flex items-center justify-center shadow-sm"
          >
            Send
          </button>
        </div>
      </div>
    </div>
  );
};

export default Chatbot;
