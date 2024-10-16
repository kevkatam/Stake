import React from 'react';
import logo from '../assets/stake_logo.png';


function Header() {


    return (
        <div className="header">
            <img src={logo} alt="Stake logo" height="150"/>
        </div>
    );
}

export default Header;