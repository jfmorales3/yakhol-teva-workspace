import React, { useState, useEffect, useContext } from "react";
import { UserContext } from '../../UserContext';
import { Table } from 'react-bootstrap';
import './Sales.css';

function Sales() {
    const { user } = useContext(UserContext);
    const [contratos, setContratos] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() => {
        const requestOptions = {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' },
            credentials: 'include',
        };
    
        fetch(`/api/comercial/contratos?comercialId=${user.id}`, requestOptions)
        .then(response => {
            if (!response.ok) {
                throw new Error('Error: ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            setContratos(data);
        })
        .catch(e => {
            console.error(e);
            setError(e.message);
        });
    }, [user.id]);

    if (error) {
        return <p>Ha ocurrido un error al cargar tus ventas: {error}</p>;
    }

    if (!contratos) {
        return <p>Cargando...</p>;
    }

    return (
        <div className="sales">
            <h1>Mis Ventas</h1>
            <Table striped bordered hover>
                <thead>
                    <tr>
                        <th>ID CONTRATO</th>
                        <th>TIPO CONTRATO</th>
                        <th>Valor Semana</th>
                        <th>Valor pagado</th>
                        <th>Saldo restante</th>
                    </tr>
                </thead>
                <tbody>
                    {contratos.map(contrato => (
                        <tr key={contrato.id}>
                            <td>{contrato.id}</td>
                            <td>{contrato.tipoContrato}</td>
                            <td>{contrato.valorSemana}</td>
                            <td>{contrato.valorPagado}</td>
                            <td>{contrato.saldoRestante}</td>
                        </tr>
                    ))}
                </tbody>
            </Table>
        </div>
    );
}

export default Sales;
