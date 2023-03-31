import HomePage from 'pages/HomePage';
import LoginPage from 'pages/LoginPage';
import RegisterPage from 'pages/RegisterPage';
import {Routes, Route} from 'react-router-dom'

function App() {
  return (
    <Routes>
      <Route exact path="/" component={HomePage} />
      <Route exact path="/login" component={LoginPage} />
      <Route exact path="/register" component={RegisterPage} />
    </Routes>
  );
}

export default App;
