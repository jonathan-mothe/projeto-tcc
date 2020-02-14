import React from 'react';
import Header from './Header';
import Sobre from './Sobre';
import './App.css';

export default class App extends React.Component{
    render(){
        return(
            <div>
                <Header />
                <Sobre />
            </div>
        );
    }
}