import React from 'react';

export default class Header extends React.Component{
    render(){
        return(
            <div className="navmenu">
                <div id="menu">
                <a href="http://localhost:3000/">Home</a>

                <div id="sobre">
                    <a href="http://localhost:3000/sobre">Sobre</a></div>
                </div>
                
                <div id="login">
                    <a href="http://127.0.0.1:8000/admin">Login</a>
                </div>

            </div>
        );
    }
}