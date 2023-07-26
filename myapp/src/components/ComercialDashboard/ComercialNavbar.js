import React from 'react';
import { Nav, Navbar } from 'react-bootstrap';
import { IoIosHome, IoIosPaper, IoMdPeople, IoIosCreate, IoIosCash } from 'react-icons/io';
import { useNavigate } from 'react-router-dom';
import './ComercialNavbar.css';

const ComercialNavbar = () => {
    const navigate = useNavigate();

    return (
        <Navbar bg="dark" variant="dark">
            <Navbar.Brand href="#" onClick={() => navigate("/comercial")}><IoIosHome /></Navbar.Brand>
            <Nav className="mr-auto">
                <Nav.Link onClick={() => navigate("sales")}><IoIosPaper /> Mis Ventas</Nav.Link>
                <Nav.Link onClick={() => navigate("team")}><IoMdPeople /> Mi Equipo</Nav.Link>
                <Nav.Link onClick={() => navigate("tokens")}><IoIosCash /> Mis Tokens</Nav.Link>
                <Nav.Link onClick={() => navigate("personal_data")}><IoIosCreate /> Modificar Datos Personales</Nav.Link>
            </Nav>
        </Navbar>
    );
};

export default ComercialNavbar;
