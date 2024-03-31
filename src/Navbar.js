/* ------------------------------ React Imports ----------------------------- */
import React from 'react';
import { CgProfile } from "react-icons/cg";

/* ------------------------------- CSS Import ------------------------------- */
import './output.css';


function Navbar() {
    return (
        <nav className="flex justify-between items-center px-40 py-4 bg-zinc-9">

            <div className="flex items-center space-x-2">
            <img src="/path-to-icon" alt="logo" />
                <p className='text-white'>GT Course Prereq</p>
                
            </div>

            <div className="flex space-x-4">
                <a href="#home" className="text-white">Home</a>
                <a href="#visualization" className="text-white">Visualization</a>
                <a href="#transcript-upload" className="text-white">Transcript Upload</a>
                <a href="#planner" className="text-white">Planner</a>
            </div>
        </nav>
    );
}

export default Navbar;
