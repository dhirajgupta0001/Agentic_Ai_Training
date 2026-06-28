// import Container from "../components/container";

// const AgenticAI = () => {
//   return (
//     <div>
//       <Container />
//     </div>
//   );
// };

// export default AgenticAI;

import Container from "../components/container";

const AgenticAI = () => {
  return (
    <div>
      <div className="text-center p-10 font-sans">
        <h1 className="text-[40px] font-bold text-gray-900 tracking-tight leading-tight">
          Agentic AI Workspace
        </h1>

        <p className="mt-4 text-[18px] text-gray-600">
          Create, test and deploy intelligent AI agents.
        </p>
      </div>

      <Container />

      {/* <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 p-10">
        <div className="bg-white shadow-sm border border-gray-100 p-6 rounded-xl text-gray-900 font-medium">
          Memory Agent
        </div>

        <div className="bg-white shadow-sm border border-gray-100 p-6 rounded-xl text-gray-900 font-medium">
          Web Search Agent
        </div>

        <div className="bg-white shadow-sm border border-gray-100 p-6 rounded-xl text-gray-900 font-medium">
          PDF Agent
        </div>

        <div className="bg-white shadow-sm border border-gray-100 p-6 rounded-xl text-gray-900 font-medium">
          Code Agent
        </div>
      </div> */}
    </div>
  );
};

export default AgenticAI;
