import React from 'react';
import './output.css';

function Navbar() {
    return (
        <div class="container w-full bg-blue-300">
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </div>
    );
}

export default Navbar;
