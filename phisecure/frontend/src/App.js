// Filename - App.js

import React, { useState, useEffect } from "react";
import { Routes, Route} from "react-router-dom";
import Header from "./pages/components/Header.js";
import Home from "./pages/Home";
import About from "./pages/About";
import Admin from "./pages/Admin.js";
import Contact from "./pages/Contact";
import CreateAccount from "./pages/CreateAccount.js";
import Dashboard from "./pages/Dashboard";
import DashboardInstructor from "./pages/DashboardInstructor.js";
import Dataanalytics from "./pages/Dataanalytics";
import Login from "./pages/Login";
import PhishingAssesment from "./pages/PhishingAssessment";
import PeerPhishing from "./pages/PeerPhishing.js";
import { ReportsInstructor } from "./pages/ReportsInstructor.js";
import { ReportsStudents } from "./pages/ReportsStudents.js";
import Services from "./pages/Services";
import SystemAnalytics from "./pages/SystemAnalytics";
import UserManagement from "./pages/UserManagement";
import ViewQuestionnaire from "./pages/components/ViewQuestionnaire.js";
import FetchPerformanceSummary from "./pages/components/FetchPerformanceSummary.js";
import FetchPerformanceDetailed from "./pages/components/FetchPerformanceDetailed.js";
import Inbox from './pages/components/Inbox';
import FetchID from "./pages/components/FetchID.js";
import PeerPhishingTemplate from "./pages/PeerPhishingTemplate.js"
import GmailClone from "./pages/components/GmailClone.js";

function App() {
  return (
        <>
            <Header />
            <Routes>
                <Route path="Home" element={<Home />} />
                <Route path="About" element={<About />} />
                <Route path="Admin" element={<Admin />} />
                <Route path="Contact" element={<Contact />} />
                <Route path="CreateAccount" element={<CreateAccount />} />
                <Route path="Dashboard" element={<Dashboard />} />
                <Route path="DashboardInstructor" element={<DashboardInstructor />} />
                <Route path="Dataanalytics" element={<Dataanalytics />} />
                <Route path="Login" element={<Login />} />
                <Route path="PeerPhishing" element={<PeerPhishing />} />
                <Route path="PhishingAssesment" element={<PhishingAssesment />} />
                <Route path="ReportsInstructor" element={<ReportsInstructor />} />
                <Route path="ReportsStudents" element={<ReportsStudents />} />
                <Route path="Services" element={<Services />} />
                <Route path="SystemAnalytics" element={<SystemAnalytics />} />
                <Route path="UserManagement" element={<UserManagement />} />
                <Route path="ViewQuestionnaire" element={<ViewQuestionnaire />} />
                <Route path="FetchPerformanceSummary" element={<FetchPerformanceSummary />} />
                <Route path="FetchPerformanceDetailed" element={<FetchPerformanceDetailed />} />
                <Route path="FetchID" element={<FetchID />} />
                <Route path="Inbox" element={<Inbox />} />
                <Route path="PeerPhishingTemplate" element={<PeerPhishingTemplate />} />
                <Route path="GmailClone" element={<GmailClone />} />
            </Routes>
        </>
  );
}

export default App;