import './App.css';
import Navbar from './components/Navbar';
import Home from './components/Home';
import { Routes, Route } from "react-router-dom";
import Booking from './components/Booking'
import Signin from './components/Signin'
import Signup from './components/signup'
import Admin from './components/Admin';


function App() {
  return (
    <>
    <div className="App">
      
      <Navbar/>
      <Routes>
        <Route exact path="/" element={<Home />}/>
      </Routes>
      <Routes>
        <Route path="/Booking" element={<Booking />}/>
      </Routes>
      <Routes>
        <Route path="/Booking" element={<Booking />}/>
      </Routes>
      <Routes>
        <Route path='signup' element={<Signup/>}/>
      </Routes>
      <Routes>
        <Route path="/Signin" element={<Signin />}/>
      </Routes>
      <Routes>
        <Route path="/admin" element={<Admin />}/>
      </Routes>
    </div>
    </>
  );
}
export default App;
