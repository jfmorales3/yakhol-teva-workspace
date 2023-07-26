import React, { createContext, useState, useEffect } from "react";
import Cookies from "js-cookie";

export const UserContext = createContext(null);

export const UserProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const authToken = Cookies.get("authToken");
    const userType = parseInt(Cookies.get("userType"));

    if (authToken && userType) {
      setUser({
        user_type: userType,
        auth_token: authToken,
      });
    }
    setLoading(false);
  }, []);

  return (
    <UserContext.Provider value={{ user, setUser, loading }}>
      {children}
    </UserContext.Provider>
  );
};
