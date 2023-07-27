import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate} from 'react-router-dom';
import { UserProvider } from './UserContext';
import Login from "./components/Login/Login";
import AdminDashboard from "./components/AdminDashboard/AdminDashboard";
import AssociatedDashboard from "./components/AssociatedDashboard/AssociatedDashboard";
import MainComercial from "./components/ComercialDashboard/MainComercial";
import PrivateRoute from './PrivateRoute';
import RedirectIfAuthenticated from './RedirectIfAuthenticated';


function App() {
  return (
    <UserProvider>
      <Router>
        <Routes>
          <Route path="/" element={<Navigate to="/login" />} />
          <Route path="/login" element={<RedirectIfAuthenticated><Login /></RedirectIfAuthenticated>} />
          <Route path="/admin_dashboard" element={<PrivateRoute><AdminDashboard /></PrivateRoute>} />
          <Route path="/comercial/*" element={<PrivateRoute><MainComercial /></PrivateRoute>} />
          <Route path="/associated_dashboard" element={<PrivateRoute><AssociatedDashboard /></PrivateRoute>} />
        </Routes>
      </Router>
    </UserProvider>
  );
}

export default App;
