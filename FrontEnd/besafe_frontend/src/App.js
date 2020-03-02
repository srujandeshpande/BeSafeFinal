import React from 'react';
import './App.css';
import Home from './Home';
import Map from './Map';
import Intermediate from './Intermediate'
import {BrowserRouter, Route, Switch} from 'react-router-dom';


function App() {
  return (
    <div className="App">
      <BrowserRouter>
          <switch>
            <Route exact path='/'  component={Home} />
            <Route exact path='/map' component={Map} />
          </switch>
        </BrowserRouter>
    </div>
  );
}

export default App;
