// const AboutMe = () => {
//   return (
//     <div className="min-h-screen bg-[#020B38] text-white p-10">

//       <div className="max-w-5xl mx-auto">

//         <h1 className="text-5xl font-bold mb-8">
//           About Me
//         </h1>

//         <div className="bg-slate-900 rounded-2xl p-8">

//           <h2 className="text-3xl font-semibold">
//             Dhiraj Kumar
//           </h2>

//           <p className="mt-4 text-gray-300 text-lg">
//             Developer and Engineer passionate about React,
//             AI, Agentic Systems, and modern web technologies.
//           </p>

//           <div className="mt-8">
//             <h3 className="text-2xl font-semibold">
//               Skills
//             </h3>

//             <div className="flex flex-wrap gap-3 mt-4">
//               <span className="bg-cyan-600 px-4 py-2 rounded-lg">
//                 Java
//               </span>

//               <span className="bg-cyan-600 px-4 py-2 rounded-lg">
//                 AI
//               </span>

//               <span className="bg-cyan-600 px-4 py-2 rounded-lg">
//                 MySQL
//               </span>

//               <span className="bg-cyan-600 px-4 py-2 rounded-lg">
//                 Python
//               </span>

//               <span className="bg-cyan-600 px-4 py-2 rounded-lg">
//                 AI Agents
//               </span>
//             </div>
//           </div>
            
//         </div>
        

//       </div>
      

//     </div>
    
//   );
// };

// export default AboutMe;

const AboutMe = () => {
  return (
    <div className="p-10 font-sans">

      <div className="max-w-5xl mx-auto">

        <h1 className="text-[40px] font-bold mb-8 text-gray-900 tracking-tight">
          About Me
        </h1>

        <div className="bg-white rounded-2xl p-8 shadow-sm border border-gray-100">

          <h2 className="text-3xl font-semibold text-gray-900 tracking-tight">
            Dhiraj Gupta
          </h2>

          <p className="mt-4 text-gray-600 text-lg leading-relaxed">
            Developer and Engineer passionate about Java,
            AI, MySQL, Agentic Systems, and modern web technologies.
          </p>

          {/* CV Buttons */}
          <div className="mt-8 flex gap-4">

            <a
              href="/resume.pdf"
              target="_blank"
              rel="noopener noreferrer"
              className="bg-[#131313] text-white px-6 py-3 rounded-xl hover:bg-black transition-colors font-medium shadow-sm"
            >
              View CV
            </a>

            <a
              href="/resume.pdf"
              download
              className="bg-[#D4ED31] text-[#131313] px-6 py-3 rounded-xl hover:bg-[#c4dc2e] transition-colors font-medium shadow-sm"
            >
              Download CV
            </a>

          </div>

          {/* Skills Section */}
          <div className="mt-10">

            <h3 className="text-2xl font-semibold text-gray-900 tracking-tight">
              Skills
            </h3>

            <div className="flex flex-wrap gap-3 mt-5">

              <span className="bg-gray-100 text-gray-800 px-4 py-2 rounded-lg font-medium border border-gray-200">
                Java
              </span>

              <span className="bg-gray-100 text-gray-800 px-4 py-2 rounded-lg font-medium border border-gray-200">
                AI
              </span>

              <span className="bg-gray-100 text-gray-800 px-4 py-2 rounded-lg font-medium border border-gray-200">
                MySQL
              </span>

              <span className="bg-gray-100 text-gray-800 px-4 py-2 rounded-lg font-medium border border-gray-200">
                Python
              </span>

              <span className="bg-gray-100 text-gray-800 px-4 py-2 rounded-lg font-medium border border-gray-200">
                AI Agents
              </span>

            </div>

          </div>

        </div>

      </div>

    </div>
  );
};

export default AboutMe;
