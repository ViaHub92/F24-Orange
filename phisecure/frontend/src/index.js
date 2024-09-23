import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import { useState, useEffect } from "react";
import './style.css';
import Header from './Header'

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
  <div>
    <Header />
    <App />
    
  </div>
);
