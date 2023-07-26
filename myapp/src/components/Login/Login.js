import React, { useState, useEffect, useContext } from "react";
import { Link, useNavigate } from "react-router-dom";
import Cookies from "js-cookie";
import { UserContext } from "../../UserContext";

function Login() {
  const { setUser } = useContext(UserContext); // Acceder a setUser de UserContext
  const [email, setEmail] = useState(""); // Cambia 'username' por 'email'
  const [password, setPassword] = useState("");
  const [errorMessage, setErrorMessage] = useState("");
  const [csrfToken, setCsrfToken] = useState("");

  const navigate = useNavigate();

  useEffect(() => {
    const csrfTokenFromCookies = Cookies.get("csrftoken");
    setCsrfToken(csrfTokenFromCookies);
  }, []);

  function handleEmailChange(event) {
    // Cambia 'handleUsernameChange' por 'handleEmailChange'
    setEmail(event.target.value);
  }

  function handlePasswordChange(event) {
    setPassword(event.target.value);
  }

  function handleSubmit(event) {
    event.preventDefault();

    const csrfToken = Cookies.get("csrftoken");

    const requestOptions = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrfToken,
      },
      body: JSON.stringify({ email: email, password: password }),
      credentials: "include",
    };

    fetch("/dj-rest-auth/login/", requestOptions)
      .then(response => {
        if (!response.ok) {
          response.text().then(text => {
            setErrorMessage("Error: " + text);
          });
          throw new Error("Error: " + response.statusText);
        }
        return response.json();
      })
      .then(data => {
        setUser({ user_type: data.user_type, auth_token: csrfToken });
        Cookies.set("authToken", data.key);
        Cookies.set("userType", data.user_type);
        console.log(Cookies.get("authToken"), Cookies.get("userType")); // Debería mostrar el authToken y el userType

        switch (data.user_type) {
          case 1:
            navigate("/admin_dashboard");
            break;
          case 2:
            navigate("/comercial");
            break;
          case 3:
            navigate("/associated_dashboard");
            break;
          default:
            setErrorMessage("Tipo de usuario no reconocido");
        }
      })
      .catch(e => console.error(e));
  }

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input type="hidden" name="csrfmiddlewaretoken" value={csrfToken} />

        <label>
          Correo:
          <input type="text" value={email} onChange={handleEmailChange} />{" "}
        </label>
        <label>
          Contraseña:
          <input
            type="password"
            value={password}
            onChange={handlePasswordChange}
          />
        </label>
        <input type="submit" value="Ingresar" />
      </form>
      <Link to="/register">Crear una cuenta</Link>
      {errorMessage && <p>{errorMessage}</p>}
    </div>
  );
}

export default Login;
