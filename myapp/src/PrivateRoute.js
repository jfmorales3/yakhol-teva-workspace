import { useNavigate } from 'react-router-dom';
import { UserContext } from './UserContext';
import { useContext, useEffect } from 'react';

const PrivateRoute = ({children}) => {
  const { user } = useContext(UserContext);
  let navigate = useNavigate();
  
  useEffect(() => {
    if (!user) {
      navigate("/login");
    }
  }, [user, navigate]);

  return user ? children : null;
};

export default PrivateRoute;

