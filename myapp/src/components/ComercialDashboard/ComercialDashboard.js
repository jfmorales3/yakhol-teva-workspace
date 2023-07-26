import React, { useContext } from 'react';
import { UserContext } from '../../UserContext';
import ComercialNavbar from './ComercialNavbar';
// importa los demás componentes aquí

function ComercialDashboard() {
    const { user } = useContext(UserContext);

    return (
        <div>
            {user ?
                <>
                    <h1>Bienvenido, {user.nombre}</h1>
                    <p>Correo: {user.correo}</p>
                    <p>Telefono: {user.telefono}</p>
                    <p>Lider: {user.lider && user.lider.length > 0 ? user.lider[0] : 'No asignado'}</p>
                    {/* Mostrar más datos según sea necesario */}
                </> :
                <p>Cargando...</p>
            }
        </div>
    );
}

export default ComercialDashboard;
