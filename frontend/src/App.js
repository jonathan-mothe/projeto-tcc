import React from 'react';
import Header from './components/Header';
import Sobre from './components/Sobre';
import './App.css';
import Conteudo from './components/Conteudo';
import Logo from './components/Logo';

export default class App extends React.Component{
    render(){
        return(
            <div>
                <Header />
                <Logo />
                <Sobre />
                <Conteudo />
            </div>
        );
    }
}