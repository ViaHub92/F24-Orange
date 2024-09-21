import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import logo from './phisecurelogo.png';
import { useState, useEffect } from "react";
import './style.css';

function Header() {
  return (
    <header>
      <nav className="nav">
        <img src={logo} alt={"logo"} className="nav-logo" />
        <ul className="nav-items">
          <li>About</li>
          <li>Privacy</li>
          <li>Help</li>
        </ul>
      </nav>
    </header>
  )
};

function HelloWorld() {
  return <h1 className="greeting">Hello world!</h1>;
};
/*
function MainContent(){

  const [testfetch, setdata] = useState({
    name: "",
});

// Using useEffect for single rendering
useEffect(() => {
    // Using fetch to fetch the api from 
    // flask server it will be redirected to proxy
    fetch("/testfetch").then((res) =>
        res.json().then((testfetch) => {
            // Setting a data from api
            setdata({
                name: testfetch.Name,
            });
        })
    );
}, []);

return <h1 classname="fetch">Fetch here</h1>(
  <p>testfetch.name</p>

  );
}
}
*/

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Header />
    <HelloWorld />
    <App />
  </React.StrictMode>
);
