import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { UserProvider } from './UserContext';
import Login from "./components/Login/Login";
import AdminDashboard from "./components/AdminDashboard/AdminDashboard";
import AssociatedDashboard from "./components/AssociatedDashboard/AssociatedDashboard";
import MainComercial from "./components/ComercialDashboard/MainComercial";
import RedirectIfAuthenticated from './RedirectIfAuthenticated';

function App() {
  return (
    <UserProvider>
      <Router>
        <Routes>
          <Route path="/" element={<RedirectIfAuthenticated />} />
          <Route path="/login" element={<RedirectIfAuthenticated />} />
          <Route path="/admin_dashboard" element={<AdminDashboard />} />
          <Route path="/comercial/*" element={<MainComercial />} />
          <Route path="/associated_dashboard" element={<AssociatedDashboard />} />
        </Routes>
      </Router>
    </UserProvider>
  );
}

export default App;
