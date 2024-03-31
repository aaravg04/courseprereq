import React from 'react';
import Navbar from './Navbar'


function Home() {
    return (
        <div className='w-full h-screen bg-zinc-900'>
            <Navbar />
            <div class="grid grid-cols-3 gap-4 place-items-center h-56 ...">
                <div>01</div>
                <div>02</div>
                <div>03</div>
                <div>04</div>
                <div>05</div>
                <div>06</div>
            </div>
        </div>
    );
}

export default Home;