import React, { useState, useEffect } from 'react';
import axios from 'axios';

const FlightStatus = () => {
    const [flights, setFlights] = useState([]);

    useEffect(() => {
        axios.get('http://127.0.0.1:5000/api/flights')
            .then(response => {
                setFlights(response.data);
            })
            .catch(error => {
                console.error('There was an error fetching the flight data!', error);
            });
    }, []);

    return (
        <div>
            <h1>Flight Status</h1>
            <ul>
                {flights.map(flight => (
                    <li key={flight.flight_number}>
                        <strong>{flight.flight_number}</strong> - {flight.status} - Gate: {flight.gate}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default FlightStatus;
