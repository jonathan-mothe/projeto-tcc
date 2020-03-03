import React from 'react';
import Header from './components/Header';
import Sobre from './components/Sobre';
import './App.css';
import Conteudo from './components/Conteudo';

export default class App extends React.Component{
    render(){
        return(
            <div>
                <Header />
                <Sobre />
                <Conteudo />
            </div>
        );
    }
}