import { useContext, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { UserContext } from './UserContext';

const RedirectIfAuthenticated = () => {
  const { user, loading } = useContext(UserContext);
  const navigate = useNavigate();

  useEffect(() => {
    if (!loading) {  
      if (user) {
        switch (user.user_type) {
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
            navigate("/login");
        }
      } else {
        navigate('/login');
      }
    }
  }, [user, navigate, loading]);  

  return null;
};

export default RedirectIfAuthenticated;
