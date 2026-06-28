// import { NavLink } from "react-router-dom";
// const Header = () => {
//   return(
//     <div className='header flex w-full h-auto py-4 px-6 bg-blue-200 justify-between items-center'>
//       <h3 className='text-teal-600 font-bold text-2xl'>CodeNoids</h3>
//       <div className="navigations flex">
//           {/* <h4 className='text-teal-900 font-bold text-xl px-4'> Home </h4>
//           <h4 className='text-teal-900 font-bold text-xl px-4'> Agentic AI </h4>
//           <h4 className='text-teal-900 font-bold text-xl px-4'> Marketlace </h4>
//           <h4 className='text-teal-900 font-bold text-xl px-4'> Settings </h4>
//       </div> */}
//        <NavLink
//           to="/"
//           className="text-white hover:text-cyan-400"
//         >
//           Home
//         </NavLink>

//         <NavLink
//           to="/agentic-ai"
//           className="text-white hover:text-cyan-400"
//         >
//           Agentic AI
//         </NavLink>

//         <NavLink
//           to="/marketplace"
//           className="text-white hover:text-cyan-400"
//         >
//           Marketplace
//         </NavLink>

//         <NavLink
//           to="/settings"
//           className="text-white hover:text-cyan-400"
//         >
//           Settings
//         </NavLink>

//       </div>
//     </div>
//   )
// }
// export default Header;

const Header = () => {
  return (
    <div className="w-full h-20 bg-[#131313] flex justify-between items-center px-10 shadow-sm">

      <h1 className="text-white text-3xl font-bold tracking-tight">
        CodeNoids
      </h1>

      <div className="flex gap-8 text-gray-300 font-medium text-lg">

        <a href="/" target="_blank" className="hover:text-white transition-colors">
          Home
        </a>

        <a href="/agentic-ai" target="_blank" className="hover:text-white transition-colors">
          Agentic AI
        </a>

        <a href="/marketplace" target="_blank" className="hover:text-white transition-colors">
          Marketplace
        </a>

        <a href="/settings" target="_blank" className="hover:text-white transition-colors">
          Settings
        </a>

        <a href="/aboutme" target="_blank" rel="noopener noreferrer" className="hover:text-white transition-colors"> 
          AboutMe
        </a>

      </div>
    </div>
  );
};

export default Header;
