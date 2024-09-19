import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import logo from './phisecurelogo.png';
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
}
function HelloWorld() {
  return <h1 className="greeting">Hello world!</h1>;
}

function MainContent(){
  return <h1>I'm Learning React!</h1>
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Header />
    <HelloWorld />
    <MainContent />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
