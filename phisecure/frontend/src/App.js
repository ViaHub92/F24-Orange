// Filename - App.js

import React, { useState, useEffect } from "react";
import { Routes, Route} from "react-router-dom";
import fetchAllUsers from "./components/FetchUsers";
import Header from "./components/Header";
import Login from "./pages/Login";
import Contact from "./pages/Contact";

function App() {
  return (
        <>
            <Header />
            <Routes>
                <Route path="Contact" element={<Contact />} />
                <Route path="Login" element={<Login />} />
            </Routes>
        </>
  );
}

export default App;