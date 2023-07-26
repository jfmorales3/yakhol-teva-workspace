import React, { useEffect, useContext } from "react";
import { Route, Routes } from "react-router-dom";
import { UserContext } from "../../UserContext";
import ComercialNavbar from "./ComercialNavbar";
import ComercialDashboard from "./ComercialDashboard";
import Sales from "./Sales";
import Team from "./Team";
import Tokens from "./Tokens";
import PersonalData from "./PersonalData";
// importa los demás componentes aquí

function MainComercial() {
  const { user, setUser } = useContext(UserContext);

  useEffect(() => {
    const requestOptions = {
      method: "GET",
      headers: { "Content-Type": "application/json" },
      credentials: "include",
    };

    fetch("/api/user-details/", requestOptions)
      .then(response => {
        if (!response.ok) {
          throw new Error("Error: " + response.statusText);
        }
        return response.json();
      })
      .then(data => {
        setUser(data);
      })
      .catch(e => console.error(e));
  }, [setUser]);

  if (!user) {
    return <p>Cargando...</p>;
  }

  return (
    <UserContext.Provider value={{ user }}>
      <ComercialNavbar />
      <Routes>
        <Route path="/" element={<ComercialDashboard />} />
        <Route path="sales" element={<Sales />} />
        <Route path="team" element={<Team />} />
        <Route path="tokens" element={<Tokens />} />
        <Route path="personal_data" element={<PersonalData />} />
        {/* Aquí definirías las demás rutas para las otras secciones de tu dashboard */}
      </Routes>
    </UserContext.Provider>
  );
}

export default MainComercial;
